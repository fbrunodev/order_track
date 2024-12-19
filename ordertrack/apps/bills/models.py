from django.db import models
from apps.orders.models import Pedidos
from apps.employees.models import Funcionarios
from apps.orders.models import Mesas
from apps.core.enums import StatusConta, MetodoPagamento
# Create your models here.


class Contas(models.Model):
    id = models.BigAutoField(primary_key=True)
    pedido = models.OneToOneField(Pedidos, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionarios, on_delete=models.CASCADE)
    mesa = models.ForeignKey(Mesas, on_delete=models.CASCADE)
    valor_total = models.DecimalField(max_digits=5, decimal_places=2)
    data = models.DateField()
    hora_abertura = models.TimeField()
    hora_fechamento = models.TimeField()
    status = models.IntegerField(
        choices=[(status.value, status.name) for status in StatusConta],
        default=StatusConta.ABERTA.value
    )
    

    

class Pagamentos(models.Model):
    id = models.BigAutoField(primary_key=True)
    conta = models.ForeignKey(Contas, on_delete=models.CASCADE)
    metodo = models.IntegerField(
       choices=[(metodo.value, metodo.name) for metodo in MetodoPagamento],
       default=MetodoPagamento.DINHEIRO.value
    )
    valor_pago = models.DecimalField(max_digits=5, decimal_places=2)
    