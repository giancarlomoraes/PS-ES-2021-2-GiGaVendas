from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.exceptions import ImproperlyConfigured
from django.db.models import QuerySet
from django.http import Http404, JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from .models import *
from .filters import *
from .forms import *
from django.contrib import messages


@login_required
def adicionar_cliente(request):
    if request.user.has_perm("global_permissions.can_add_cliente"):
        if request.method == 'POST':

            # Trata os dois formulários, tanto o de usuário comum, como o personalizado de ClientPermissions
            form = UserForm(data=request.POST)
            user_form = ClienteForm(data=request.POST)

            if form.is_valid() and user_form.is_valid():
                user = form.save(commit=False)
                user.is_active = True
                user.save()
                aux = user_form.save(commit=False)
                aux.user = user
                aux.save()
                return redirect('comercio:listar_clientes')
        else:
            form = UserForm()
            user_form = ClienteForm()
        return render(request, 'comercio/clientes/adicionar-cliente.html',
                      {'form': form, 'user_form': user_form})
    else:
        raise PermissionDenied()


# Tela para editar Usuário cadastrado
@login_required
def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    user = cliente.user
    if request.user.has_perm("global_permissions.can_edit_cliente"):
        if request.method == 'POST':
            form = EditUserForm(data=request.POST, instance=user)
            user_form = ClienteForm(data=request.POST, instance=cliente)
            if form.is_valid() and user_form.is_valid():
                user = form.save()
                aux = user_form.save(commit=False)
                aux.user = user
                aux.save()
                return redirect('comercio:listar_clientes')
        else:
            form = EditUserForm(instance=user)
            user_form = ClienteForm(instance=cliente)
        return render(request, 'comercio/clientes/editar-cliente.html',
                      {'form': form, 'user_form': user_form, 'usuario': user})
    else:
        raise PermissionDenied()


# Tela de alteração de Senha do Usuário por parte do Admin
@login_required
def change_cliente_password(request, pk):
    user = get_object_or_404(User, pk=pk)
    if user.cliente_user:
        if request.user.has_perm("can_edit_cliente_password"):
            if request.method == 'POST':
                form = EditClientePasswordForm(data=request.POST, user=user)
                if form.is_valid():
                    form.save()
                    return redirect('comercio:listar_clientes')
            else:
                form = EditClientePasswordForm(user=user)
            return render(request, 'comercio/clientes/change-cliente-password.html',
                          {'form': form, 'usuario': user})
        else:
            raise PermissionDenied()
    else:
        raise Http404


@method_decorator(login_required, name='dispatch')
class ListarClientes(PermissionRequiredMixin, ListView):
    model = Cliente
    permission_required = 'global_permissions.can_see_clientes'
    raise_exception = True
    template_name = 'comercio/clientes/listar-clientes.html'


@method_decorator(login_required, name='dispatch')
class DeletarCliente(PermissionRequiredMixin, DeleteView):
    model = Cliente
    permission_required = 'global_permissions.can_delete_cliente'
    raise_exception = True
    template_name = 'clientes/listar_clientes.html'
    success_url = reverse_lazy('comercio:listar_clientes')


@login_required
def adicionar_colaborador(request):
    if request.user.has_perm("global_permissions.can_add_colaborador"):
        if request.method == 'POST':
            form = UserForm(data=request.POST)
            user_form = ColaboradorForm(data=request.POST)

            if form.is_valid() and user_form.is_valid():
                user = form.save(commit=False)
                user.is_active = True
                user.save()
                aux = user_form.save(commit=False)
                aux.user = user
                aux.save()
                return redirect('comercio:listar_colaboradores')
        else:
            form = UserForm()
            user_form = ColaboradorForm()
        return render(request, 'comercio/colaboradores/adicionar-colaborador.html',
                      {'form': form, 'user_form': user_form})
    else:
        raise PermissionDenied()


# Tela para editar Usuário cadastrado
@login_required
def editar_colaborador(request, pk):
    colaborador = get_object_or_404(Colaborador, pk=pk)
    user = colaborador.user
    if request.user.has_perm("global_permissions.can_edit_colaborador"):
        if request.method == 'POST':
            form = EditUserForm(data=request.POST, instance=user)
            user_form = ColaboradorForm(data=request.POST, instance=colaborador)
            if form.is_valid() and user_form.is_valid():
                user = form.save()
                aux = user_form.save(commit=False)
                aux.user = user
                aux.save()
                return redirect('comercio:listar_colaboradores')
        else:
            form = EditUserForm(instance=user)
            user_form = ColaboradorForm(instance=colaborador)
        return render(request, 'comercio/colaboradores/editar-colaborador.html',
                      {'form': form, 'user_form': user_form, 'usuario': user})
    else:
        raise PermissionDenied()


