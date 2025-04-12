from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Contas, Pagamentos
from .serializers import BillSerializer,  PaymentSerializer
from .services.bill_service import update_bill

# Create your views here.

class ListAllBillView(generics.ListAPIView):
    queryset = Contas.objects.all()
    serializer_class = BillSerializer
    permission_classes = [IsAuthenticated]

class UpdateBillView(APIView):
    permission_classes = [IsAuthenticated]
    def patch(self, request, id):
        serializer = BillSerializer(data = request.data)

        if serializer.is_valid():
            bill = update_bill(id, serializer.validated_data)

            serializer_data = BillSerializer(bill)

            return Response({
                "message" : 'Bill has been updated',
                'Bill' : serializer_data.data
            })
        return Response(serializer.errors, status =status.HTTP_400_BAD_REQUEST)
    
class DestroyBillView(generics.DestroyAPIView):
    queryset = Contas.objects.all()
    serializer_class = BillSerializer
    permission_classes = [IsAuthenticated]