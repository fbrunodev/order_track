from apps.dishes.models import Pratos, ItemPratos
from apps.orders.models import Acompanhamentos
from django.db import transaction , IntegrityError


# Dishes CRUD
def create_dishe(validated_data):
    try:
        with transaction.atomic():
            acompanhamentos = Acompanhamentos.objects.all()
            prato = Pratos.objects.create(**validated_data)
            prato.acompanhamento.set(acompanhamentos)
            return prato
    except Exception as e:
        print('Something goes wrong', e)
    except IntegrityError:
        raise ValueError('Something wrong with database')
    

def update_dishe(dishe_id, validated_data):
    try:
        with transaction.atomic():
            prato = Pratos.objects.get(id = dishe_id)

            for field, value in validated_data.items():
                setattr(prato, field, value)
            
            prato.save()
            return prato  
    except Exception as e:
        print('Something goes wrong', e)
    except IntegrityError:
        raise ValueError('Something wrong with database')

