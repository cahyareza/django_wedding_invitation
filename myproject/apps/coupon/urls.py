from django.urls import path

from .views import check_coupon

urlpatterns = [
    # path('', cart_detail, name='cart_detail'),
    path('check/', check_coupon, name='check'),
]