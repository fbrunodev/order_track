from django.db import transaction, IntegrityError
from apps.bills.models import Contas
from apps.orders.models import ItemPedidos, ItemAdicionais


def recalcular_valor_total(conta):
    itens = ItemPedidos.objects.filter(pedido = conta.pedido)
    adicionais = ItemAdicionais.objects.filter(item_pedido__pedido = conta.pedido)
    valor_total= sum(item.preco_unitario * item.quantidade for item in itens)
    total_adicionais = sum(add.preco_unitario * add.quantidade for add in adicionais)
    conta.valor_total = valor_total + total_adicionais

    conta.save()


def update_bill (bill_id, validated_data):
    try:
        with transaction.atomic():
            conta = Contas.objects.get(id = bill_id)
            for field, value  in validated_data.items():
                setattr(conta, field, value )
            conta.save()
    except IntegrityError as e:
        raise ValueError ("Something went wrong with database")
    except  Contas.DoesNotExist : 
        print("This bill doesn't exist!!")