from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FloatConverter, 'float')

urlpatterns = [
    path('clientes/listar/', views.ListarClientes.as_view(), name='listar_clientes'),
    path('clientes/adicionar/', views.adicionar_cliente, name='adicionar_cliente'),
    path('clientes/<int:pk>/editar/', views.editar_cliente, name='editar_cliente'),
    path('clientes/<int:pk>/deletar/', views.DeletarCliente.as_view(), name='deletar_cliente'),
    path('clientes/<int:pk>/editar-senha/', views.change_cliente_password, name='change_cliente_password'),
    path('colaboradores/listar/', views.ListarColaboradores.as_view(), name='listar_colaboradores'),
    path('colaboradores/adicionar/', views.adicionar_colaborador, name='adicionar_colaborador'),
    path('colaboradores/<int:pk>/editar/', views.editar_colaborador, name='editar_colaborador'),
    path('colaboradores/<int:pk>/deletar/', views.DeletarColaborador.as_view(), name='deletar_colaborador'),
    path('colaboradores/<int:pk>/editar-senha/', views.change_colaborador_password, name='change_colaborador_password'),
    path('produtos/listar/', views.ListarProdutos.as_view(), name='listar_produtos'),
    path('produtos/adicionar/', views.AdicionarProduto.as_view(), name='adicionar_produto'),
    path('produtos/<int:pk>/editar/', views.EditarProduto.as_view(), name='editar_produto'),
    path('produtos/<int:pk>/deletar/', views.DeletarProduto.as_view(), name='deletar_produto'),
    path('vendas/listar/', views.ListarVendas.as_view(), name='listar_vendas'),
    path('vendas/adicionar/', views.AdicionarVenda.as_view(), name='adicionar_venda'),
    path('vendas/finalizar/<int:pk>/<float:valor>/', views.finalizar_venda, name='finalizar_venda'),
    path('vendas/<int:pk>/editar/', views.EditarVenda.as_view(), name='editar_venda'),
    path('vendas/<int:pk>/deletar/', views.DeletarVenda.as_view(), name='deletar_venda'),
    path('vendas/adicionar/<int:pk>/itens/', views.AdicionarItem.as_view(), name='adicionar_item'),
    path('vendas/<int:pk>/deletar/item/<int:item_pk>/', views.DeletarItem.as_view(), name='deletar_item'),
    path('vendas/balanco/', views.VerBalanco.as_view(), name='ver_balanco'),
]
