from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from PIL import Image
from django.core.validators import MinValueValidator, MaxValueValidator

from myproject.apps.portofolio.models import Fitur, Payment, Kabupaten, ThemeProduct, Portofolio
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
    place = models.ForeignKey(Kabupaten, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='menunggu pembayaran')
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(70)], null=True, blank=True, default=0)
    paid = models.FloatField(default=0.00)
    payment = models.ForeignKey(Payment, null=True, on_delete=models.SET_NULL)
    nama_rekening = models.CharField(max_length=100)
    bukti = models.ImageField(blank=True, null=True)
    bukti_upgrade = models.ImageField(blank=True, null=True)
    status_upgrade = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='menunggu pembayaran')
    upgrade_status = models.BooleanField(default=False)
    paid_upgrade = models.FloatField(default=0.00)


    def get_url_path(self):
        return reverse("update", kwargs={
            "order_id": self.id,
        })

    def __str__(self):
        return str(self.user)

    def mark_paid(self):
        if self.bukti != None and self.status != 'terkonfirmasi':
            self.status = 'menunggu konfirmasi'
        return self.status

    def mark_paid_upgrade(self):
        if self.bukti_upgrade != None:
            self.status_upgrade = 'menunggu konfirmasi'
        return self.status_upgrade

    def save(self, *args, **kwargs):

        if str(self.status_upgrade) == "terkonfirmasi":
            orderitem = OrderItem.objects.get(order=self.id)
            orderitem.product = orderitem.product_update
            orderitem.save(update_fields=["product"])

        super().save(*args, **kwargs)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Fitur, related_name='items', null=True, on_delete=models.SET_NULL)
    product_update = models.ForeignKey(Fitur, related_name='products', null=True, blank=True, on_delete=models.SET_NULL)
    price = models.FloatField()
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.order.user)

    def save(self, *args, **kwargs):

        # Mengganti otomatis pada themeproduct sesuai dengan orderitem
        user = self.order.user
        try:
            portofolio = Portofolio.objects.get(user=user)
            themeproduct = ThemeProduct.objects.get(portofolio=portofolio)
            themeproduct.fitur = self.product.name
            themeproduct.save(update_fields=["fitur"])
        except Portofolio.DoesNotExist:
            portofolio = None

        super().save(*args, **kwargs)


