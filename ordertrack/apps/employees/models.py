from django.db import models
from django.contrib.auth.models import User
from apps.core.enums import StatusFuncionario, Permissao
# Create your models here.
class Funcionarios(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="employee")
    nome = models.CharField(max_length=50)
    cargo = models.CharField(max_length=15)
    data_admissao = models.DateField()
    data_nascimento = models.DateField()
    status = models.IntegerField(
        choices=[(status.value, status.name) for status in StatusFuncionario],
        default=StatusFuncionario.INATIVO.value
    )
    salario = models.DecimalField(max_digits=5, decimal_places=2)