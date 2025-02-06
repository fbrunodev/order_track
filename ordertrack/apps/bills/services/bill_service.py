from apps.orders.models import ItemPedidos


def recalcular_valor_total(conta):
    itens = ItemPedidos.objects.filter(pedido = conta.pedido)

    valor_total = sum(item.preco_unitario * item.quantidade for item in itens)

    conta.valor_total = valor_total

    conta.save()