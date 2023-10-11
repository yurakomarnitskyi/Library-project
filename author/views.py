from django.shortcuts import render, redirect
from author.models import Author
from django.http import HttpResponse

def author_views(request):
    authors = Author.objects.all()
    return render(request, 'author.html', {'authors': authors})
        
def create_author(request):
    if request.method == 'POST':
        name = request.POST['name']
        surname = request.POST['surname']
        patronymic = request.POST['patronymic']

       
        author = Author.objects.create(
            name=name,
            surname=surname,
            patronymic=patronymic,
        )

        return redirect('author_views')  

    return render(request, 'create_author.html')


def remove_unused_authors(request):
    unused_authors = Author.objects.filter(books=None)

    if request.method == 'POST':
        selected_authors = request.POST.getlist('authors_to_remove')
        Author.objects.filter(id__in=selected_authors).delete()
        return redirect('author_views')

    return render(request, 'remove_unused_authors.html', {'unused_authors': unused_authors})