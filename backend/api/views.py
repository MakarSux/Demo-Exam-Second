from django.shortcuts import render

from rest_framework import viewsets, permissions, generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView 

from .models import Order
from .serializers import UserRegistrationSerializer, OrderSerializer


class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
