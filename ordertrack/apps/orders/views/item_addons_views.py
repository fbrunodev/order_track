from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from apps.orders.models import ItemAdicionais
from apps.orders.serializers import ItemAddonsSerializer

class ItemAddonsCreateView(generics.CreateAPIView):
    queryset = ItemAdicionais.objects.all()
    serializer_class = ItemAddonsSerializer
    permission_classes = [IsAuthenticated]

class ItemAddonsUpdateView(generics.UpdateAPIView):
    queryset = ItemAdicionais.objects.all()
    serializer_class = ItemAddonsSerializer
    permission_classes = [IsAuthenticated]

class ItemAddonsDestroyView(generics.DestroyAPIView):
    queryset = ItemAdicionais.objects.all()
    serializer_class = ItemAddonsSerializer
    permission_classes = [IsAuthenticated]