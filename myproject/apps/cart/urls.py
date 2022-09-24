from django.urls import path

from .views import add_cart, remove_cart, cart_detail, clear_cart

urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', add_cart, name='add_cart'),
    path('remove/<int:product_id>/', remove_cart, name='remove_cart'),
    path('clear/', clear_cart, name='clear_cart'),
]