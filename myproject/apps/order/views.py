from decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from myproject.apps.portofolio.models import Fitur
from myproject.apps.cart.cart import Cart
from .models import Order, OrderItem
from .forms import OrderForm

# @login_required
# def my_orders_view(request):
#     qs = Order.objects.filter(user=request.user, status='dibayar')
#     return render(request, "orders/my_orders.html", {'object_list': qs})
#
@login_required
def order_checkout_view(request):
    user = request.user # Anonuser
    cart = Cart(request)

    if request.method == "POST":
        print('unvalid')
        form = OrderForm(request.POST or None)
        if form.is_valid():
            print('valid')
            instance = form.save(commit=False)
            instance.user = user
            instance.phone = form.cleaned_data.get("phone")
            instance.place = form.cleaned_data.get("place")
            instance.paid =  cart.get_total_price()
            instance.save()

            order_pk = instance.pk

            # create orderitem
            for item in cart:
                print(item)
                OrderItem.objects.create(order=order_pk, price=item['total_price'], product= ['item.product.name'], quantity=['item.quantity'])

            # clear session
            cart.clear

            return redirect("cart:clear_cart")
    else:
        form = OrderForm(request.POST or None)

    return render(request, 'order/checkout.html', {"form": form} )