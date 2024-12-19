from enum import Enum

# Create your models here.
class StatusFuncionario(Enum):
    INATIVO = 0
    ATIVO = 1


class StatusProduto(Enum):
    DISPONIVEL = 0
    INDISPONIVEL = 1

class StatusPedido(Enum):
    NA_FILA = 0
    PREPARANDO = 1
    PRONTO = 2

class StatusMesa(Enum):
    DISPONIVEL = 0
    INDISPONIVEL = 1 
    RESERVADA = 2
class StatusConta(Enum): 
    ABERTA = 0
    FECHADA = 1

class Permissao(Enum): 
    ADMIN = 0
    GARCOM = 1
    CHAPEIRO = 2
    MONTADOR = 3

class UnidadeMedida(Enum):
    KILO = 0
    LITRO = 1
    GRAMA = 2
    ML = 3


class TipoMovimentacaoProduto(Enum):
    ENTRADA = 0
    SAIDA = 1

class MetodoPagamento(Enum):
    DINHEIRO = 0
    CREDITO = 1
    DEBITO = 2
    PIX  = 3 