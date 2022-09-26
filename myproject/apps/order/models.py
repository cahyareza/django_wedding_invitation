from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from PIL import Image
from myproject.apps.portofolio.models import Fitur, FiturProduct, Payment

from myproject.apps.core.models import CreationModificationDateBase, UrlBase

# Create your models here.
# User = get_user_model()

ORDER_STATUS_CHOICES = (
    ('menunggu pembayaran', 'menunggu pembayaran'),
    ('menunggu konfirmasi', 'menunggu konfirmasi'),
    ('terkonfirmasi', 'terkonfirmasi'),
)


class Order(CreationModificationDateBase, UrlBase):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='menunggu pembayaran')
    paid = models.FloatField(default=0.00)
    payment = models.ForeignKey(Payment, null=True, on_delete=models.SET_NULL)
    nama_rekening = models.CharField(max_length=100)
    bukti = models.ImageField(blank=True, null=True)

    def get_url_path(self):
        return reverse("update", kwargs={
            "order_id": self.id,
        })

    def __str__(self):
        return str(self.user)

    def mark_paid(self):
        if self.bukti != None:
            self.status = 'menunggu konfirmasi'
        return self.status

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Fitur, related_name='items', null=True, on_delete=models.SET_NULL)
    price = models.FloatField()
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.order.user)
