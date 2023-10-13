from django.shortcuts import render, redirect
from author.models import Author
from django.http import HttpResponse
from .forms import AuthorForm, RemoveAuthorsForm

def author_views(request):
    authors = Author.objects.all()
    return render(request, 'author.html', {'authors': authors})


def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            patronymic = form.cleaned_data['patronymic']

            # Перевірка, чи автор вже існує
            if Author.objects.filter(name=name, surname=surname, patronymic=patronymic).exists():
                return render(request, 'create_author.html', {'form': form, 'error_message': 'Цей автор вже існує'})
            form.save()
            return redirect('author_views')
    else:
        form = AuthorForm()

    return render(request, 'create_author.html', {'form': form})


def remove_unused_authors(request):
    form = RemoveAuthorsForm()
    if request.method == 'POST':
        form = RemoveAuthorsForm(request.POST)
        if form.is_valid():
            selected_authors = form.cleaned_data['authors_to_remove']
            for author in selected_authors:
                author.delete()
            return redirect('author_views')

    unused_authors = Author.objects.filter(books=None)
    return render(request, 'remove_unused_authors.html', {'form': form, 'unused_authors': unused_authors})