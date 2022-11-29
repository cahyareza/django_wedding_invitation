import json
import re
from datetime import datetime

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.conf import settings
from multiselectfield import MultiSelectField
from PIL import Image

from django_resized import ResizedImageField

from myproject.apps.core.models import CreationModificationDateBase, UrlBase

TIMEZONE_CHOICES = (
    ('', 'Pilih zona waktu'),
    ('Asia/Jakarta', 'WIB'),
    ('Asia/Makassar', 'WITA'),
    ('Asia/Jayapura', 'WIT')
)

ANAK_KE = (
    ('Pertama', 'Pertama'),
    ('Kedua', 'Kedua'),
    ('Ketiga', 'Ketiga'),
    ('Keempat', 'Keempat'),
    ('Kelima', 'Kelima'),
    ('Keenam', 'Keenam'),
    ('Ketujuh', 'Ketujuh'),
    ('Kedelapan', 'Kedelapan'),
    ('Kesembilan', 'Kesembilan'),
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
    porto_name = models.CharField(max_length=150, unique=True, null=True, blank=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    # Couple
    pname = models.CharField(max_length=40, null=True, blank=True)
    pinsta_link = models.CharField(max_length=250, null=True, blank=True)
    panak_ke = models.CharField(max_length=30, choices=ANAK_KE, null=True, blank=True)
    pnama_ayah = models.CharField(max_length=40, null=True, blank=True)
    pnama_ibu = models.CharField(max_length=40, null=True, blank=True)
    # ppicture = models.ImageField(blank=True)
    ppicture = ResizedImageField(size=[180, 180], crop=['middle', 'center'], upload_to='whatever', null=True, blank=True)

    lname = models.CharField(max_length=40, null=True, blank=True)
    linsta_link = models.CharField(max_length=250, null=True, blank=True)
    lanak_ke = models.CharField(max_length=30, choices=ANAK_KE, null=True, blank=True)
    lnama_ayah = models.CharField(max_length=40, null=True, blank=True)
    lnama_ibu = models.CharField(max_length=40, null=True, blank=True)
    # lpicture = models.ImageField(blank=True)
    lpicture = ResizedImageField(size=[180, 180], crop=['middle', 'center'], upload_to='whatever', null=True, blank=True)

    # Countdown
    tanggal_countdown = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    waktu_countdown = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    location_countdown = models.CharField(max_length=250, null=True, blank=True)
    waktu_countdown_selesai = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    datetime_countdown = models.CharField(max_length=250, null=True, blank=True)

    # Our moment
    video = models.TextField(null=True, blank=True)
    livestream = models.URLField(max_length=1000, null=True, blank=True)

    # Kata2
    kata_special_invite = models.TextField(null=True, blank=True)
    kata_live_streaming = models.TextField(null=True, blank=True)
    kata_moment = models.TextField(null=True, blank=True)


    # Add to calender
    name = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    startDate = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    location = models.CharField(max_length=250, null=True, blank=True)
    startTime = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    endTime = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    options = models.CharField(
        max_length=200, null=True, blank=True
    )
    timeZone = models.CharField(max_length=30, choices=TIMEZONE_CHOICES, default='Asia/Jakarta', null=True, blank=True)
    trigger = models.CharField(max_length=20, null=True, blank=True)
    iCalFileName = models.CharField(max_length=50, null=True, blank=True)

    # Goto
    link_iframe = models.TextField(null=True, blank=True)
    lokasi = models.CharField(max_length=250, null=True, blank=True)
    link_gmap = models.URLField(max_length=1000, null=True, blank=True)

    # Tema
    cover_background = models.ImageField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "APortofolio"

    def __str__(self):
        return self.porto_name

    # ========== CLEAN METHOD ========== !
    # get link from iframe
    def get_link(self, url):
        return re.search('(?P<name>https?://[^\s]+\w)', url).group('name')

    def clean(self):
        if self.link_iframe:
            self.link_iframe = self.get_link(self.link_iframe)
        if self.video:
            self.video = self.get_link(self.video)


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
        if self.tanggal_countdown and self.waktu_countdown:
            self.datetime_countdown = datetime.combine(self.tanggal_countdown,self.waktu_countdown).strftime("%Y-%m-%d %H:%M")
        super().save(*args, **kwargs)

class MultiImage(CreationModificationDateBase, UrlBase):
    portofolio = models.ForeignKey(Portofolio, on_delete=models.CASCADE)
    image = models.FileField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Multiimages"

    def __str__(self):
        return self.portofolio.porto_name

    # def save(self, *args, **kwargs):
    #     if self.portofolio.themeproduct == "platinum":
    #         if sum(self.portofolio) >= 10:
    #             return
    #     if self.portofolio.themeproduct == "gold":
    #         if sum(self.portofolio) >= 20:
    #             return
    #     else:
    #         return
    #
    #     super().save(*args, **kwargs)

class SpecialInvitation(CreationModificationDateBase, UrlBase):
    portofolio = models.ForeignKey(Portofolio, on_delete=models.CASCADE)
    name_invite = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name_invite

class Rekening(CreationModificationDateBase, UrlBase):
    bank = models.CharField(max_length=50, null=True, blank=True)
    kode = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.bank

class Payment(CreationModificationDateBase, UrlBase):
    rekening = models.ForeignKey(Rekening, on_delete=models.SET_NULL, blank=True, null=True)
    number = models.CharField(max_length=20, null=True, blank=True)
    name = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        # return self.rekening.bank
        return f"{self.rekening.kode}({self.number}) a/n {self.name}"

class Dompet(CreationModificationDateBase, UrlBase):
    portofolio = models.ForeignKey(Portofolio, on_delete=models.CASCADE)
    # rekening = models.CharField(max_length=40, choices=DAFTAR_BANK)
    rekening = models.ForeignKey(Rekening, on_delete=models.SET_NULL, blank=True, null=True)
    nomor = models.CharField(max_length=40, null=True, blank=True)
    pemilik = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Dompet"

    def __str__(self):
        return self.portofolio.porto_name

class Quote(CreationModificationDateBase, UrlBase):
    portofolio = models.ForeignKey(Portofolio, on_delete=models.CASCADE)
    ayat = models.CharField(max_length=500, null=True, blank=True)
    kutipan = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.portofolio.porto_name

    class Meta:
        verbose_name_plural = "Quotes"

class Ucapan(CreationModificationDateBase, UrlBase):
    portofolio = models.ForeignKey(Portofolio, on_delete=models.CASCADE)
    nama = models.CharField(max_length=40, null=True, blank=True)
    alamat = models.CharField(max_length=40, null=True, blank=True)
    pesan = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return self.portofolio.porto_name

    class Meta:
        verbose_name_plural = "Ucapan"



class Hadir(CreationModificationDateBase, UrlBase):
    IYA = 'iya'
    TIDAK = 'tidak'

    STATUS_CHOICES = (
        (IYA, 'iya'),
        (TIDAK, 'tidak')
    )
    portofolio = models.ForeignKey(Portofolio, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, null=True, blank=True)
    hadir = models.CharField(max_length=20, choices=STATUS_CHOICES, default=TIDAK, null=True, blank=True)

    def __str__(self):
        return self.portofolio.porto_name

    class Meta:
        verbose_name_plural = "Hadir"

# Fitur (GOLD, SILVER, PLATINUM)
class Fitur(CreationModificationDateBase, UrlBase):
    name = models.CharField(max_length=40, null=True, blank=True)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    price = models.FloatField(null=True, blank=True)
    fitur = MultiSelectField(choices=FITUR_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.name

    # SUPER FUNCTION

    # ========== SAVE FUNCTION ========== !
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

# class FiturProduct(CreationModificationDateBase, UrlBase):
#     fitur = models.ForeignKey(Fitur, on_delete=models.SET_NULL, blank=True, null=True)
#     portofolio = models.OneToOneField(Portofolio, on_delete=models.SET_NULL, blank=True, null=True)

class Theme(CreationModificationDateBase, UrlBase):
    name = models.CharField(max_length=40, null=True, blank=True)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    open_fitur = models.FileField(blank=True, null=True)
    cover_fitur = models.FileField(blank=True, null=True)
    quote_fitur = models.FileField(blank=True, null=True)
    rundown_fitur = models.FileField(blank=True, null=True)
    line = models.FileField(blank=True, null=True)
    space = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.name

    # SUPER FUNCTION

    # ========== SAVE FUNCTION ========== !
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class ThemeProduct(CreationModificationDateBase, UrlBase):
    fitur = models.ForeignKey(Fitur, on_delete=models.CASCADE, blank=True, null=True)
    portofolio = models.OneToOneField(Portofolio,related_name='items', on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.portofolio.porto_name


class Kabupaten(CreationModificationDateBase, UrlBase):
    name = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
        return self.name


class Story(CreationModificationDateBase, UrlBase):
    portofolio = models.ForeignKey(Portofolio, on_delete=models.CASCADE)
    year = models.CharField(max_length=4, null=True, blank=True)
    cerita = models.TextField(null=True, blank=True)
    image = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.portofolio.porto_name

class Acara(CreationModificationDateBase, UrlBase):
    portofolio = models.ForeignKey(Portofolio, on_delete=models.CASCADE)
    nama_acara = models.CharField(max_length=250, null=True, blank=True)
    tanggal_acara = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    waktu_mulai_acara = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    waktu_selesai_acara = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    tempat_acara = models.CharField(max_length=250, null=True, blank=True)
    link_gmap_acara = models.URLField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.portofolio.porto_name
