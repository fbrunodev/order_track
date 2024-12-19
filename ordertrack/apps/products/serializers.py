from rest_framework  import serializers
from apps.products.models import Produtos


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        fields = '__all__'
        