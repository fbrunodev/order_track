from django.db import models
from .enums import UnidadeMedida

class Adicionais(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    unidade_medida = models.IntegerField(
        choices=[(unidade_medida.value, unidade_medida.name) for unidade_medida in UnidadeMedida]
    )