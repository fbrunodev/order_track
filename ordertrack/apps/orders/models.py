from django.db import models
from django.conf import settings

from apps.core.enums import StatusMesa, StatusPedido, UnidadeMedida

class Mesas(models.Model):
    id = models.BigAutoField(primary_key=True)
    numero= models.IntegerField()
    status = models.IntegerField(
        choices=[(status.value, status.name) for status in StatusMesa],
        default=StatusMesa.DISPONIVEL.value
    )

class Pedidos(models.Model):
    id = models.BigAutoField(primary_key=True)
    mesa = models.ForeignKey(Mesas, on_delete=models.CASCADE)
    funcionario = models.ForeignKey('employees.CustomUser', on_delete=models.CASCADE)
    status =  models.IntegerField(
        choices=[(status.value, status.name) for status in StatusPedido],
        default=StatusPedido.NA_FILA.value
    )
    data = models.DateField()
    hora_abertura = models.TimeField()
    hora_fechamento = models.TimeField()
    


class Acompanhamentos(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20)


class ItemPedidos(models.Model):
    id = models.BigAutoField(primary_key=True)
    pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE)
    acompanhamento = models.ForeignKey(Acompanhamentos, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=5, decimal_places=2)
    


class Adicionais(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    unidade_medida = models.IntegerField(
        choices=[(unidade_medida.value, unidade_medida.name) for unidade_medida in UnidadeMedida]
    )



class ItemAdicionais(models.Model): 
    id = models.BigAutoField(primary_key=True)
    item_pedido = models.ForeignKey(ItemPedidos, on_delete=models.CASCADE)
    adicional = models.ForeignKey(Adicionais, on_delete=models.CASCADE)
    quantidade = models.IntegerField
    preco_unitario = models.DecimalField(max_digits=5, decimal_places=2)
    









