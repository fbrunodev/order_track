from django.db import models
from .produtos import Produtos


class HistoricoCustoProdutos(models.Model): 
    id = models.BigAutoField(primary_key=True)
    preco_custo = models.DecimalField(max_digits=5, decimal_places=2)
    data = models.DateField()
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)