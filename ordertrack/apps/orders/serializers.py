from rest_framework import serializers
from .models import Mesas

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesas
        fields = '__all__'