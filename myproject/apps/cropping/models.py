from django.db import models
from myproject.apps.core.models import CreationModificationDateBase, UrlBase

class Photo(CreationModificationDateBase, UrlBase):
    file = models.ImageField()
    file2 = models.ImageField()
    description = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'photo'
        verbose_name_plural = 'photos'


class Photo2(CreationModificationDateBase, UrlBase):
    file2 = models.ImageField()
    description = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'photo2'
        verbose_name_plural = 'photos2'

