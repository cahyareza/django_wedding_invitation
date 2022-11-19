from myproject.apps.portofolio.models import Fitur
from myproject.apps.cart.cart import Cart

from myproject.apps.portofolio.models import Fitur
from myproject.apps.order.models import Order, OrderItem
from myproject.apps.order.forms import OrderForm
from myproject.apps.coupon.models import Coupon
from django.contrib.auth.decorators import login_required

def listProduct(request):
    objects_fitur = Fitur.objects.all()

    return {'fiturs': objects_fitur}

def cart(request):
    return {'cart' : Cart(request)}

def listCoupon(request):
    objects_coupon = Coupon.objects.all()
    obj_silver = Coupon.objects.filter(active=True, silver=True).first()
    obj_platinum = Coupon.objects.filter(active=True, platinum=True).first()
    obj_gold = Coupon.objects.filter(active=True, gold=True).first()

    return {'coupon_silver': obj_silver,
            'coupon_platinum': obj_platinum,
            'coupon_gold': obj_gold,}

def order_checkout_form(request):
    form = OrderForm(request.POST or None)

    return {"orderform": form}

def order_checkout_update(request):
    if request.user.is_authenticated:
        obj = Order.objects.filter(user=request.user).first()
        form2 = OrderForm(instance=obj)
        return {"orderform2": form2}

    else:
        return {}

def order(request):
    if request.user.is_authenticated:
        order = Order.objects.filter(user=request.user).first()
        if order:
            orderproduct = str(order.items.first().product)
            return {'order': order, 'orderproduct': orderproduct}
        else:
            return {'order' : order, 'orderproduct': None}

    else:
        return {}



