from datetime import datetime
from django.db import transaction, IntegrityError
from apps.orders.models import Mesas
from apps.bills.models import Contas
from apps.orders.models import Pedidos, Mesas, ItemPedidos
from apps.core.enums import StatusPedido,StatusConta

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

            Contas.objects.create(
                pedido = pedido,
                funcionario = request.user,
                mesa = validated_data.get('mesa'),
                valor_total = 0,
                data = datetime.now().date(),
                hora_abertura = datetime.now().time(),
                status =  StatusConta.ABERTA.value
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


