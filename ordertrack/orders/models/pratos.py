from django.db import models
from .enums import StatusProduto 
from.acompanhamentos import Acompanhamentos

class Pratos(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    preco_venda = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.IntegerField(
        choices=[(status.value,status.name) for status in StatusProduto],
        default=StatusProduto.DISPONIVEL.value
    )
    acompanhamento = models.ManyToManyField(Acompanhamentos)
