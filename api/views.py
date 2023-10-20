from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from authentication.models import CustomUser
from author.models import Author
from book.models import Book
from order.models import Order
from .serializers import CustomUserSerializers, AuthorSerializer, BookSerializer, OrderSerializer

class UserDetailView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializers
    


class UserOrderDetailView(APIView):
    def get(self, request, user_id, order_id):
        user = get_object_or_404(CustomUser, id=user_id)
        order = get_object_or_404(Order, id=order_id)
        user_data = {
            "id": user.id,
            "username": user.first_name,
            "email": user.email
        }
        order_data = {
            "id": order.id,
            "book_id": order.book.id,
            "user_id": order.user.id,
            "created_at": order.created_at.timestamp() if order.created_at else None,
            "end_at": order.end_at.timestamp() if order.end_at else None,
            "plated_end_at": order.plated_end_at.timestamp() if order.plated_end_at else None
        }
        response_data = {"user": user_data, "order": order_data}
        return Response(response_data)


class AuthorDetailView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class OrderDetailView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class BookDetailView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

