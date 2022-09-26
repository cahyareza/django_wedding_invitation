from django.urls import path

from .views import order_checkout_view

urlpatterns = [
    # path('', cart_detail, name='cart_detail'),
    path('checkout/', order_checkout_view, name='checkout'),
]