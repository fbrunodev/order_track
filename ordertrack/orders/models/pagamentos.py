from django.db import models
from .contas import Contas
from .enums import MetodoPagamento

class Pagamentos(models.Model):
    id = models.BigAutoField(primary_key=True)
    metodo = models.IntegerField(
       choices=[(metodo.value, metodo.name) for metodo in MetodoPagamento],
       default=MetodoPagamento.DINHEIRO.value
    )
    valor_pago = models.DecimalField(max_digits=5, decimal_places=2)
    conta = models.ForeignKey(Contas, on_delete=models.CASCADE)