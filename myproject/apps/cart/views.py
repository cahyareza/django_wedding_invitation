from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from ..portofolio.models import Fitur, Payment
from myproject.apps.coupon.models import Coupon
from django.utils import timezone

def add_cart(request, product_id):
    # Cart
    cart = Cart(request)
    product = get_object_or_404(Fitur, id=product_id)
    coupon_obj = Coupon.objects.filter(active=True)
    current_time = timezone.now()

    initial_data = {
        'quantity' : 1,
        'override' : False
    }

    if request.method == "POST":
        # Cart
        if coupon_obj.exists() :
            obj = Coupon.objects.filter(active=True).first()
            if obj.valid_to >= current_time:
                cart.add(product=product, quantity=initial_data['quantity'], coupon=obj.discount, override_quantity=initial_data['override'])
            else:
                cart.add(product=product, quantity=initial_data['quantity'], coupon=0, override_quantity=initial_data['override'])
        else:
            cart.add(product=product, quantity=initial_data['quantity'], coupon=0, override_quantity=initial_data['override'])

        return redirect('cart:cart_detail')

    return render(request, 'index.html')

def remove_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Fitur, id=product_id)
    cart.remove(product=product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    payments = Payment.objects.all()
    context = {
        'cart': cart,
        'payments': payments,
    }
    return render(request, 'cart/cart.html', context)


def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return render(request, 'cart/success.html')


