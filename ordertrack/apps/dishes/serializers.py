from rest_framework import serializers
from .models import Pratos, ItemPratos,Produtos
from apps.products.serializers import ProductSerializer

class DisheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pratos
        fields = ['categoria', 'nome', 'preco_venda', 'status']

class ItemDisheSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemPratos
        fields = '__all__'


# Serilizers that returns a dictionary where contains all itens of each dishe 
class ItemListSerializer(serializers.Serializer):
    produto = serializers.CharField()
    quantidade_por_porcao = serializers.IntegerField()

class DisheWithItemSerializer(serializers.Serializer):
    prato = serializers.CharField()  
    produtos = ItemListSerializer(many=True) 
