from rest_framework import viewsets
from authentication.models import CustomUser
from author.models import Author
from book.models import Book
from order.models import Order
from .serializers import CustomUserSerializers, AuthorSerializer, BookSerializer, OrderSerializer

class UserDetailView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializers

class AuthorDetailView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

   
class OrderDetailView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    