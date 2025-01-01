from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import status
from .models import Produtos, Categorias
from .serializers import ProductSerializer, CategoriaSerializer
from .filters import ProductFilter
from .services.product_service import create_product, update_product, delete_product,create_category, upadate_category, delete_category
# Create your views here.

class ProductCreateView(CreateAPIView):
    queryset = Produtos.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        produto = create_product(serializer.validated_data, self.request)
        return  Response({
            "message": "Product has been creaated",
            "product": produto
        })

class ProductListView(ListAPIView):
    queryset = Produtos.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = ProductFilter
   

class ProductUpdateView(UpdateAPIView):
    queryset = Produtos.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def perform_update(self, serializer,*args, **kwargs):
        instance = self.get_object()
        produto = update_product(instance.id, serializer.validated_data, self.request)
        return Response({
            "message": "Product has been creaated",
            "product": produto
        })
 
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
    
# Views related category
class CategoryCreateView(CreateAPIView):
    queryset = Categorias.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes= [IsAuthenticated]

    def perform_create(self, serializer):
        categoria = create_category(serializer.validated_data)
       
    

class CategoryListView(ListAPIView):
    queryset = Categorias.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated]


class CategoryUpdateView(UpdateAPIView):
    queryset= Categorias.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer, *args, **kwargs):
        instance = self.get_object()
        categoria = upadate_category(instance.id, serializer.validated_data)
        return Response({
            "message": "Category updated",
            "category" : categoria
        })


class CategoryDestroyView(DestroyAPIView):
    queryset = Categorias.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        categoria = delete_category(instance.id)
        return categoria