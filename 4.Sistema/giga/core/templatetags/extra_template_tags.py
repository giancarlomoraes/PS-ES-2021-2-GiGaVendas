from django import template
from comercio.models import Colaborador
from django.contrib.auth.models import Permission

register = template.Library()


@register.simple_tag
def check_permission(user, permission_required):
    user_permissions = user.user_permissions.all()
    permission = Permission.objects.get(codename=permission_required)
    if permission in user_permissions:
        return True
    else:
        return False


@register.simple_tag
def count_metodo_pagamento(vendas, metodo_pagamento):
    count = 0
    for venda in vendas:
        if venda.get_metodo_pagamento_display() == metodo_pagamento:
            count += 1
    return count


@register.simple_tag
def count_valor_vendas(vendas):
    valor = 0
    for venda in vendas:
        valor += venda.valor
    return valor


@register.simple_tag
def count_produtos_vendas(vendas):
    count = 0
    for venda in vendas:
        for item in venda.itens_venda.all():
            count += item.quantidade
    return count


@register.simple_tag
def top_tres_colaboradores(vendas):
    colaboradores = Colaborador.objects.all()
    ocorrencias = []
    for colaborador in colaboradores:
        ocorrencias.append({'colaborador': colaborador, 'vendas': len(vendas.filter(colaborador=colaborador))})

    top1, top2, top3 = {'colaborador': None, 'vendas': 0}, {'colaborador': None, 'vendas': 0}, {'colaborador': None, 'vendas': 0}

    for ocorrencia in ocorrencias:
        if ocorrencia['vendas'] > top1['vendas']:
            top1 = ocorrencia

    if top1 in ocorrencias:
        ocorrencias.pop(ocorrencias.index(top1))

    for ocorrencia in ocorrencias:
        if ocorrencia['vendas'] > top2['vendas']:
            top2 = ocorrencia

    if top2 in ocorrencias:
        ocorrencias.pop(ocorrencias.index(top2))

    for ocorrencia in ocorrencias:
        if ocorrencia['vendas'] > top3['vendas']:
            top3 = ocorrencia

    if top3 in ocorrencias:
        ocorrencias.pop(ocorrencias.index(top3))
    return top1, top2, top3
