from django.urls import path

from .views import order_checkout_view, my_orders_list, order_delete, \
    order_checkout_update, status_order

urlpatterns = [
    # path('', cart_detail, name='cart_detail'),
    path('checkout/', order_checkout_view, name='checkout'),
    path('list/', my_orders_list, name='list'),
    path('delete/<int:id>', order_delete, name='delete'),
    path('update/<int:id>', order_checkout_update, name='update'),
    path('status/', status_order, name='status'),
]