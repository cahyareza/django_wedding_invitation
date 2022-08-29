from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from myproject.apps.core.models import CreationModificationDateBase, UrlBase

class Portofolio(CreationModificationDateBase, UrlBase):
    name = models.CharField(max_length=250)
    # sementara belum mengunakan app account karena belum dibuat
    user = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = "Portofolio"

class Couple(CreationModificationDateBase, UrlBase):
    portofolio = models.OneToOneField(Portofolio, on_delete=models.CASCADE, blank=True, null=True)
    pname = models.CharField(max_length=40, blank=True, null=True)
    pinsta_link = models.CharField(max_length=250)
    panak_ke = models.IntegerField()
    pnama_ayah = models.CharField(max_length=40)
    pnama_ibu = models.CharField(max_length=40)
    ppicture = models.CharField(max_length=40)
    lname = models.CharField(max_length=40)
    linsta_link = models.CharField(max_length=250)
    lanak_ke = models.IntegerField()
    lnama_ayah = models.CharField(max_length=40)
    lnama_ibu = models.CharField(max_length=40)
    lpicture = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = "Couple"

    class Couple(UrlBase):
        # fields, attributes, properties and methods...
        def get_url_path(self):
            return reverse("register", kwargs={
                "couple_id": str(self.pk),
            })

class Acara(CreationModificationDateBase, UrlBase):
    portofolio = models.OneToOneField(Portofolio, on_delete=models.CASCADE, blank=True, null=True)
    tanggal_akad = models.DateField()
    tanggal_selesai_akad = models.DateField()
    tempat_akad = models.CharField(max_length=250)
    link_gmap_akad = models.CharField(max_length=250)
    tanggal_resepsi = models.DateField()
    tanggal_selesai_resepsi = models.DateField()
    tempat_resepsi = models.CharField(max_length=250)
    link_gmap_resepsi = models.CharField(max_length=250)
    tanggal_unduhmantu = models.DateField()
    tanggal_selesai_unduhmantu = models.DateField()
    tempat_unduhmantu = models.CharField(max_length=250)
    link_gmap_unduhmantu = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = "Acara"

class Ourmoment(CreationModificationDateBase, UrlBase):
    portofolio = models.OneToOneField(Portofolio, on_delete=models.SET_NULL, blank=True, null=True)
    video = models.CharField(max_length=250)
    livestream = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = "Ourmoment"

class SpecialInvitation(CreationModificationDateBase, UrlBase):
    portofolio = models.ForeignKey(Portofolio, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = "SpecialInvitation"

class Ucapan(CreationModificationDateBase, UrlBase):
    portofolio = models.ForeignKey(Portofolio, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=40)
    alamat = models.CharField(max_length=40)
    pesan = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural = "Ucapan"

class Quotes(CreationModificationDateBase, UrlBase):
    portofolio = models.OneToOneField(Portofolio, on_delete=models.CASCADE, blank=True, null=True)
    ayat = models.CharField(max_length=250)
    kutipan = models.TextField()

    class Meta:
        verbose_name_plural = "Quotes"

class AddtoCalender(CreationModificationDateBase, UrlBase):
    WIB = 'Asia/Jakarta'
    WITA = 'Asia/Makassar'
    WIT = 'Asia/Jayapura'

    TIMEZONE_CHOICES = (
        (WIB, 'Asia/Jakarta'),
        (WITA, 'Asia/Makassar'),
        (WIT, 'Asia/Jayapura')
    )

    portofolio = models.OneToOneField(Portofolio, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    startDate = models.DateField()
    location = models.CharField(max_length=250)
    startTime = models.DateField()
    endTime = models.DateField()
    options = models.CharField(max_length=250)
    timeZone = models.CharField(max_length=20, choices=TIMEZONE_CHOICES, default=WIB)
    trigger = models.CharField(max_length=250)
    iCalFileName = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = "AddtoCalender"

class Goto(CreationModificationDateBase, UrlBase):
    portofolio = models.OneToOneField(Portofolio, on_delete=models.CASCADE, blank=True, null=True)
    link_iframe = models.CharField(max_length=250)
    lokasi = models.CharField(max_length=250)
    link_gmap = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = "Goto"

class Hadir(CreationModificationDateBase, UrlBase):
    IYA = 'iya'
    TIDAK = 'tidak'

    STATUS_CHOICES = (
        (IYA, 'iya'),
        (TIDAK, 'tidak')
    )
    portofolio = models.ForeignKey(Portofolio, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=40)
    hadir = models.CharField(max_length=20, choices=STATUS_CHOICES, default=TIDAK)

    class Meta:
        verbose_name_plural = "Hadir"

class Dompet(CreationModificationDateBase, UrlBase):
    portofolio= models.ForeignKey(Portofolio, on_delete=models.SET_NULL, blank=True, null=True)
    nomor = models.IntegerField()
    pemilik = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = "Dompet"

# Tambahan

class PhotoOurmoment(CreationModificationDateBase, UrlBase):
    ourmoment = models.ForeignKey(Ourmoment, on_delete=models.SET_NULL, blank=True, null=True)
    name =  models.CharField(max_length=150)
    photo = models.CharField(max_length=150)

class Rekening(CreationModificationDateBase, UrlBase):
    dompet = models.ForeignKey(Dompet, on_delete=models.SET_NULL, blank=True, null=True)
    bank = models.CharField(max_length=50)
    kode = models.CharField(max_length=20)