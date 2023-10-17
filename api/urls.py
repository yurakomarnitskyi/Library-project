from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('v1/user', views.UserDetailView) 
router.register('v1/author', views.AuthorDetailView) 
router.register('v1/book', views.BooksDetailView)
router.register('v1/order', views.OrderDetailView)


urlpatterns = [
    path('', include(router.urls)),
    path('v1/user/<int:user_id>/order/', views.UserOrderListView.as_view(), name='user-order-list'), 
    path('v1/user/<int:user_id>/order/<int:order_id>/', views.UserOrderDetailView.as_view(), name='user-order-detail'),    
]


