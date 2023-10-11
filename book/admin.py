from django.contrib import admin
from .models import Book



class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'count')  
    list_filter = ('name', 'authors__name') 
    search_fields = ('name', 'description')  
 

admin.site.register(Book, BookAdmin) 