from django.urls import path
from . import views


urlpatterns = [
    path('', views.author_views, name= 'author_views'), 
    path('create/', views.create_author, name='create_author'),
    path('delete/', views.remove_unused_authors, name='remove_unused_authors')
]

