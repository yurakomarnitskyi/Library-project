from django import forms
from .models import Order  
from django.forms.widgets import DateInput

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order  
        fields = ['book', 'user', 'plated_end_at']  # Вибираємо поля, які будуть включені в форму

        widgets = {
            'book': forms.Select(),  # Використовуємо випадаючий список для поля "book"
            'user': forms.Select(),  # Використовуємо випадаючий список для поля "user"
            'plated_end_at': forms.DateInput(attrs={'type': 'date'})      
        }
 

class DeleteOrderForm(forms.Form):
    order_id = forms.IntegerField(widget=forms.HiddenInput())