from django.db import models
from .funcionarios import Funcionarios
from .pedidos import Pedidos
from .mesas import Mesas
from .enums import StatusConta


class Contas(models.Model):
    id = models.BigAutoField(primary_key=True)
    valor_total = models.DecimalField(max_digits=5, decimal_places=2)
    data = models.DateField()
    hora_abertura = models.TimeField()
    hora_fechamento = models.TimeField()
    status = models.IntegerField(
        choices=[(status.value, status.name) for status in StatusConta],
        default=StatusConta.ABERTA.value
    )
    pedido = models.OneToOneField(Pedidos, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionarios, on_delete=models.CASCADE)
    mesa = models.ForeignKey(Mesas, on_delete=models.CASCADE)