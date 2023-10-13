from django.shortcuts import render, redirect, get_object_or_404
from order.models import Order
from book.models import Book
from authentication.models import CustomUser
from django.db.models import Q
from . forms import OrderForm, DeleteOrderForm


def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('create_order')  
    else:
        form = OrderForm()
    
    existing_orders = Order.objects.all()
    return render(request, 'create_order.html', {'form': form, 'existing_orders': existing_orders})



def close_order(request, order_id):
    if request.method == 'POST':
        form = DeleteOrderForm(request.POST)
        if form.is_valid():
            order_id = form.cleaned_data['order_id']
            try:
                order = Order.objects.get(id=order_id)
                order.delete()
                return redirect('create_order')
            except Order.DoesNotExist:
                return render(request, 'order_not_found.html')
            
            


def custom_404_view(request, exception=None):
    return render(request, '404.html', status=404)