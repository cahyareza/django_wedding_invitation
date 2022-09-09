import json
import re

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from PIL import Image

from myproject.apps.core.models import CreationModificationDateBase, UrlBase

TIMEZONE_CHOICES = (
    ('', 'Pilih zona waktu'),
    ('Asia/Jakarta', 'WIB'),
    ('Asia/Makassar', 'WITA'),
    ('Asia/Jayapura', 'WIT')
)

ANAK_KE = (
    ('1', 'Pertama'),
    ('2', 'Kedua'),
    ('3', 'Ketiga'),
    ('4', 'Keempat'),
    ('5', 'Kelima'),
    ('6', 'Keenam'),
    ('7', 'Ketujuh'),
    ('8', 'Kedelapan'),
    ('9', 'Kesembilan'),
)

class Portofolio(CreationModificationDateBase, UrlBase):
    # Portofolio
    porto_name = models.CharField(max_length=150)

    # Couple
    pname = models.CharField(max_length=40)
    pinsta_link = models.CharField(max_length=250)
    panak_ke = models.CharField(max_length=2, choices=ANAK_KE, default='1')
    pnama_ayah = models.CharField(max_length=40)
    pnama_ibu = models.CharField(max_length=40)
    ppicture = models.ImageField(blank=True)
    lname = models.CharField(max_length=40)
    linsta_link = models.CharField(max_length=250)
    lanak_ke = models.CharField(max_length=2, choices=ANAK_KE, default='1')
    lnama_ayah = models.CharField(max_length=40)
    lnama_ibu = models.CharField(max_length=40)
    lpicture = models.ImageField(blank=True)

    # Acara
    tanggal_akad = models.DateField(auto_now=False, auto_now_add=False)
    waktu_akad = models.TimeField(auto_now=False, auto_now_add=False)
    waktu_selesai_akad = models.TimeField(auto_now=False, auto_now_add=False)
    tempat_akad = models.CharField(max_length=250)
    link_gmap_akad = models.TextField()
    tanggal_resepsi = models.DateField(auto_now=False, auto_now_add=False)
    waktu_resepsi = models.TimeField(auto_now=False, auto_now_add=False)
    waktu_selesai_resepsi = models.TimeField(auto_now=False, auto_now_add=False)
    tempat_resepsi = models.CharField(max_length=250)
    link_gmap_resepsi = models.TextField()
    tanggal_unduhmantu = models.DateField(auto_now=False, auto_now_add=False)
    waktu_unduhmantu = models.TimeField(auto_now=False, auto_now_add=False)
    waktu_selesai_unduhmantu = models.TimeField(auto_now=False, auto_now_add=False)
    tempat_unduhmantu = models.CharField(max_length=250)
    link_gmap_unduhmantu = models.TextField()

    # Our moment
    video = models.CharField(max_length=250)
    livestream = models.CharField(max_length=250)


    # Add to calender
    name = models.CharField(max_length=250)
    description = models.TextField()
    startDate = models.DateField(auto_now=False, auto_now_add=False)
    location = models.CharField(max_length=250)
    startTime = models.TimeField(auto_now=False, auto_now_add=False)
    endTime = models.TimeField(auto_now=False, auto_now_add=False)
    options = models.CharField(
        max_length=200
    )
    timeZone = models.CharField(max_length=30, choices=TIMEZONE_CHOICES)
    trigger = models.CharField(max_length=20)
    iCalFileName = models.CharField(max_length=50)

    # # Goto
    link_iframe = models.TextField()
    lokasi = models.CharField(max_length=250)
    link_gmap = models.TextField()

    class Meta:
        verbose_name_plural = "Portofolio"

    def __str__(self):
        return self.porto_name

    # ========== CLEAN METHOD ========== !
    # get link from iframe
    def get_link(self, url):
        return re.search("(?P<name>https?://[^\s]+)", url).group('name')

    def clean(self):
        self.link_iframe = self.get_link(self.link_iframe)

    # SUPER FUNCTION

    # ========== SAVE FUNCTION ========== !
    def save(self, *args, **kwargs):
        self.options = json.dumps([
          "Google",
          "Apple",
          "iCal",
          "Yahoo",
          "Outlook.com",
          "Microsoft365"
        ])
        self.trigger = "click"
        self.iCalFileName = "Reminder-Event"
        super().save(*args, **kwargs)

class MultiImage(CreationModificationDateBase, UrlBase):
    portofolio = models.ForeignKey(Portofolio, on_delete=models.SET_NULL, blank=True, null=True)
    image = models.FileField(blank=True)

    class Meta:
        verbose_name_plural = "Multiimages"

class SpecialInvitation(CreationModificationDateBase, UrlBase):
    portofolio = models.ForeignKey(Portofolio, on_delete=models.SET_NULL, blank=True, null=True)
    name_invite = models.CharField(max_length=100)

    def __str__(self):
        return self.name_invite

# class Ucapan(CreationModificationDateBase, UrlBase):
#     portofolio = models.ForeignKey(Portofolio, on_delete=models.SET_NULL, blank=True, null=True)
#     name = models.CharField(max_length=40)
#     alamat = models.CharField(max_length=40)
#     pesan = models.CharField(max_length=60)
#
#     class Meta:
#         verbose_name_plural = "Ucapan"
#
# class Quotes(CreationModificationDateBase, UrlBase):
#     portofolio = models.OneToOneField(Portofolio, on_delete=models.CASCADE, blank=True, null=True)
#     ayat = models.CharField(max_length=250)
#     kutipan = models.TextField()
#
#     class Meta:
#         verbose_name_plural = "Quotes"
#
# class Hadir(CreationModificationDateBase, UrlBase):
#     IYA = 'iya'
#     TIDAK = 'tidak'
#
#     STATUS_CHOICES = (
#         (IYA, 'iya'),
#         (TIDAK, 'tidak')
#     )
#     portofolio = models.ForeignKey(Portofolio, on_delete=models.SET_NULL, blank=True, null=True)
#     name = models.CharField(max_length=40)
#     hadir = models.CharField(max_length=20, choices=STATUS_CHOICES, default=TIDAK)
#
#     class Meta:
#         verbose_name_plural = "Hadir"
#
# class Dompet(CreationModificationDateBase, UrlBase):
#     portofolio= models.ForeignKey(Portofolio, on_delete=models.SET_NULL, blank=True, null=True)
#     nomor = models.IntegerField()
#     pemilik = models.CharField(max_length=40)
#
#     class Meta:
#         verbose_name_plural = "Dompet"
#
# class Rekening(CreationModificationDateBase, UrlBase):
#     dompet = models.ForeignKey(Dompet, on_delete=models.SET_NULL, blank=True, null=True)
#     bank = models.CharField(max_length=50)
#     kode = models.CharField(max_length=20)