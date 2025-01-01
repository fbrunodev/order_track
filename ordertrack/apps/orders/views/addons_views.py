from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from apps.orders.models import Adicionais
from apps.orders.serializers import AddonsSerializer

# Views of Additionals

class AddonsCreateView(generics.CreateAPIView):
    queryset = Adicionais.objects.all()
    serializer_class = AddonsSerializer
    permission_classes = [IsAuthenticated]

class AddonsListView(generics.ListAPIView):
    queryset = Adicionais.objects.all()
    serializer_class = AddonsSerializer
    permission_class = [IsAuthenticated]

class AddonsUpdateView(generics.UpdateAPIView):
    queryset = Adicionais.objects.all()
    serializer_class = AddonsSerializer
    permission_classes = [IsAuthenticated]

class AddonsDestroyView(generics.DestroyAPIView):
    queryset = Adicionais.objects.all()
    serializer_class = AddonsSerializer
    permission_classes = [IsAuthenticated]

