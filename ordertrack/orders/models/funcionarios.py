from django.db import models
from .enums import StatusFuncionario, Permissao


class Funcionarios(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    cargo = models.CharField(max_length=15)
    data_admissao = models.DateField()
    data_nascimento = models.DateField()
    email = models.CharField(max_length=30)
    status = models.IntegerField(
        choices=[(status.value, status.name) for status in StatusFuncionario],
        default=StatusFuncionario.INATIVO.value
    )
    senha = models.CharField(max_length=30)
    permissao = models.IntegerField(
        choices=[(permissao.value, permissao.name) for permissao in Permissao],
        default=Permissao.GARCOM.value
    )
    salario = models.DecimalField(max_digits=5, decimal_places=2)