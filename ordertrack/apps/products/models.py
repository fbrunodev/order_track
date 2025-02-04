from django.db import models
from django.conf import settings
from apps.core.enums import StatusProduto, TipoMovimentacaoProduto, UnidadeMedida
# Create your models here.
class Categorias(models.Model): 
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=20)


class Produtos(models.Model):
    id = models.BigAutoField(primary_key=True)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
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
    

    

class MovimentacaoProdutos(models.Model):
    id = models.BigAutoField(primary_key=True)
    produto = models.ForeignKey(Produtos, on_delete=models.SET_NULL, null=True)
    funcionario = models.ForeignKey('employees.CustomUser', on_delete=models.CASCADE)
    tipo = models.IntegerField(
        choices= [(tipo.value,tipo.name) for tipo in TipoMovimentacaoProduto],
    )
    quantidade = models.IntegerField()
    data = models.DateField()
    hora = models.TimeField()
    


class HistoricoCustoProdutos(models.Model): 
    id = models.BigAutoField(primary_key=True)
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)
    preco_custo = models.DecimalField(max_digits=5, decimal_places=2)
    data = models.DateField()
    



