from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from .models import Pratos, ItemPratos
from .serializers import DisheSerializer, ItemDisheSerializer,DisheWithItemSerializer, ItemListSerializer
from .services.dishe_service import create_dishe, update_dishe
from .services.item_dishe_service import create_item_dishe,update_item_dishe, list_itens
# Create your views here.


class DisheApiView(CreateAPIView):
    queryset  = Pratos.objects.all()
    serializer_class = DisheSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        prato = create_dishe(serializer.validated_data)
        return Response({
            'message' : 'Prato criado'
        })
    

class DisheListView(ListAPIView):
    queryset = Pratos.objects.all()
    serializer_class = DisheSerializer
    permission_classes = [IsAuthenticated]


class DishUpdateView(UpdateAPIView):
    queryset = Pratos.objects.all()
    serializer_class = DisheSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = self.get_object()
        prato = update_dishe(instance.id, serializer.validated_data)
        return Response({
            'message': 'Prado atualizado'
        })
    
class DisheDestroyView(DestroyAPIView):
    queryset = Pratos.objects.all()
    serializer_class = DisheSerializer
    permission_classes = [IsAuthenticated]


# Views of Item Dishes

class ItemDisheCreateView(CreateAPIView):
    queryset = ItemPratos.objects.all()
    serializer_class = ItemDisheSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        item_dishe = create_item_dishe(serializer.validated_data)

class ItemDisheListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        pratos_data = list_itens()  

        serializer = DisheWithItemSerializer(pratos_data, many=True)

        return Response(serializer.data)
    

class ItemDisheUpdateView(UpdateAPIView):
    queryset = ItemPratos.objects.all()
    serializer_class = ItemDisheSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer, *args, **kwargs):
        instance = self.get_object()
        item_prato = update_item_dishe(instance.id, serializer.validated_data)

class ItemDisheDestroyView(DestroyAPIView):
    queryset = ItemPratos.objects.all()
    serializer_class = ItemDisheSerializer
    permission_classes = [IsAuthenticated]