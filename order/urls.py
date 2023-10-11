# urls.py
from django.urls import path
from . import views
from order.views import custom_404_view

handler404 = custom_404_view

urlpatterns = [
    path('create_order/', views.create_order, name='create_order'),
    path('close_order/<int:order_id>/', views.close_order, name='close_order'),
]
