from django.shortcuts import render, redirect, get_object_or_404
from .models import Laptop

def laptop_list(request):
    laptops = Laptop.objects.all()
    return render(request, 'shop/laptop_list.html', {'laptops': laptops})

def laptop_detail(request, pk):
    laptop = get_object_or_404(Laptop, pk=pk)
    return render(request, 'shop/laptop_detail.html', {'laptop': laptop})

def cart_add(request, pk):
    laptop = get_object_or_404(Laptop, pk=pk)
    cart = request.session.get('cart', {})
    cart[str(pk)] = cart.get(str(pk), 0) + 1
    request.session['cart'] = cart
    return redirect('cart_detail')

def cart_remove(request, pk):
    cart = request.session.get('cart', {})
    if str(pk) in cart:
        del cart[str(pk)]
    request.session['cart'] = cart
    return redirect('cart_detail')

def cart_detail(request):
    cart = request.session.get('cart', {})
    laptops = []
    total_price = 0
    for pk, quantity in cart.items():
        laptop = get_object_or_404(Laptop, pk=pk)
        laptop.quantity = quantity
        laptop.total = laptop.price * quantity
        total_price += laptop.total
        laptops.append(laptop)
    return render(request, 'shop/cart.html', {'cart_items': laptops, 'total_price': total_price})

def home(request):
    return redirect('laptop_list')
