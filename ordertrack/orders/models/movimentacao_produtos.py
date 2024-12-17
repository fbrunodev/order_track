from django.db import models
from .produtos import Produtos
from .funcionarios import Funcionarios
from .enums import TipoMovimentacaoProduto


class MovimentacaoProdutos(models.Model):
    id = models.BigAutoField(primary_key=True)
    tipo = models.IntegerField(
        choices= [(tipo.value,tipo.name) for tipo in TipoMovimentacaoProduto],
    )
    quantidade = models.IntegerField()
    data = models.DateField()
    hora = models.TimeField()
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionarios, on_delete=models.CASCADE)