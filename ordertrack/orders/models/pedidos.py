from django.db import models
from .funcionarios import Funcionarios
from .mesas import Mesas
from .enums import StatusPedido

class Pedidos(models.Model):
    id = models.BigAutoField(primary_key=True)
    status =  models.IntegerField(
        choices=[(status.value, status.name) for status in StatusPedido],
        default=StatusPedido.NA_FILA.value
    )
    data = models.DateField()
    hora_abertura = models.TimeField()
    hora_fechamento = models.TimeField()
    mesa = models.ForeignKey(Mesas, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionarios, on_delete=models.CASCADE)