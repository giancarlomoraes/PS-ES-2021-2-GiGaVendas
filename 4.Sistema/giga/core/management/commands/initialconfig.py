from django.core.management.base import BaseCommand
from global_permissions.models import GlobalPermission
from comercio.models import FuncaoColaborador


def create_permissions_and_functions():
    try:
        lista_permissoes = [
            ('Pode Criar Cliente', 'can_add_cliente'),
            ('Pode Ver Clientes', 'can_see_clientes'),
            ('Pode Editar Cliente', 'can_edit_cliente'),
            ('Pode Deletar Cliente', 'can_delete_cliente'),
            ('Pode Alterar Senha do Cliente', 'can_edit_cliente_password'),
            ('Pode Criar Colaborador', 'can_add_colaborador'),
            ('Pode Ver Colaboradores', 'can_see_colaboradores'),
            ('Pode Editar Colaborador', 'can_edit_colaborador'),
            ('Pode Deletar Colaborador', 'can_delete_colaborador'),
            ('Pode Alterar Senha do Colaborador', 'can_edit_colaborador_password'),
            ('Pode Criar Venda', 'can_add_venda'),
            ('Pode Ver Vendas', 'can_see_vendas'),
            ('Pode Editar Venda', 'can_edit_venda'),
            ('Pode Deletar Venda', 'can_delete_venda'),
            ('Pode Criar Item', 'can_add_item'),
            ('Pode Ver Itens', 'can_see_itens'),
            ('Pode Deletar Item', 'can_delete_item'),
            ('Pode Criar Produto', 'can_add_produto'),
            ('Pode Ver Produtos', 'can_see_produtos'),
            ('Pode Editar Produto', 'can_edit_produto'),
            ('Pode Deletar Produto', 'can_delete_produto'),
            ('Pode Ver Balanço', 'can_see_balanco'),
        ]

        for permissao in lista_permissoes:
            GlobalPermission.objects.get_or_create(name=permissao[0], codename=permissao[1])

        lista_funcoes_colaboradores = [
            {
                'nome': 'Administrador',
                'permissoes': [
                    GlobalPermission.objects.get(codename="can_add_cliente"),
                    GlobalPermission.objects.get(codename="can_see_clientes"),
                    GlobalPermission.objects.get(codename="can_edit_cliente"),
                    GlobalPermission.objects.get(codename="can_delete_cliente"),
                    GlobalPermission.objects.get(codename="can_edit_cliente_password"),
                    GlobalPermission.objects.get(codename="can_add_colaborador"),
                    GlobalPermission.objects.get(codename="can_see_colaboradores"),
                    GlobalPermission.objects.get(codename="can_edit_colaborador"),
                    GlobalPermission.objects.get(codename="can_delete_colaborador"),
                    GlobalPermission.objects.get(codename="can_edit_colaborador_password"),
                    GlobalPermission.objects.get(codename="can_add_venda"),
                    GlobalPermission.objects.get(codename="can_see_vendas"),
                    GlobalPermission.objects.get(codename="can_edit_venda"),
                    GlobalPermission.objects.get(codename="can_delete_venda"),
                    GlobalPermission.objects.get(codename="can_add_item"),
                    GlobalPermission.objects.get(codename="can_see_itens"),
                    GlobalPermission.objects.get(codename="can_delete_item"),
                    GlobalPermission.objects.get(codename="can_add_produto"),
                    GlobalPermission.objects.get(codename="can_see_produtos"),
                    GlobalPermission.objects.get(codename="can_edit_produto"),
                    GlobalPermission.objects.get(codename="can_delete_produto"),
                    GlobalPermission.objects.get(codename="can_see_balanco"),
                ]
            },
            {
                'nome': 'Gestor',
                'permissoes': [
                    GlobalPermission.objects.get(codename="can_add_cliente"),
                    GlobalPermission.objects.get(codename="can_see_clientes"),
                    GlobalPermission.objects.get(codename="can_edit_cliente"),
                    GlobalPermission.objects.get(codename="can_delete_cliente"),
                    GlobalPermission.objects.get(codename="can_edit_cliente_password"),
                    GlobalPermission.objects.get(codename="can_add_colaborador"),
                    GlobalPermission.objects.get(codename="can_see_colaboradores"),
                    GlobalPermission.objects.get(codename="can_edit_colaborador"),
                    GlobalPermission.objects.get(codename="can_delete_colaborador"),
                    GlobalPermission.objects.get(codename="can_edit_colaborador_password"),
                    GlobalPermission.objects.get(codename="can_add_venda"),
                    GlobalPermission.objects.get(codename="can_see_vendas"),
                    GlobalPermission.objects.get(codename="can_edit_venda"),
                    GlobalPermission.objects.get(codename="can_delete_venda"),
                    GlobalPermission.objects.get(codename="can_add_item"),
                    GlobalPermission.objects.get(codename="can_see_itens"),
                    GlobalPermission.objects.get(codename="can_delete_item"),
                    GlobalPermission.objects.get(codename="can_add_produto"),
                    GlobalPermission.objects.get(codename="can_see_produtos"),
                    GlobalPermission.objects.get(codename="can_edit_produto"),
                    GlobalPermission.objects.get(codename="can_delete_produto"),
                    GlobalPermission.objects.get(codename="can_see_balanco"),
                ]
            },
            {
                'nome': 'Caixa',
                'permissoes': [
                    GlobalPermission.objects.get(codename="can_add_cliente"),
                    GlobalPermission.objects.get(codename="can_see_clientes"),
                    GlobalPermission.objects.get(codename="can_edit_cliente"),
                    GlobalPermission.objects.get(codename="can_delete_cliente"),
                    GlobalPermission.objects.get(codename="can_edit_cliente_password"),
                    GlobalPermission.objects.get(codename="can_add_venda"),
                    GlobalPermission.objects.get(codename="can_see_vendas"),
                    GlobalPermission.objects.get(codename="can_edit_venda"),
                    GlobalPermission.objects.get(codename="can_delete_venda"),
                    GlobalPermission.objects.get(codename="can_add_item"),
                    GlobalPermission.objects.get(codename="can_see_itens"),
                    GlobalPermission.objects.get(codename="can_delete_item"),
                ]
            },
        ]

        for funcao in lista_funcoes_colaboradores:
            colaborador, created = FuncaoColaborador.objects.get_or_create(nome=funcao['nome'])
            for permissao in funcao['permissoes']:
                if permissao not in colaborador.permissoes.all():
                    colaborador.permissoes.add(permissao)

    except Exception as e:
        print(e)


class Command(BaseCommand):
    help = 'Criar configurações iniciais do sistema, assim como permissões.'

    def handle(self, *args, **kwargs):
        create_permissions_and_functions()
