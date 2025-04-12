from django.db import transaction, IntegrityError
from apps.orders.models import ItemAdicionais, ItemPedidos

def create_item_addon(item_order_id, validated_data):
    item_pedido = ItemPedidos.objects.get(id = item_order_id)
    
    item_addon = ItemAdicionais.create(
        item_pedido = item_pedido,
        adicional = validated_data.get('adicional'),
        quantidade = validated_data.get('quantidade'),
        preco_unitario = validated_data.get('preco_unitario')
    )
    