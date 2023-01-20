import os
from myproject.apps.portofolio.models import Fitur
from myproject.apps.cart.cart import Cart
from myproject.settings import dev, staging, production

from myproject.apps.portofolio.models import Fitur, Portofolio
from myproject.apps.order.models import Order, OrderItem
from myproject.apps.order.forms import OrderForm
from myproject.apps.coupon.models import Coupon
from django.contrib.auth.decorators import login_required

def portofolio(request):
    if request.user.is_authenticated:
        obj = Portofolio.objects.filter(user=request.user).first()
        if obj:
            porto_slug = obj.slug
            if obj.items.theme:
                theme = obj.items.theme
                return {"portofolio": obj, "porto_slug": porto_slug, "theme": theme}
            else:
                return {"porto_slug": porto_slug, "theme": None}
        else:
            return {"porto_slug": None, "theme": None}
    else:
        return {}

# def listProduct(request):
#     objects_fitur = Fitur.objects.all()
#
#     return {'fiturs': objects_fitur}

def cart(request):
    return {'cart' : Cart(request)}

# def order_checkout_form(request):
#     form = OrderForm(request.POST or None)
#     return {"orderform": form}

# def order_checkout_update(request):
#     if request.user.is_authenticated:
#         obj = Order.objects.filter(user=request.user).first()
#         form2 = OrderForm(instance=obj)
#         return {"orderform2": form2}
#
#     else:
#         return {}

def order(request):
    if request.user.is_authenticated:
        order = Order.objects.filter(user=request.user).first()
        return {'order': order}
        # if order:
            # orderproduct = str(order.items.first().product)
            # return {'order': order, 'orderproduct': orderproduct}
        # else:
            # return {'order' : order, 'orderproduct': None}

    else:
        return {}

def webaddress(request):
    if os.environ["DJANGO_SETTINGS_MODULE"] == "myproject.settings.dev":
        web_address = dev.WEBSITE_URL
        web_address_frontend = dev.WEBSITE_URL_FRONTEND
    elif os.environ["DJANGO_SETTINGS_MODULE"] == "myproject.settings.staging":
        web_address = staging.WEBSITE_URL
        web_address_frontend = staging.WEBSITE_URL_FRONTEND
    else:
        web_address = production.WEBSITE_URL
        web_address_frontend = production.WEBSITE_URL_FRONTEND
    return {'web_address' : web_address, 'web_address_frontend':web_address_frontend}

