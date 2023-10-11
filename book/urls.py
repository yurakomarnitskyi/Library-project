from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_books, name= 'all_books'), 
    path('books/<int:book_id>/', views.view_book, name='view_book'),
    path('filter/', views.filter_books, name='filter_books'),
    path('user/<int:user_id>/books/', views.user_books, name='user_books')

]
