from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AdminPasswordChangeForm
from .models import *


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = '__all__'
        labels = {'cpf': "CPF", 'numero': 'Número'}


class ColaboradorForm(forms.ModelForm):

    class Meta:
        model = Colaborador
        fields = '__all__'
        labels = {'cpf': "CPF", 'numero': 'Número', 'salario': 'Salário', 'funcao': 'Função'}


class VendaForm(forms.ModelForm):

    class Meta:
        model = Venda
        fields = '__all__'
        labels = {'metodo_pagamento': "Método de Pagamento", 'data_hora': "Data e Hora"}


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = '__all__'


class ProdutoForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = '__all__'
        labels = {'preco': "Preço"}


class UserForm(UserCreationForm):

    class Meta:
        model = User

        fields = [
            'first_name',
            'last_name',
            'password1',
            'password2',
            'username',
            'email',
        ]


class EditUserForm(UserChangeForm):

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'email',
        ]


class EditClientePasswordForm(AdminPasswordChangeForm):

    class Meta:
        model = User
        fields = ['password1', 'password2', 'password']


class EditColaboradorPasswordForm(AdminPasswordChangeForm):

    class Meta:
        model = User
        fields = ['password1', 'password2', 'password']
