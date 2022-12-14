from django.urls import path

from .views import order_checkout_view, my_orders_list, order_delete, \
    orderitem_update, status_order, upload_bukti

urlpatterns = [
    # path('', cart_detail, name='cart_detail'),
    path('checkout/', order_checkout_view, name='checkout'),
    path('list/', my_orders_list, name='list'),
    path('delete/<int:id>', order_delete, name='delete'),
    path('orderitem_update/<int:id>', orderitem_update, name='orderitem_update'),
    path('status/', status_order, name='status'),
    path('bukti/', upload_bukti, name='bukti'),
]