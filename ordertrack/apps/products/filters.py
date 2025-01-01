import django_filters
from .models import Produtos

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Produtos
        fields = {
            'nome': ['iexact','icontains'], 
            'preco_venda': ['exact','lt','gt'], 
            'status':['exact'], 
            'unidade_medida':['exact']}
