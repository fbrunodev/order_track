from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework import status

from .models import Produtos
from .serializers import ProductSerializer
# Create your views here.

class ProductCreateView(CreateAPIView):
    queryset = Produtos.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    
class ProductListView(ListAPIView):
    queryset = Produtos.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    
class ProductUpdateView(UpdateAPIView):
    queryset = Produtos.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'
 