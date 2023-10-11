from django.shortcuts import render, redirect, get_object_or_404
from order.models import Order
from book.models import Book
from authentication.models import CustomUser
from django.db.models import Q


def create_order(request):
    if request.method == 'POST':
        user_input = request.POST.get('user')
        book_id = request.POST.get('book')
        plated_end_at = request.POST.get('plated_end_at')

        # Перевірка на валідність даних форми перед створенням ордера
        if user_input and book_id and plated_end_at:
            try:
                book = Book.objects.get(pk=book_id)
                user = CustomUser.objects.get(Q(email=user_input) | Q(id=user_input))
                order = Order(user=user, book=book, plated_end_at=plated_end_at)
                order.save()
                
            except (Book.DoesNotExist, CustomUser.DoesNotExist):
                # Обробка випадку, коли книга або користувач не існує
                pass
    existing_orders = Order.objects.all()
    return render(request, 'create_order.html', {'existing_orders': existing_orders})


def close_order(request, order_id):
    order = Order.get_by_id(order_id)

    if order:
        if request.method == 'POST':
            order.delete()
            return redirect('create_order')

        return render(request, 'close_order_confirm.html', {'order': order})

    # Handle the case where the order does not exist (e.g., show an error page)
    return render(request, 'order_not_found.html')

def custom_404_view(request, exception=None):
    return render(request, '404.html', status=404)