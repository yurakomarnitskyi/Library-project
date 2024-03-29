from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_all_users, name='show_all_users'),  
    path('users/<int:book_id>/', views.views_user, name='views_user'),
    path('authentication/users/<int:user_id>/', views.views_user, name='views_user'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout')
]
   
