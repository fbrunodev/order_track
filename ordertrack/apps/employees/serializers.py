from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Funcionarios



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionarios
        fields = ['id', 'user', 'nome', 'cargo', 'status', 'salario']

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()