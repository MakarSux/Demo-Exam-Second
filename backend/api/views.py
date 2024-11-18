from django.shortcuts import render
from django.contrib.auth import authenticate

from rest_framework import viewsets, permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView 

from .models import *
from .serializers import *



class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def perform_create(self, serializer):
        # Получаем пароль из валидированных данных
        password = serializer.validated_data.get('password')
        # Создаем пользователя с хешированным паролем
        user = serializer.save()
        user.set_password(password)
        user.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]


class LoginView(APIView):
    def post(self, request):
        data = request.data
        username = data.get('username', None)
        password = data.get('password', None)

        if username is None or password is None:
            return Response({'error': 'Нужен и логин, и пароль'},
                status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(username=username, password=password)

        if user is None:
            return Response({'error': 'Неверные данные'},
                status=status.HTTP_401_UNAUTHORIZED)
        
        return Response(
            {
                'ok':'ok',
                'username': username,
                'user_id': user.id,
                'admin': user.is_superuser
            },
            status=status.HTTP_200_OK
        )
