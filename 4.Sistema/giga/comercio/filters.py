import django_filters

from .models import *


class VendaFilter(django_filters.FilterSet):

    METODO_PAGAMENTO_CHOICES = [
        (1, 'Cartão de Crédito'),
        (2, 'Cartão de Débito'),
        (3, 'Dinheiro'),
        (4, 'Pix'),
    ]

    colaborador = django_filters.ModelMultipleChoiceFilter(queryset=Colaborador.objects.none())
    cliente = django_filters.ModelMultipleChoiceFilter(queryset=Cliente.objects.none())
    metodo_pagamento = django_filters.MultipleChoiceFilter(choices=METODO_PAGAMENTO_CHOICES)
    data_hora = django_filters.DateFilter(method='data_custom')

    def __init__(self, *args, **kwargs):
        request_user = kwargs.get('request_user')
        if 'request_user' in kwargs:
            kwargs.pop('request_user')
        super(VendaFilter, self).__init__(*args, **kwargs)

        self.filters['cliente'].field.queryset = Cliente.objects.all()

        if request_user:
            colaborador = request_user.colaborador_user.first()
            if colaborador:
                if colaborador.funcao.nome == 'Gestor':
                    self.filters['colaborador'].field.queryset = Colaborador.objects.all().filter(funcao__nome='Caixa')
                else:
                    self.filters['colaborador'].field.queryset = Colaborador.objects.all()
            elif request_user.is_superuser:
                self.filters['colaborador'].field.queryset = Colaborador.objects.all()

    class Meta:
        model = Venda
        fields = []

        def data_custom(self, queryset, name, value):
            aux_queryset = Venda.objects.none()
            aux_queryset |= queryset.filter(data_hora__icontains=value)
            return aux_queryset
