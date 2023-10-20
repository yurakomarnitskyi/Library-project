from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from authentication.models import CustomUser
from author.models import Author
from book.models import Book
from order.models import Order
from .serializers import CustomUserSerializers, AuthorSerializer, BookSerializer, OrderSerializer
from rest_framework import generics
from rest_framework import permissions


class UserDetailView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializers


class AuthorDetailView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

   
class OrderDetailView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

class BooksDetailView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class UserOrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_url_kwarg = 'order_id'

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        return Order.objects.filter(user_id=user_id, id=self.kwargs.get('order_id'))


class UserOrderListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        return Order.objects.filter(user_id=user_id)
