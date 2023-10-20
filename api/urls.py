from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('user', views.UserDetailView) 
router.register('author', views.AuthorDetailView) 
router.register('order', views.OrderDetailView)
router.register('book', views.BookDetailView)


urlpatterns = [
    path('', include(router.urls)), 
    path('user/<int:user_id>/order/<int:order_id>/', views.UserOrderDetailView.as_view(), name='user-order-detail')
]


