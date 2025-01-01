import django_filters
from .models import Pratos


class DisheFilter(django_filters.FilterSet):
    class Meta:
        model = Pratos
        fields = {
            'nome' : ['iexact', 'icontains'],
            'categoria__nome' : ['iexact', 'icontains'],
            'preco_venda' : ['exact', 'lt', 'gt'],
            'status' : ['exact']
        }