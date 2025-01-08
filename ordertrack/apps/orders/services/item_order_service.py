from django.db import transaction, IntegrityError
from apps.orders.models import ItemPedidos, Pedidos




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
            return item_order
    except IntegrityError as e: 
        raise ValueError('Something went wrong with database')