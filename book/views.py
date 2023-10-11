from django.shortcuts import render, redirect, get_object_or_404
from book.models import Book
from django.http import Http404
from django.db.models import Q
from authentication.models import CustomUser
from django.contrib import messages

def all_books(request):
    books = Book.objects.all()
    return render(request, 'all_books.html', {'books': books})


def view_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'views_book.html', {'book': book})


def filter_books(request):
    author = request.GET.get('author')
    title = request.GET.get('title')
    
    
    if author or title:
        books = Book.objects.filter(
            Q(authors__name__icontains=author) | Q(name__icontains=title)
        )
    else:
        books = Book.objects.all()
    
    return render(request, 'all_books.html', {'books': books})



def user_books(request, user_id):
    try:
        user = get_object_or_404(CustomUser, id=user_id)
        books = user.books.all()
        return render(request, 'user_books.html', {'user': user, 'books': books})
    except Http404:
        return render(request, 'user_not_found.html')