# Tela de alteração de Senha do Usuário por parte do Admin
@login_required
def change_colaborador_password(request, pk):
    user = get_object_or_404(User, pk=pk)
    if user.colaborador_user:
        if request.user.has_perm("can_edit_colaborador_password"):
            if request.method == 'POST':
                form = EditColaboradorPasswordForm(data=request.POST, user=user)
                if form.is_valid():
                    form.save()
                    return redirect('comercio:listar_colaboradores')
            else:
                form = EditColaboradorPasswordForm(user=user)
            return render(request, 'comercio/colaboradores/change-colaborador-password.html',
                          {'form': form, 'usuario': user})
        else:
            raise PermissionDenied()
    else:
        raise Http404


@method_decorator(login_required, name='dispatch')
class ListarColaboradores(PermissionRequiredMixin, ListView):
    model = Colaborador
    permission_required = 'global_permissions.can_see_colaboradores'
    raise_exception = True
    template_name = 'comercio/colaboradores/listar-colaboradores.html'


@method_decorator(login_required, name='dispatch')
class DeletarColaborador(PermissionRequiredMixin, DeleteView):
    model = Colaborador
    permission_required = 'global_permissions.can_delete_colaborador'
    raise_exception = True
    template_name = 'colaboradores/listar-colaboradores.html'
    success_url = reverse_lazy('comercio:listar_colaboradores')


@method_decorator(login_required, name='dispatch')
class AdicionarProduto(PermissionRequiredMixin, CreateView):
    model = Produto
    form_class = ProdutoForm
    permission_required = 'global_permissions.can_add_produto'
    raise_exception = True
    template_name = 'comercio/produtos/adicionar-produto.html'
    success_url = reverse_lazy('comercio:listar_produtos')


@method_decorator(login_required, name='dispatch')
class ListarProdutos(PermissionRequiredMixin, ListView):
    model = Produto
    permission_required = 'global_permissions.can_see_produtos'
    raise_exception = True
    template_name = 'comercio/produtos/listar-produtos.html'


@method_decorator(login_required, name='dispatch')
class EditarProduto(PermissionRequiredMixin, UpdateView):
    model = Produto
    form_class = ProdutoForm
    permission_required = 'global_permissions.can_edit_produto'
    raise_exception = True
    template_name = 'comercio/produtos/adicionar-produto.html'
    success_url = reverse_lazy('comercio:listar_produtos')


@method_decorator(login_required, name='dispatch')
class DeletarProduto(PermissionRequiredMixin, DeleteView):
    model = Produto
    permission_required = 'global_permissions.can_delete_produto'
    raise_exception = True
    template_name = 'comercio/produtos/listar-produtos.html'
    success_url = reverse_lazy('comercio:listar_produtos')


@method_decorator(login_required, name='dispatch')
class AdicionarVenda(PermissionRequiredMixin, CreateView):
    model = Venda
    form_class = VendaForm
    permission_required = 'global_permissions.can_add_venda'
    raise_exception = True
    template_name = 'comercio/vendas/adicionar-venda.html'

    def form_valid(self, form):
        self.object = form.save()
        self.success_url = reverse_lazy('comercio:adicionar_item', kwargs={'pk': self.object.pk})
        return super().form_valid(form)


def finalizar_venda(request, pk, valor):
    try:
        venda = Venda.objects.get(pk=pk)
        venda.valor = valor
        venda.save()

        for item in venda.itens_venda.all():
            if not item.descontado_estoque:
                item.produto.quantidade -= item.quantidade
                item.produto.save()
                item.descontado_estoque = True
                item.save()
        return redirect('comercio:listar_vendas')
    except Venda.DoesNotExist:
        return Http404


@method_decorator(login_required, name='dispatch')
class ListarVendas(PermissionRequiredMixin, ListView):
    model = Venda
    filterset_class = VendaFilter
    permission_required = 'global_permissions.can_see_vendas'
    raise_exception = True
    template_name = 'comercio/vendas/listar-vendas.html'

    def get_context_data(self, **kwargs):
        context = super(ListarVendas, self).get_context_data(**kwargs)
        context['filter'] = self.filterset
        return context

    def get_queryset(self):
        queryset = super(ListarVendas, self).get_queryset()

        for venda in queryset:
            if not venda.valor and len(venda.itens_venda.all()) == 0:
                venda.delete()
        queryset = Venda.objects.all()

        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs.distinct()


