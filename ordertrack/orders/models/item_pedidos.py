from django.db import models
from .pedidos import Pedidos
from .acompanhamentos import Acompanhamentos


class ItemPedidos(models.Model):
    id = models.BigAutoField(primary_key=True)
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=5, decimal_places=2)
    pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE)
    acompanhamento = models.ForeignKey(Acompanhamentos, on_delete=models.CASCADE)