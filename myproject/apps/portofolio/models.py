from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from myproject.apps.core.models import CreationModificationDateBase

class Couple (CreationModificationDateBase):
    pname = models.CharField(max_length=40)
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

class Acara(CreationModificationDateBase):
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

class Ourmoment(CreationModificationDateBase):
    video = models.CharField(max_length=250)
    photo = models.CharField(max_length=250)
    livestream = models.CharField(max_length=250)

class SpecialInvitation(CreationModificationDateBase):
    name = models.CharField(max_length=40)

class Ucapan(CreationModificationDateBase):
    name = models.CharField(max_length=40)
    alamat = models.CharField(max_length=40)
    pesan = models.CharField(max_length=60)

class Quotes(CreationModificationDateBase):
    ayat = models.CharField(max_length=250)
    kutipan = models.TextField()

class AddtoCalender(CreationModificationDateBase):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    startDate = models.DateField()
    location = models.CharField(max_length=250)
    startTime = models.DateField()
    endTime = models.DateField()
    options = models.CharField(max_length=250)
    timeZone = models.CharField(max_length=250)
    trigger = models.CharField(max_length=250)
    iCalFileName = models.CharField(max_length=250)

class Goto(CreationModificationDateBase):
    link_iframe = models.CharField(max_length=250)
    lokasi = models.CharField(max_length=250)
    link_gmap = models.CharField(max_length=250)

class Hadir(CreationModificationDateBase):
    name = models.CharField(max_length=40)
    hadir = models.CharField(max_length=40)

class Dompet(CreationModificationDateBase):
    rekening = models.CharField(max_length=40)
    nomor = models.IntegerField()
    pemilik = models.CharField(max_length=40)
