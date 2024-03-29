from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from ..portofolio.models import Fitur, Payment
from myproject.apps.coupon.models import Coupon
from myproject.apps.order.models import Order
from myproject.apps.order.forms import OrderForm
from django.utils import timezone

def add_cart(request, product_id, coupon_id=None):
    # Cart
    cart = Cart(request)
    product = get_object_or_404(Fitur, id=product_id)
    coupon_obj = Coupon.objects.filter(active=True, id=coupon_id).first()
    current_time = timezone.now()
    order = Order.objects.filter(user=request.user).first()

    # print(coupon_obj)

    initial_data = {
        'quantity' : 1,
        'override' : False
    }

    if request.method == "POST":
        if not order:
            if len(cart) <= 0:
                # Cart
                if coupon_obj :
                    if coupon_obj.valid_to >= current_time:
                        if coupon_obj.silver:
                            cart.add(product=product, quantity=initial_data['quantity'], coupon=coupon_obj.discount,
                                     override_quantity=initial_data['override'])
                        elif coupon_obj.platinum:
                            cart.add(product=product, quantity=initial_data['quantity'], coupon=coupon_obj.discount,
                                     override_quantity=initial_data['override'])
                        elif coupon_obj.gold:
                            cart.add(product=product, quantity=initial_data['quantity'], coupon=coupon_obj.discount,
                                     override_quantity=initial_data['override'])
                        else:
                            cart.add(product=product, quantity=initial_data['quantity'], coupon=coupon_obj.discount,
                                     override_quantity=initial_data['override'])
                        # cart.add(product=product, quantity=initial_data['quantity'], coupon=obj.discount, override_quantity=initial_data['override'])
                    else:
                        cart.add(product=product, quantity=initial_data['quantity'], coupon=0, override_quantity=initial_data['override'])
                else:
                    cart.add(product=product, quantity=initial_data['quantity'], coupon=0, override_quantity=initial_data['override'])

                return redirect('cart:cart_detail')
            else:
                return render(request, 'cart/add_cart_failed.html')
        else:
            return render(request, 'cart/failed.html')

    return render(request, 'index.html')

def remove_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Fitur, id=product_id)
    cart.remove(product=product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    payments = Payment.objects.all()
    form = OrderForm(request.POST or None)
    context = {
        'cart': cart,
        'payments': payments,
        'form': form
    }
    return render(request, 'cart/cart.html', context)


def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return render(request, 'cart/success.html')



