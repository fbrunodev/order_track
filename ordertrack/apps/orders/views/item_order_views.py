from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from apps.orders.models import ItemPedidos
from apps.orders.serializers import ItemOrderSerializer
from apps.orders.services.item_order_service import create_item_order, update_order


class ItemOrderCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request,id):
        serializer= ItemOrderSerializer(data = request.data)
        if serializer.is_valid():
            item_order = create_item_order(id,serializer.validated_data)

            serializer_data  = ItemOrderSerializer(item_order)

            return Response({
                'message' : 'Item has been added',
                'Item Order' : serializer_data.data
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class ItemOrderUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, id):
        serializer = ItemOrderSerializer(data = request.data)
        if serializer.is_valid():
            item_order =  update_order(id, serializer.validated_data)

            serializer_data = ItemOrderSerializer(item_order)
            return Response({
                "message" : 'Item has been updated',
                'Item Order' : serializer_data.data
            })
        return Response(serializer.errors, status =status.HTTP_400_BAD_REQUEST)

class ItemOrderDestroyView(generics.DestroyAPIView):
    queryset = ItemPedidos.objects.all()
    serializer_class = ItemOrderSerializer
    permission_classes = [IsAuthenticated]