from rest_framework  import serializers
from .models import Produtos, MovimentacaoProdutos, HistoricoCustoProdutos
from .services.product_service import create_product, update_product


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

    def create(self, validated_data):
        produto = create_product(validated_data, self.context['request'])
        return produto

    def update(self, instance, validated_data):
        produto = update_product(instance.id, validated_data, self.context['request'])
        return produto