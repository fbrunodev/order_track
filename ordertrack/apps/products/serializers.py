from rest_framework  import serializers
from .models import Produtos, MovimentacaoProdutos, HistoricoCustoProdutos
from .services.product_service import create_product, update_product, delete_product


class MovimentacaoProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovimentacaoProdutos
        fields = '__all__'

class HistoricoCustoProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoCustoProdutos
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        fields = '__all__'

    
    
  
