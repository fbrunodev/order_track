from django.db import transaction, IntegrityError
from apps.orders.models import ItemPedidos, Pedidos, ItemAdicionais
from apps.bills.models import Contas
from apps.bills.services.bill_service import recalcular_valor_total


def create_item_order(order_id,validated_data):
    try:
        with transaction.atomic():
            pedido = Pedidos.objects.get(id = order_id)
            item_order = ItemPedidos.objects.create(
                pedido = pedido,
                prato = validated_data.get('prato'),
                quantidade = validated_data.get('quantidade'),
                preco_unitario = validated_data.get('preco_unitario')
            )
            if 'acompanhamento' in validated_data:
                 item_order.acompanhamento.set(validated_data['acompanhamento'])

            recalcular_valor_total(pedido.conta)
            return item_order
    except IntegrityError as e: 
        raise ValueError('Something went wrong with database')
    

def update_order(item_order_id, validated_data):
    try: 
        with transaction.atomic():
            item_order = ItemPedidos.objects.get(id = item_order_id)
            pedido = item_order.pedido
            for field, value in validated_data.items():
                setattr(item_order,field, value)
            item_order.save()
            recalcular_valor_total(pedido.conta)
            return item_order
    except IntegrityError as e:
        raise ValueError("Something went wrong with database")
    
