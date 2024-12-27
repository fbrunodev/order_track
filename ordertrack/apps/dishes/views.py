from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from .models import Pratos
from .serializers import DisheSerializer
from .services.dishe_service import create_dishe, update_dishe
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
