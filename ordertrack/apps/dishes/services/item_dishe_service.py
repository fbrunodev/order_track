from django.db import transaction, IntegrityError
from apps.dishes.models import ItemPratos, Pratos
from collections import defaultdict

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

def update_item_dishe(item_dishe_id, validated_data):
    try:
        with transaction.atomic():
            item_prato = ItemPratos.objects.get(id = item_dishe_id)

            for field, value in validated_data.items():
                setattr(item_prato, field, value)

            item_prato.save()
            return item_prato
    except IntegrityError:
        raise ValueError('Something wrong with the database')
    except ItemPratos.DoesNotExist:
        print("This item doesn't exist")