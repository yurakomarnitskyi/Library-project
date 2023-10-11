from django.contrib import admin
from .models import Author

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'patronymic')  # Customize the list display fields
    list_filter = ('name', 'surname', 'patronymic')  # Add list filters for author name, surname, and patronymic
    search_fields = ('name', 'surname', 'patronymic')  # Add search fields for author name, surname, and patronymic


admin.site.register(Author, AuthorAdmin)