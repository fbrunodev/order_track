from rest_framework import serializers
from .models import Pratos


class DisheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pratos
        fields = ['categoria', 'nome', 'preco_venda', 'status']