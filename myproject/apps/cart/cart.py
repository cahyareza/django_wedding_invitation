from django.conf import settings
from decimal import Decimal
from myproject.apps.portofolio.models import Fitur

class Cart():
    '''
    Akan membuat session dengan keys cart dan salah satu valuenya product_id
    "cart" ={
    "product_id": {
        'price': $9.99,
        'quantity': 1,
        'id': nike
        }
    }

    Kemudian pada session ini bisa menambahkan di session cart menggunakan prinsip2 dictionary data type
    '''

    def __init__(self, request):
        self.session = request.session
        # initialize session cart
        cart = self.session.get(settings.CART_SESSION_ID)

        # jika tidak bukan cart
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart


    def add(self, product, quantity=1, override_quantity=False):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'price': str(product.price), 'quantity': 0}

        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            # edit logic from += to =
            self.cart[product_id]['quantity'] = quantity

        self.save()
        print(self.cart)

    def save(self):
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()

        products = Fitur.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price']*item['quantity']

            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']* item['quantity']) for item in self.cart.values())

    def get_total_quantity(self):
        return sum(item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True






