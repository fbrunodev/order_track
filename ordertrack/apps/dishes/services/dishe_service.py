from apps.dishes.models import Pratos, ItemPratos, Acompanhamentos
from django.db import transaction , IntegrityError
from collections import defaultdict

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

# Dishes Itens CRUD

def create_item_dishe(validated_data):
    try:
        with transaction.atomic():
            item_prato = ItemPratos.objects.create(**validated_data)
            return item_prato
    except IntegrityError : 
        raise ValueError("Somethin wrong with database")
    except Pratos.DoesNotExist:
        print("There isn't any dishes with that id")


def list_itens():
  
    item_prato = ItemPratos.objects.select_related('prato', 'produto')

    
    dishe_dict = defaultdict(list)

    for item in item_prato:
        dishe_dict[item.prato.nome].append({
            'produto': item.produto.nome,  
            'quantidade_por_porcao': item.quantidade_por_porcao 
        })

    
    dishe_data = []
    for prato, produtos in dishe_dict.items():
        dishe_data.append({
            'prato': prato,  
            'produtos': produtos  
        })

    return dishe_data