import json
import re
import os
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

FITUR_CHOICES = (('desain standard', 'desain standard'),
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
    ('desain platinum', 'desain platinum'),
    ('gallery(max 20)', 'gallery(max 20)'),
    ('live streaming', 'live streaming'),
    ('share eksklusif(unlimited)', 'share eksklusif(unlimited)'),
    ('background music(list dan custom)', 'background music(list dan custom)'),
    ('tersedia versi inggris', 'tersedia versi inggris'),
    ('semua jenis desain', 'semua jenis desain'),
    ('support prioritas', 'support prioritas'),
    ('masa aktif selamanya', 'masa aktif selamanya'),
    ('edit tanpa batas', 'edit tanpa batas'))

THEME_LIST = (
    ('', 'Pilih theme'),
    ('autumn', 'autumn'),
    ('snow', 'snow'),
    ('winter', 'winter')
)

# ========== UPLOAD TO ========== !
def portofolio_picture_upload_to(instance, filename):
    user = instance.porto_name
    return f"portofolio/{user}/picture/{filename}"

def portofolio_pasangan_upload_to(instance, filename):
    user = instance.porto_name
    return f"portofolio/{user}/pasangan/{filename}"

def portofolio_background_upload_to(instance, filename):
    user = instance.user
    return f"portofolio/{user}/background/{filename}"

def portofolio_multiimage_upload_to(instance, filename):
    user = instance.portofolio.user
    return f"portofolio/{user}/multiimage/{filename}"

def portofolio_story_upload_to(instance, filename):
    user = instance.portofolio.user
    return f"portofolio/{user}/story/{filename}"

def theme_upload_to(instance, filename):
    slug = instance.slug
    return f"theme/{slug}/{filename}"
# ========== UPLOAD TO END ========== !

class Track(CreationModificationDateBase, UrlBase):
    name = models.CharField(max_length=50)
    artist = models.CharField(max_length=30)
    url = models.URLField(max_length=500)

    def __str__(self):
        return f'{self.name} ({self.artist})'

class Portofolio(CreationModificationDateBase, UrlBase):
    # Portofolio
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    porto_name = models.CharField(max_length=400, unique=True, null=True, blank=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    porto_picture = models.ImageField(null=True, blank=True, upload_to=portofolio_picture_upload_to, max_length=500)
    # Couple
    pname = models.CharField(max_length=40, null=True, blank=True)
    pinsta_link = models.CharField(max_length=250, null=True, blank=True)
    panak_ke = models.CharField(max_length=30, choices=ANAK_KE, null=True, blank=True)
    pnama_ayah = models.CharField(max_length=40, null=True, blank=True)
    pnama_ibu = models.CharField(max_length=40, null=True, blank=True)
    # ppicture = models.ImageField(blank=True)
    ppicture = ResizedImageField(size=[180, 180], crop=['middle', 'center'], upload_to=portofolio_pasangan_upload_to, null=True, blank=True, max_length=500)

    lname = models.CharField(max_length=40, null=True, blank=True)
    linsta_link = models.CharField(max_length=250, null=True, blank=True)
    lanak_ke = models.CharField(max_length=30, choices=ANAK_KE, null=True, blank=True)
    lnama_ayah = models.CharField(max_length=40, null=True, blank=True)
    lnama_ibu = models.CharField(max_length=40, null=True, blank=True)
    # lpicture = models.ImageField(blank=True)
    lpicture = ResizedImageField(size=[180, 180], crop=['middle', 'center'], upload_to=portofolio_pasangan_upload_to, null=True, blank=True, max_length=500)

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
    description = models.TextField(null=True, blank=True, default="Merupakan undangan pernikahan kami. Besar harapan untuk kehadiran bapak/ibu, dan atas perhatianya diucapkan terimakasih")
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
    cover_background = models.ImageField(blank=True, null=True, upload_to=portofolio_background_upload_to, max_length=500)
    open_background = models.ImageField(blank=True, null=True, upload_to=portofolio_background_upload_to, max_length=500)

    # Track
    track = models.ForeignKey(Track, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural = "APortofolio"
        ordering = ['-created']

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
    image = models.FileField(blank=True, null=True, upload_to=portofolio_multiimage_upload_to, max_length=500)

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
    pembuka = models.CharField(max_length=500, null=True, blank=True)
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
    category = models.CharField(max_length=40, null=True, blank=True)
    pembuat =  models.CharField(max_length=50, null=True, blank=True)
    # tag = models.CharField(max_length=50, null=True, blank=True)
    fitur = models.ForeignKey(Fitur, on_delete=models.CASCADE, blank=True, null=True)
    theme_picture = models.ImageField(blank=True, null=True, upload_to=theme_upload_to)
    preview_url = models.URLField(max_length=1000, null=True, blank=True)

    name = models.CharField(max_length=40, null=True, blank=True)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    open_fitur = models.FileField(blank=True, null=True, upload_to=theme_upload_to)
    cover_fitur = models.FileField(blank=True, null=True, upload_to=theme_upload_to)
    quote_fitur = models.FileField(blank=True, null=True, upload_to=theme_upload_to)
    rundown_fitur = models.FileField(blank=True, null=True, upload_to=theme_upload_to)
    line = models.FileField(blank=True, null=True, upload_to=theme_upload_to)
    space = models.FileField(blank=True, null=True, upload_to=theme_upload_to)
    ornament_1 = models.FileField(blank=True, null=True, upload_to=theme_upload_to)
    ornament_2 = models.FileField(blank=True, null=True, upload_to=theme_upload_to)
    ornament_3 = models.FileField(blank=True, null=True, upload_to=theme_upload_to)
    ornament_4 = models.FileField(blank=True, null=True, upload_to=theme_upload_to)
    background_1 = models.FileField(blank=True, null=True, upload_to=theme_upload_to)
    background_2 = models.FileField(blank=True, null=True, upload_to=theme_upload_to)
    background_3 = models.FileField(blank=True, null=True, upload_to=theme_upload_to)
    background_4 = models.FileField(blank=True, null=True, upload_to=theme_upload_to)
    background_5 = models.FileField(blank=True, null=True, upload_to=theme_upload_to)
    background_open = models.FileField(blank=True, null=True, upload_to=theme_upload_to)
    background_cover = models.FileField(blank=True, null=True, upload_to=theme_upload_to)


    class Meta:
        ordering = ['-created']


    def __str__(self):
        return self.name

    # SUPER FUNCTION

    # ========== SAVE FUNCTION ========== !
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super().save(*args, **kwargs)

class ThemeProduct(CreationModificationDateBase, UrlBase):
    fitur = models.CharField(max_length=40, null=True, blank=True)
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
    image = models.FileField(blank=True, null=True, upload_to=portofolio_story_upload_to, max_length=500)

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

class Kata(CreationModificationDateBase, UrlBase):
    name = models.CharField(max_length=250, null=True, blank=True)
    pembuka = models.TextField(null=True, blank=True)
    isi = models.TextField(null=True, blank=True)
    penutup = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
