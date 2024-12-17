from django.db import models
from .item_pedidos import ItemPedidos
from .adicionais import Adicionais


class ItemAdicionais(models.Model): 
    id = models.BigAutoField(primary_key=True)
    quantidade = models.IntegerField
    preco_unitario = models.DecimalField(max_digits=5, decimal_places=2)
    item_pedido = models.ForeignKey(ItemPedidos, on_delete=models.CASCADE)
    adicional = models.ForeignKey(Adicionais, on_delete=models.CASCADE)