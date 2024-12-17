from django.db import models
from .produtos import Produtos
from .pratos import Pratos


class ItemPratos(models.Model):
    id = models.BigAutoField(primary_key=True)
    quantidade_por_porcao = models.DecimalField(max_digits=5, decimal_places=2)
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)
    prato = models.ForeignKey(Pratos, on_delete=models.CASCADE)