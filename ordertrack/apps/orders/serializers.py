from rest_framework import serializers
from .models import Mesas, Acompanhamentos, Adicionais

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