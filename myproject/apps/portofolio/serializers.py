from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Portofolio, Rekening, Dompet, MultiImage, SpecialInvitation, \
    Payment, Quote, Ucapan, Hadir, Fitur, FiturProduct, Theme

class PortofolioSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset=User.objects.all(),
        slug_field='username')
    class Meta:
        model = Portofolio
        fields = ("user", "porto_name", "slug", "pname", "pinsta_link", "panak_ke",\
                  "pnama_ayah", "pnama_ibu", "ppicture", "lname", "linsta_link", "lanak_ke", \
                  "lnama_ayah", "lnama_ibu", "lpicture", "tanggal_akad", "waktu_akad", "waktu_selesai_akad", \
                  "tempat_akad", "link_gmap_akad", "tanggal_resepsi", "waktu_resepsi", "waktu_selesai_resepsi", "datetime_resepsi",\
                  "tempat_resepsi", "link_gmap_resepsi", "tanggal_unduhmantu", "waktu_unduhmantu", "waktu_selesai_unduhmantu", \
                  "tempat_unduhmantu", "link_gmap_unduhmantu", "video", "livestream", "name", "description", "startDate",
                  "location", "startTime", "endTime", "options", "timeZone", "trigger", "iCalFileName", "link_iframe", \
                  "lokasi", "link_gmap")

# Multiimage
class MultiImageSerializer(serializers.HyperlinkedModelSerializer):
    portofolio = serializers.SlugRelatedField(queryset=Portofolio.objects.all(),
        slug_field='slug')

    class Meta:
        model = MultiImage
        fields = ("portofolio", "image")

# SpecialInvitation
class SpecialInvitationSerializer(serializers.HyperlinkedModelSerializer):
    portofolio = serializers.SlugRelatedField(queryset=Portofolio.objects.all(),
        slug_field='slug')

    class Meta:
        model = SpecialInvitation
        fields = ("portofolio", "name_invite")

class RekeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rekening
        fields = "__all__"

# Payment
class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    rekening = RekeningSerializer()

    class Meta:
        model = Payment
        fields = ("rekening", "number", "name")

# Dompet
class DompetSerializer(serializers.HyperlinkedModelSerializer):
    rekening = RekeningSerializer()
    portofolio = serializers.SlugRelatedField(queryset=Portofolio.objects.all(),
        slug_field='slug')

    class Meta:
        model = Dompet
        fields = ("portofolio", "rekening", "nomor", "pemilik")

# Quote
class QuoteSerializer(serializers.HyperlinkedModelSerializer):
    portofolio = serializers.SlugRelatedField(queryset=Portofolio.objects.all(),
        slug_field='slug')

    class Meta:
        model = Quote
        fields = ("portofolio", "ayat", "kutipan")

# Ucapan
class UcapanSerializer(serializers.HyperlinkedModelSerializer):
    portofolio = serializers.SlugRelatedField(queryset=Portofolio.objects.all(),
        slug_field='slug')

    class Meta:
        model = Ucapan
        fields = ("portofolio", "nama", "alamat", "pesan")

# Hadir
class HadirSerializer(serializers.HyperlinkedModelSerializer):
    portofolio = serializers.SlugRelatedField(queryset=Portofolio.objects.all(),
        slug_field='slug')

    class Meta:
        model = Hadir
        fields = ("portofolio", "name", "hadir")

class FiturSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fitur
        fields = "__all__"

# FiturProduct
class FiturProductSerializer(serializers.HyperlinkedModelSerializer):
    portofolio = serializers.SlugRelatedField(queryset=Portofolio.objects.all(),
        slug_field='slug')
    fitur = FiturSerializer()

    class Meta:
        model = FiturProduct
        fields = ("fitur", "portofolio")


# Theme
class ThemeSerializer(serializers.HyperlinkedModelSerializer):
    fitur = FiturSerializer()

    class Meta:
        model = Theme
        fields = ("fitur", "name", "slug")

