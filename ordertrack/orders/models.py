from django.db import models
from enum import Enum

# Create your models here.
class StatusFuncionario(Enum):
    INATIVO = 0
    ATIVO = 1
class Permissao(Enum): 
    Admin = 0
    Garcom = 1
    Chapeiro = 2
    Montador = 3
class UnidadeMedida(Enum):
    Kilo = 0
    Litro = 1
    Grama = 2
    ML = 3

class StatusProduto(Enum):
    Disponivel = 0
    Indisponivel = 1

class TipoMovimentacaoProduto(Enum):
    Entrada = 0
    Saida = 1


class Funcionarios(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=50),
    cargo = models.CharField(max_length=15),
    data_admissao = models.DateField,
    data_nascimento = models.DateField,
    email = models.CharField(max_length=30),
    status = models.IntegerField(
        choices=[(status.value, status.name) for status in StatusFuncionario],
        default=StatusFuncionario.INATIVO.value
    ),
    senha = models.CharField(max_length=30),
    permissao = models.IntegerField(
        choices=[(permissao.value, permissao.name) for permissao in Permissao],
        default=Permissao.Garcom.value
    )
    salario = models.DecimalField(max_digits=5, decimal_places=2)

class Categorias(models.Model): 
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=20)

class Produtos(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=30),
    categoria_id = models.ForeignKey(Categorias, on_delete=models.CASCADE),
    unidade_medida = models.IntegerField( choices= [(unidade_medida.value, unidade_medida.name) for unidade_medida in UnidadeMedida]),
    quantidade = models.IntegerField,
    data_validade = models.DateField,
    custo_unitario = models.DecimalField(max_digits=5, decimal_places=2),
    status = models.IntegerField(
        choices=[(status.value,status.name) for status in StatusProduto],
        default=StatusProduto.Disponivel.value
    ),
    preco_venda = models.DecimalField(max_digits=5, decimal_places=2)


class MovimentacaoProdutos(models.Model):
    id = models.BigAutoField(primary_key=True)
    tipo = models.IntegerField(
        choices= [(tipo.value,tipo.name) for tipo in TipoMovimentacaoProduto],
    )
    produto_id = models.ForeignKey(Produtos, on_delete=models.CASCADE),
    funcionario_id = models.ForeignKey(Funcionarios, on_delete=models.CASCADE),
    quantidade = models.IntegerField,
    data = models.DateField,
    hora = models.TimeField

class HistoricoCustoProdutos(models.Model): 
    id = models.BigAutoField(primary_key=True)
    produto_id = models.ForeignKey(Produtos, on_delete=models.CASCADE),
    preco_custo = models.DecimalField(max_digits=5, decimal_places=2),
    data = models.DateField

class Pratos(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=30),
    preco_venda = models.DecimalField(max_digits=5, decimal_places=2),
    status = models.IntegerField(
        choices=[(status.value,status.name) for status in StatusProduto],
        default=StatusProduto.Disponivel.value
    )


class ItemPratos(models.Model):
    id = models.BigAutoField(primary_key=True)
    produto_id = models.ForeignKey(Produtos, on_delete=models.CASCADE),
    prato_id = models.ForeignKey(Pratos, on_delete=models.CASCADE),
    quantidade_por_porcao = models.DecimalField(max_digits=5, decimal_places=2),




