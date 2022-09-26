import json
import re

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.conf import settings
from multiselectfield import MultiSelectField
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

DAFTAR_BANK = (
    ('', 'Pilih bank'),
    ('BANK RAKYAT INDONESIA', 'BANK RAKYAT INDONESIA'),
    ('BANK NEGARA INDONESIA', 'BANK NEGARA INDONESIA'),
    ('MANDIRI', 'MANDIRI')
)

FITUR_CHOICES = (('preset standard', 'preset standard'),
    ('quotes', 'quotes'),
    ('detail acara', 'detail acara'),
    ('profil pasangan', 'profil pasangan'),
    ('protokol kesehatan', 'protokol kesehatan'),
    ('navigasi lokasi', 'navigasi lokasi'),
    ('google calender', 'google calender'),
    ('unlimited custom jadwal acara', 'unlimited custom jadwal acara'),
    ('rsvp', 'rsvp'),
    ('amplop digital', 'amplop digital'),
    ('kirim ucapan', 'kirim ucapan'),
    ('gallery(max 10)', 'gallery(max 10)'),
    ('love stories', 'love stories'),
    ('buku tamu', 'buku tamu'),
    ('share eksklusif(max 50)', 'share eksklusif(max 50)'),
    ('background music(list only)', 'background music(list only)'),
    ('custom domain(additional)', 'custom domain(additional)'),
    ('preset platinum', 'preset platinum'),
    ('gallery(max 20)', 'gallery(max 20)'),
    ('live streaming', 'live streaming'),
    ('share eksklusif(unlimited)', 'share eksklusif(unlimited)'),
    ('background music(list dan custom)', 'background music(list dan custom)'),
    ('tersedia versi inggris', 'tersedia versi inggris'),
    ('semua jenis preset', 'semua jenis preset'),
    ('support prioritas', 'support prioritas'),
    ('masa aktif selamanya', 'masa aktif selamanya'),
    ('edit tanpa batas', 'edit tanpa batas'))

THEME_LIST = (
    ('', 'Pilih theme'),
    ('autumn', 'autumn'),
    ('snow', 'snow'),
    ('winter', 'winter')
)

class Portofolio(CreationModificationDateBase, UrlBase):
    # Portofolio
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    porto_name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=255)
    # Couple
    pname = models.CharField(max_length=40)
    pinsta_link = models.CharField(max_length=250)
    panak_ke = models.CharField(max_length=2, choices=ANAK_KE)
    pnama_ayah = models.CharField(max_length=40)
    pnama_ibu = models.CharField(max_length=40)
    ppicture = models.ImageField(blank=True)
    lname = models.CharField(max_length=40)
    linsta_link = models.CharField(max_length=250)
    lanak_ke = models.CharField(max_length=2, choices=ANAK_KE)
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

    # Goto
    link_iframe = models.TextField()
    lokasi = models.CharField(max_length=250)
    link_gmap = models.TextField()

    class Meta:
        verbose_name_plural = "APortofolio"

    def __str__(self):
        return self.porto_name

    # ========== CLEAN METHOD ========== !
    # get link from iframe
    def get_link(self, url):
        return re.search('(?P<name>"https?://[^\s]+)', url).group('name')

    def clean(self):
        if self.link_iframe:
            self.link_iframe = self.get_link(self.link_iframe)

    def get_url_path(self):
        return reverse("update", kwargs={
            "portofolio_slug": self.slug,
        })

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
        self.slug = slugify(self.porto_name)
        super().save(*args, **kwargs)

class MultiImage(CreationModificationDateBase, UrlBase):
    portofolio = models.ForeignKey(Portofolio, on_delete=models.CASCADE, blank=True, null=True)
    image = models.FileField(blank=True)

    class Meta:
        verbose_name_plural = "Multiimages"

class SpecialInvitation(CreationModificationDateBase, UrlBase):
    portofolio = models.ForeignKey(Portofolio, on_delete=models.CASCADE, blank=True, null=True)
    name_invite = models.CharField(max_length=100)

    def __str__(self):
        return self.name_invite

class Rekening(CreationModificationDateBase, UrlBase):
    bank = models.CharField(max_length=50)
    kode = models.CharField(max_length=20)

    def __str__(self):
        return self.bank

class Payment(CreationModificationDateBase, UrlBase):
    rekening = models.ForeignKey(Rekening, on_delete=models.SET_NULL, blank=True, null=True)
    number = models.CharField(max_length=20)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.rekening.bank

class Dompet(CreationModificationDateBase, UrlBase):
    portofolio = models.ForeignKey(Portofolio, on_delete=models.CASCADE, blank=True, null=True)
    # rekening = models.CharField(max_length=40, choices=DAFTAR_BANK)
    rekening = models.ForeignKey(Rekening, on_delete=models.SET_NULL, blank=True, null=True)
    nomor = models.CharField(max_length=40)
    pemilik = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Dompet"

    def __str__(self):
        return self.pemilik

class Quote(CreationModificationDateBase, UrlBase):
    portofolio = models.ForeignKey(Portofolio, on_delete=models.CASCADE, blank=True, null=True)
    ayat = models.CharField(max_length=250)
    kutipan = models.TextField()

    class Meta:
        verbose_name_plural = "Quotes"

class Ucapan(CreationModificationDateBase, UrlBase):
    portofolio = models.ForeignKey(Portofolio, on_delete=models.CASCADE, blank=True, null=True)
    nama = models.CharField(max_length=40)
    alamat = models.CharField(max_length=40)
    pesan = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural = "Ucapan"



class Hadir(CreationModificationDateBase, UrlBase):
    IYA = 'iya'
    TIDAK = 'tidak'

    STATUS_CHOICES = (
        (IYA, 'iya'),
        (TIDAK, 'tidak')
    )
    portofolio = models.ForeignKey(Portofolio, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=40)
    hadir = models.CharField(max_length=20, choices=STATUS_CHOICES, default=TIDAK)

    class Meta:
        verbose_name_plural = "Hadir"


class Fitur(CreationModificationDateBase, UrlBase):
    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=255, blank=True)
    price = models.FloatField()
    fitur = MultiSelectField(choices=FITUR_CHOICES)

    def __str__(self):
        return self.name

    # SUPER FUNCTION

    # ========== SAVE FUNCTION ========== !
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class FiturProduct(CreationModificationDateBase, UrlBase):
    fitur = models.ForeignKey(Fitur, on_delete=models.SET_NULL, blank=True, null=True)
    portofolio = models.OneToOneField(Portofolio, on_delete=models.SET_NULL, blank=True, null=True)

class Theme(CreationModificationDateBase, UrlBase):
    fitur = models.ForeignKey(Fitur, on_delete=models.CASCADE, blank=True, null=True)
    # portofolio = models.OneToOneField(Portofolio, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=40, choices=THEME_LIST, blank=True, null=True)
    slug = models.SlugField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    # SUPER FUNCTION

    # ========== SAVE FUNCTION ========== !
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)