@method_decorator(login_required, name='dispatch')
class EditarVenda(PermissionRequiredMixin, UpdateView):
    model = Venda
    form_class = VendaForm
    permission_required = 'global_permissions.can_edit_venda'
    raise_exception = True
    template_name = 'comercio/vendas/adicionar-venda.html'
    success_url = reverse_lazy('comercio:adicionar_item')

    def get_success_url(self):
        self.success_url = reverse_lazy('comercio:adicionar_item', kwargs={'pk': self.object.pk})
        return self.success_url


@method_decorator(login_required, name='dispatch')
class DeletarVenda(PermissionRequiredMixin, DeleteView):
    model = Venda
    permission_required = 'global_permissions.can_delete_venda'
    raise_exception = True
    template_name = 'comercio/vendas/listar-vendas.html'
    success_url = reverse_lazy('comercio:listar_vendas')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()

        for item in self.object.itens_venda.all():
            item.produto.quantidade += item.quantidade
            item.produto.save()

        self.object.delete()
        return HttpResponseRedirect(success_url)


@method_decorator(login_required, name='dispatch')
class AdicionarItem(PermissionRequiredMixin, CreateView):
    model = Item
    form_class = ItemForm
    permission_required = 'global_permissions.can_add_item'
    raise_exception = True
    template_name = 'comercio/itens/itens.html'

    def get_context_data(self, **kwargs):
        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()

        itens = Item.objects.filter(venda__pk=self.kwargs['pk'])
        kwargs['object_list'] = itens
        kwargs['pk'] = self.kwargs['pk']

        valor = 0
        for item in itens:
            valor += item.produto.preco * item.quantidade
        kwargs['valor'] = valor
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)

        if self.object.produto.quantidade >= self.object.quantidade:
            venda = Venda.objects.get(pk=self.kwargs['pk'])
            self.object.venda = venda
            self.object = form.save()
            self.success_url = reverse_lazy('comercio:adicionar_item', kwargs={'pk': self.object.venda.pk})
            return super().form_valid(form)
        else:
            messages.add_message(self.request, messages.ERROR, 'Quantidade informada excede o disponível no estoque.')
            return self.render_to_response(self.get_context_data(form=form))


@method_decorator(login_required, name='dispatch')
class DeletarItem(PermissionRequiredMixin, DeleteView):
    model = Item
    permission_required = 'global_permissions.can_delete_item'
    raise_exception = True
    template_name = 'comercio/itens/itens.html'

    def get_success_url(self):
        self.success_url = reverse_lazy('comercio:adicionar_item', kwargs={'pk': self.object.venda.pk})
        return self.success_url


@method_decorator(login_required, name='dispatch')
class VerBalanco(PermissionRequiredMixin, ListView):
    model = Venda
    filterset_class = VendaFilter
    permission_required = 'global_permissions.can_see_balanco'
    raise_exception = True
    template_name = 'comercio/balanco/ver-balanco.html'

    def get_context_data(self, **kwargs):
        context = super(VerBalanco, self).get_context_data(**kwargs)
        context['filter'] = self.filterset
        return context

    def get_queryset(self):
        queryset = Venda.objects.none()

        colaborador = self.request.user.colaborador_user.first()
        if colaborador:
            if colaborador.funcao.nome == "Administrador":
                queryset = Venda.objects.all()
            elif colaborador.funcao.nome == "Gestor":
                queryset = Venda.objects.filter(colaborador__funcao__nome="Caixa")
        elif self.request.user.is_superuser:
            queryset = Venda.objects.all()

        for venda in queryset:
            if not venda.valor and len(venda.itens_venda.all()) == 0:
                venda.delete()

        if colaborador:
            if colaborador.funcao.nome == "Administrador":
                queryset = Venda.objects.all()
            elif colaborador.funcao.nome == "Gestor":
                queryset = Venda.objects.filter(colaborador__funcao__nome="Caixa")
        elif self.request.user.is_superuser:
            queryset = Venda.objects.all()

        self.filterset = self.filterset_class(self.request.GET, queryset=queryset, request_user=self.request.user)
        return self.filterset.qs.distinct()
