from django.shortcuts import render, redirect, get_object_or_404
from decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from django.utils import timezone
from django.contrib import messages

# Create your views here.
from myproject.apps.coupon.models import Coupon
from myproject.apps.coupon.forms import CouponForm


@login_required
def check_coupon(request):
    if request.method == "POST":
        coupon_form = CouponForm(request.POST or None)
        coupon_list = Coupon.objects.all()
        if coupon_form.is_valid():
            current_time = timezone.now()
            code = coupon_form.cleaned_data.get('code')
            coupon_obj = Coupon.objects.filter(code=code, active=True).first()
            if coupon_obj == True:
                if coupon_obj.valid_to >= current_time:
                    messages.warning(request, "Coupon masih aktif !")
                    return redirect('cart:cart_detail')
                else:
                    messages.warning(request, "Coupon tidak aktif !")
                    return redirect('cart:cart_detail')

                context = {
                    "coupon_form": coupon_form,
                }

                return render(request, 'cart/cart.html', context)
            else:
                messages.warning(request, "Kode coupon salah !")

                return redirect('cart:cart_detail')

    else:
        coupon_form = CouponForm(request.POST or None)

    return render(request, 'cart/cart.html', {"coupon_form": coupon_form})
