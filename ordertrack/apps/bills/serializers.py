from rest_framework import serializers
from .models import Contas, Pagamentos

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contas
        fields = "__all__"

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamentos
        fields = "__all__"