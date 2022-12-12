from django.shortcuts import render, redirect, get_object_or_404
from decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings

# Create your views here.
from myproject.apps.portofolio.models import Fitur
from myproject.apps.cart.cart import Cart
from .models import Order, OrderItem
from .forms import OrderForm

@login_required(login_url="account_login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def my_orders_list(request):
    user = request.user # Anonuser
    order = Order.objects.filter(user=user).first()

    if request.method == "POST":
        form = OrderForm(request.POST or None, request.FILES, instance=order)
        if form.is_valid():
            # print("valid")
            instance = form.save(commit=False)
            instance.user = user
            instance.phone = instance.phone
            instance.place = instance.place
            instance.bukti = form.cleaned_data.get("bukti")
            instance.paid =  instance.paid
            instance.status = order.mark_paid()
            instance.save()

            return redirect("order:bukti")
    else:
        form = OrderForm(instance=order)

    return render(request, "order/my_orders.html", {'order': order, 'form': form})

@login_required(login_url="account_login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def order_checkout_view(request):
    user = request.user # Anonuser
    cart = Cart(request)

    if request.method == "POST":
        order = Order.objects.filter(user=request.user).exists()
        if order == False:
            form = OrderForm(request.POST or None, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = user
                instance.phone = form.cleaned_data.get("phone")
                instance.place = form.cleaned_data.get("place")
                instance.paid =  cart.get_total_price_discount()
                instance.save()

                order_instance = Order.objects.get(pk=instance.pk)
                # create orderitem
                for item in cart:
                    # print(item)
                    fitur_instance = Fitur.objects.get(pk=item['product'].pk)
                    OrderItem.objects.create(order=order_instance, price=item['total_price'], product= fitur_instance, quantity=item['quantity'])
                return redirect("cart:clear_cart")
            else:
                form = OrderForm(request.POST or None, request.FILES)
            return render(request, 'cart/cart.html', {"form": form})
        else:
            # clear session
            del request.session[settings.CART_SESSION_ID]
            request.session.modified = True

            return render(request, 'cart/failed.html')

# @login_required
# def order_checkout_update(request, id):
#     user = request.user # Anonuser
#     obj = Order.objects.filter(id=id).first()
#     # obj = get_object_or_404(Order, id=id)
#     # print(obj)
#
#     # print(request.POST)
#     if request.method == "POST":
#         form2 = OrderForm(request.POST or None, request.FILES, instance=obj)
#         # print(form2)
#         if form2.is_valid():
#             print("valid")
#             instance = form2.save(commit=False)
#             instance.user = user
#             instance.phone = instance.phone
#             instance.place = instance.place
#             instance.bukti = form2.cleaned_data.get("bukti")
#             instance.paid =  instance.paid
#             instance.status = obj.mark_paid()
#             instance.save()
#
#             return redirect("order:bukti")
#     else:
#         form2 = OrderForm(request.POST or None, request.FILES)
#
#     context = {
#         'form2': form2,
#     }
#
#     return redirect("order:list")

@login_required(login_url="account_login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def order_delete(request, id):
    obj = get_object_or_404(Order, id=id)

    obj.delete()

    return render(request, 'order/my_orders.html')

@login_required(login_url="account_login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def status_order(request):
    return render(request, 'order/status_order.html')

@login_required(login_url="account_login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def upload_bukti(request):
    return render(request, 'order/upload_bukti_kirim.html')
