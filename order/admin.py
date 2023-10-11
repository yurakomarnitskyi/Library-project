from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'created_at', 'end_at', 'plated_end_at')  
    list_filter = ('created_at', 'end_at', 'plated_end_at')  
    search_fields = ('book__name', 'user__email')

admin.site.register(Order, OrderAdmin)