from django.db import models
from .categorias import Categorias
from .enums import UnidadeMedida, StatusProduto




class Produtos(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    unidade_medida = models.IntegerField( choices= [(unidade_medida.value, unidade_medida.name) for unidade_medida in UnidadeMedida])
    quantidade = models.IntegerField()
    data_validade = models.DateField()
    custo_unitario = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.IntegerField(
        choices=[(status.value,status.name) for status in StatusProduto],
        default=StatusProduto.DISPONIVEL.value
    )
    preco_venda = models.DecimalField(max_digits=5, decimal_places=2)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)