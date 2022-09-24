from myproject.apps.portofolio.models import Fitur
from myproject.apps.cart.cart import Cart
from myproject.apps.cart.forms import CartAddProductForm

def listProduct(request):
    objects_fitur = Fitur.objects.all()

    return {'fiturs': objects_fitur}

def cartaddform(request):
    form = CartAddProductForm(request.POST)
    print(form)
    return {'cartaddform': form }


def cart(request):
    return {'cart' : Cart(request)}

