from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import status

from .models import Produtos
from .serializers import ProductSerializer
from .services.product_service import delete_product,create_product, update_product
# Create your views here.

class ProductCreateView(CreateAPIView):
    queryset = Produtos.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        produto = create_product(serializer.validated_data, self.request)
        return produto

class ProductListView(ListAPIView):
    queryset = Produtos.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    
class ProductUpdateView(UpdateAPIView):
    queryset = Produtos.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def perform_update(self, serializer,*args, **kwargs):
        instance = self.get_object()
        produto = update_product(instance.id, serializer.validated_data, self.request)
        return produto
 
class ProductDestroyView(DestroyAPIView):
    queryset = Produtos.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def perform_destroy(self, request, *args, **kwargs):
       
        instance = self.get_object()
        
        produto = delete_product(instance.id, request)

       
        return Response(
            {"message": "Produto excluído com sucesso"},
            status=200
        )