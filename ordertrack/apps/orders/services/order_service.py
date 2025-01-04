from datetime import datetime
from apps.orders.models import Mesas
from django.db import transaction, IntegrityError
from apps.orders.models import Pedidos, Mesas
from apps.core.enums import StatusPedido

def create_order(validated_data,request):
    try:
        with transaction.atomic():
            pedido = Pedidos.objects.create(
                mesa = validated_data.get('mesa'),
                funcionario = request.user,
                status = StatusPedido.NA_FILA.value,
                data = datetime.now().date(),
                hora_abertura  = datetime.now().time()
            )
            return pedido
    except IntegrityError as e:
        raise ValueError('Something went wrong with the database',e)
    

def update_order(order_id, validated_data):
    try: 
        with transaction.atomic():
            pedido = Pedidos.objects.get(id = order_id)

            for field, value in validated_data.items():
                setattr(pedido, field, value)
            pedido.save()
            return pedido
    except IntegrityError as e: 
        raise ValueError('Something went wrong with the database', e)
