from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import CustomUser
from django.contrib.auth.models import update_last_login
from .serializers import LoginSerializer,UserSerializer

# Create your views here.
class LoginView(APIView):
    
    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)
        if not serializer.is_valid():
            return Response({
                "status": False,
                "data": serializer.errors
            })
        
        username = serializer.data['username']
        password = serializer.data['password']
   
        print(f"Username: {username}")
        print(f"Password: {password}")
        
        user_obj = authenticate(request, username = username, password = password)

        if user_obj is not None: 
            print("User authenticated successfully.")
            update_last_login(None, user_obj)
            token, created = Token.objects.get_or_create(user=user_obj)

            return Response({
                'token': str(token),
                'user': user_obj.data 
            })
        else:
            return Response({'error': 'Invalid credentials'}, status =  400)
        
class UserView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        queryset = CustomUser.objects.all()
        serializer = UserSerializer(queryset, many = True)

        return Response({
                "status" : True,
                "data" : serializer.data
            })
