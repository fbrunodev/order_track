from apps.orders.models import Pedidos, Mesas
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from apps.orders.serializers import OrderSerializer, ShowOrderSerializer
from apps.orders.services.order_service import create_order,update_order

class OrderCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer_data = OrderSerializer(data = request.data)
        if serializer_data.is_valid():
            pedido = create_order(serializer_data.validated_data,request)

            serializer = OrderSerializer(pedido)

        
            return Response({
                'message': 'Created',
                'order': serializer.data
            })
        return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)
    
class OrderUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def patch(self, request, id):
        
        serializer_data = OrderSerializer(data = request.data)
        if serializer_data.is_valid():
            pedido = update_order(id, serializer_data.validated_data)     
            serializer = OrderSerializer(pedido)       
            return Response({
                'message': 'Created',
                'order': serializer.data
            })
        return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)
    

class OrderListView(generics.ListAPIView):
    queryset = Pedidos.objects.all()
    serializer_class = ShowOrderSerializer
    permission_classes = [IsAuthenticated]

class OrderListDetails(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, id):
        orders = Pedidos.objects.filter(id = id)
        if not orders.exists():
            return Response({'error':'No orders found'},status=status.HTTP_404_NOT_FOUND)
        serializer = ShowOrderSerializer(orders, many=True)
        return Response(serializer.data)