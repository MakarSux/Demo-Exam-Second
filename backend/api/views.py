from django.shortcuts import render

from django.http import JsonResponse
from django.middleware.csrf import get_token

from rest_framework import viewsets, permissions, generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView 

from .models import Order
from .serializers import UserRegistrationSerializer, OrderSerializer


def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrfToken': csrf_token})


class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
       
        print(serializer.errors)  # Вывод ошибок сериализатора
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
