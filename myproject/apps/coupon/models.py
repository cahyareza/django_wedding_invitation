from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from myproject.apps.portofolio.models import Fitur

# Create your models here.
class Coupon(models.Model):
    code = models.CharField(max_length=15, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(70)])
    active = models.BooleanField(default=False)
    silver = models.BooleanField(default=False)
    platinum = models.BooleanField(default=False)
    gold = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Coupon Code"

    def __str__(self):
        return self.code