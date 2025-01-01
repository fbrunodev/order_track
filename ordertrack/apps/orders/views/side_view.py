from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.response import Response
from apps.orders.models import Acompanhamentos
from apps.orders.serializers import  SideSerializer





# Views of Sides

class SideCreateView(generics.CreateAPIView):
    queryset = Acompanhamentos.objects.all()
    serializer_class = SideSerializer
    permission_classes = [IsAuthenticated]

class SideListView(generics.ListAPIView):
    queryset = Acompanhamentos.objects.all()
    serializer_class = SideSerializer
    permission_classes = [IsAuthenticated]

class SideUpdateView(generics.UpdateAPIView):
    queryset = Acompanhamentos.objects.all()
    serializer_class = SideSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        instance = serializer.save()
        

class SideDestroyView(generics.DestroyAPIView):
    queryset = Acompanhamentos.objects.all()
    serializer_class = SideSerializer
    permission_classes = [IsAuthenticated]