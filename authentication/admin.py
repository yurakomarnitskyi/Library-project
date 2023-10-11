from django.contrib import admin
from .models import CustomUser

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'role', 'is_active')  
    list_filter = ('role', 'is_active')  
    search_fields = ('first_name', 'last_name', 'email')  
  
   

admin.site.register(CustomUser, UserAdmin)
