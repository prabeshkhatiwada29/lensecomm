from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.contrib.sessions.models import Session


def product_list(request):
    products = Product.objects.all()
    return render(request, 'cart/product_list.html', {'products': products})


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})
    if product_id in cart:
        cart[product_id]['quantity'] += 1
    else:
        cart[product_id] = {'name': product.name, 'price': str(product.price), 'quantity': 1}
    request.session['cart'] = cart
    return redirect('cart_detail')
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if product_id in cart:
        del cart[product_id]
    request.session['cart'] = cart
    return redirect('cart_detail')



def cart_detail(request):
    cart = request.session.get('cart', {})
    return render(request, 'cart/cart_detail.html', {'cart': cart})
