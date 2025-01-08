from django.db import models
from apps.products.models import Produtos, Categorias
from apps.core.enums import StatusProduto


# Create your models here.
class Pratos(models.Model):
    id = models.BigAutoField(primary_key=True)
    acompanhamento = models.ManyToManyField('orders.Acompanhamentos')
    categoria = models.ForeignKey(Categorias, on_delete=models.SET_NULL, null= True)
    nome = models.CharField(max_length=30)
    preco_venda = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.IntegerField(
        choices=[(status.value,status.name) for status in StatusProduto],
        default=StatusProduto.DISPONIVEL.value
    )
  


class ItemPratos(models.Model):
    id = models.BigAutoField(primary_key=True)
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)
    prato = models.ForeignKey(Pratos, on_delete=models.CASCADE)
    quantidade_por_porcao = models.DecimalField(max_digits=5, decimal_places=2)
   