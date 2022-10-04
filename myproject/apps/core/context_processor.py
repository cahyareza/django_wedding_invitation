from myproject.apps.portofolio.models import Fitur
from myproject.apps.cart.cart import Cart

from myproject.apps.portofolio.models import Fitur
from myproject.apps.order.models import Order, OrderItem
from myproject.apps.order.forms import OrderForm
from django.contrib.auth.decorators import login_required

def listProduct(request):
    objects_fitur = Fitur.objects.all()

    return {'fiturs': objects_fitur}

def cart(request):
    return {'cart' : Cart(request)}

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
        return {'order' : order}

    else:
        return {}

