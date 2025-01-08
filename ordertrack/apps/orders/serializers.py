from rest_framework import serializers
from .models import Mesas, Acompanhamentos, Adicionais, Pedidos, ItemPedidos

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesas
        fields = '__all__'


class SideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acompanhamentos
        fields = '__all__'


class AddonsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Adicionais
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    mesa = TableSerializer()
    class Meta: 
        model = Pedidos
        fields = '__all__'


class ItemOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPedidos
        fields = '__all__'


class ShowOrderSerializer(serializers.ModelSerializer):
    
    mesa = TableSerializer() 
    itens = serializers.SerializerMethodField() 

    class Meta:
        model = Pedidos
        fields = ['id', 'mesa', 'itens']

    def get_itens(self, obj):
        itens = ItemPedidos.objects.filter(pedido=obj)
       
        itens_list = []
    
        for item in itens:
            acompanhamento =  item.acompanhamento.all()
            acompanhamento_nomes = [acomp.name for acomp in acompanhamento] 
            itens_list.append({
                'id' : item.id,
                'prato' : item.prato.nome,
                'quantidade' : item.quantidade,
                'preco': item.preco_unitario,
                'acompanhamentos': acompanhamento_nomes
            })
        return itens_list

