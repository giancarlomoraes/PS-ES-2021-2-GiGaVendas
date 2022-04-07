from django.core.exceptions import PermissionDenied
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User, Permission
from django.db.models.signals import pre_save, post_save, post_delete, pre_delete, m2m_changed
from django.dispatch import receiver
from datetime import datetime


class Cliente(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cliente_user", null=True, blank=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    complemento = models.CharField(max_length=100)
    rua = models.CharField(max_length=100)
    numero = models.IntegerField()
    telefone = models.CharField(
        validators=[RegexValidator(regex='\([\d]{2}\) [\d]{5}-[\d]{4}', message='Telefone Inválido',
                                   code='nomatch')], max_length=15, null=True, blank=True)
    cpf = models.CharField(validators=[RegexValidator(regex='^\d{3}\.\d{3}\.\d{3}\-\d{2}$', message='CPF Inválido',
                                                      code='nomatch')], max_length=14)

    class Meta:
        ordering = ['user']
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)


class Colaborador(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="colaborador_user", null=True, blank=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    complemento = models.CharField(max_length=100)
    rua = models.CharField(max_length=100)
    numero = models.IntegerField()
    telefone = models.CharField(
        validators=[RegexValidator(regex='\([\d]{2}\) [\d]{5}-[\d]{4}', message='Telefone Inválido',
                                   code='nomatch')], max_length=15, null=True, blank=True)
    cpf = models.CharField(validators=[RegexValidator(regex='^\d{3}\.\d{3}\.\d{3}\-\d{2}$', message='CPF Inválido',
                                                      code='nomatch')], max_length=14)
    salario = models.FloatField()
    funcao = models.ForeignKey('FuncaoColaborador', on_delete=models.SET_NULL, null=True,
                               related_name='funcao_colaborador')

    class Meta:
        ordering = ['user']
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)


class FuncaoColaborador(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    permissoes = models.ManyToManyField(Permission, blank=True, verbose_name="Permissões",
                                        related_name='permissoes_funcao_colaborador')

    class Meta:
        ordering = ['nome']
        verbose_name = 'Função'
        verbose_name_plural = 'Funções'

    def __str__(self):
        return '{}'.format(self.nome)


class Produto(models.Model):
    nome = models.CharField(max_length=150)
    preco = models.FloatField()
    quantidade = models.PositiveIntegerField()

    class Meta:
        ordering = ['nome']
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return '{}'.format(self.nome)


class Venda(models.Model):
    valor = models.FloatField(blank=True, null=True)
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE, related_name="venda_colaborador", null=True,
                                    blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="venda_cliente", null=True,
                                blank=True)
    data_hora = models.DateTimeField(default=datetime.now, blank=True)

    METODO_PAGAMENTO_CHOICES = [
        (1, 'Cartão de Crédito'),
        (2, 'Cartão de Débito'),
        (3, 'Dinheiro'),
        (4, 'Pix'),
    ]

    metodo_pagamento = models.IntegerField(choices=METODO_PAGAMENTO_CHOICES)

    class Meta:
        ordering = ['valor']
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'

    def __str__(self):
        return '{} - {}'.format(self.valor, self.cliente)


class Item(models.Model):
    quantidade = models.PositiveIntegerField(blank=True, null=True)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name="itens_produto", null=True,
                                blank=True)
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name="itens_venda", null=True,
                              blank=True)
    descontado_estoque = models.BooleanField(blank=True, null=True)

    class Meta:
        ordering = ['produto']
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'

    def __str__(self):
        return '{}'.format(self.produto)


@receiver(post_delete, sender=Cliente)
def delete_cliente(sender, instance, *args, **kwargs):
    if instance.user:
        User.objects.get(pk=instance.user.pk).delete()


@receiver(post_delete, sender=Colaborador)
def delete_colaborador(sender, instance, *args, **kwargs):
    if instance.user:
        User.objects.get(pk=instance.user.pk).delete()


@receiver(pre_delete, sender=User)
def delete_user(sender, instance, *args, **kwargs):
    if instance.cliente_user.all().first() is not None:
        raise PermissionDenied()
    elif instance.colaborador_user.all().first() is not None:
        raise PermissionDenied()


@receiver(post_save, sender=Colaborador)
def save_colaborador(sender, instance, created, *args, **kwargs):
    if created:
        if instance:
            user = instance.user
            for permission in instance.funcao.permissoes.all():
                user.user_permissions.add(permission)


@receiver(pre_save, sender=Colaborador)
def edit_colaborador(sender, instance, *args, **kwargs):
    if instance.id:
        colaborador = Colaborador.objects.get(id=instance.id)
        if colaborador.funcao != instance.funcao:
            user = instance.user
            user.user_permissions.set([])
            for permission in instance.funcao.permissoes.all():
                user.user_permissions.add(permission)


@receiver(m2m_changed, sender=FuncaoColaborador.permissoes.through)
def edit_colaborador(sender, instance, action, *args, **kwargs):
    if action in ["post_add", "post_remove", "post_clear"]:
        colaboradores = Colaborador.objects.filter(funcao=instance)
        for colaborador in colaboradores:
            user = colaborador.user
            user.user_permissions.set([])
            for permission in instance.permissoes.all():
                user.user_permissions.add(permission)
