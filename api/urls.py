from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('user', views.UserDetailView) 
router.register('author', views.AuthorDetailView) 
router.register('order', views.OrderDetailView)


urlpatterns = [
    path('', include(router.urls)),    
]


