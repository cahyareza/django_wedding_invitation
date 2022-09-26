from django.contrib.auth import get_user_model
from django.db import models
from myproject.apps.portofolio.models import Fitur, FiturProduct, Payment

from myproject.apps.core.models import CreationModificationDateBase, UrlBase

# Create your models here.
User = get_user_model()

ORDER_STATUS_CHOICES = (
    ('dibuat', 'dibuat'),
    ('menunggu pembayaran', 'menunggu pembayaran'),
    ('dibayar', 'dibayar'),
    ('menunggu konfirmasi', 'menunggu konfirmasi'),
    ('terkonfirmasi', 'terkonfirmasi'),
)


class Order(CreationModificationDateBase, UrlBase):
    user = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='dibuat')
    paid = models.FloatField(default=0.00)
    payment = models.ForeignKey(Payment, null=True, on_delete=models.SET_NULL)
    nama_rekening = models.CharField(max_length=100)

    def get_url_path(self):
        return reverse("update", kwargs={
            "order_id": self.id,
        })

    def __str__(self):
        return self.user

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Fitur, null=True, on_delete=models.SET_NULL)
    price = models.FloatField()
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.order.user
