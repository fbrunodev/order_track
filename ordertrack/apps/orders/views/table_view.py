from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.response import Response
from apps.orders.models import Mesas, Acompanhamentos
from apps.orders.serializers import TableSerializer, SideSerializer

# Views of tables
class TableCreateView(generics.CreateAPIView):
    queryset = Mesas.objects.all()
    serializer_class = TableSerializer
    permission_classes = [IsAuthenticated]
    


class TableListView(generics.ListAPIView):
    queryset = Mesas.objects.all()
    serializer_class = TableSerializer
    permission_classes = [IsAuthenticated]


class TableUpdateView(generics.UpdateAPIView):
    queryset = Mesas.objects.all()
    serializer_class = TableSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        instance = serializer.save()
    
class TableDestroyView(generics.DestroyAPIView):
    queryset = Mesas.objects.all()
    serializer_class = TableSerializer
    permission_classes = [IsAuthenticated]
