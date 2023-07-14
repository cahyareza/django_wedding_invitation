import json
import re
import random
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage
import os
# import cv2
import base64
from django.core import files
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile


from django.http import HttpResponseRedirect
from django.forms import modelformset_factory
from django.core.exceptions import ValidationError
from .serializers import PortofolioSerializer, RekeningSerializer, DompetSerializer, \
    MultiImageSerializer, SpecialInvitationSerializer, PaymentSerializer, QuoteSerializer, \
    UcapanSerializer, HadirSerializer, FiturSerializer, ThemeSerializer, ThemeProductSerializer, \
    StorySerializer, AcaraSerializer, DanaSerializer, ResumeSerializer, MultiImageThemeSerializer, \
    PortoBackgroundSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.utils import timezone
from django.utils.timezone import now
from datetime import datetime
from django.db.models import Q
from myproject.settings import dev, staging, production

from rest_framework import filters, generics, permissions
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet

from django.contrib.auth.decorators import login_required # Login required to access private pages.
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import permission_required
from django.core.cache import cache

from myproject.apps.coupon.models import Coupon
from myproject.apps.order.models import Order, OrderItem
from myproject.apps.portofolio.models import MultiImage, Portofolio, SpecialInvitation, Dompet, Quote, Fitur, \
    Rekening, Payment, MultiImage, SpecialInvitation, Ucapan, Hadir, Fitur, \
    Theme, ThemeProduct, Story, Acara, Kata, Dana, Resume, MultiImageTheme, PortoBackground

# from .forms import PortofolioForm, MultiImageForm, SpecialInvitationForm, \
#     BaseRegisterFormSet, DompetForm, QuoteForm, ThemeProductForm, StoryForm, AcaraForm \

from myproject.apps.portofolio.forms import PortoInfoForm, PasanganForm, AcaraForm, QuoteForm, PortoInfo2Form, \
    MultiImageForm, StoryForm, NavigasiForm, DompetForm, PortoInfo3Form, SpecialInvitationForm, \
    CalenderForm, PortoInfo4Form, ThemeProductForm, PortoInfo5Form, PasanganPictureForm, PortoAlamatDompet, \
    MultiImageThemeForm, BaseRegisterFormSet

from myproject.apps.portofolio.services import AcaraFormSESSION, PasanganFormSESSION, MultiImageFormSESSION, \
    StoryFormSESSION, DompetFormSESSION, SpecialinviteFormSESSION

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.exceptions import PermissionDenied
from django.db.models import F

#################### SERIALIZER #######################
# Portofolio
class PortofolioList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Portofolio.objects.all()
    serializer_class = PortofolioSerializer
    name = 'portofolio-list'
    filterset_fields = (
        'slug',
        )

class PortofolioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Portofolio.objects.all()
    serializer_class = PortofolioSerializer
    name = 'portofolio-detail'


# Rekening
class RekeningList(generics.ListCreateAPIView):
    queryset = Rekening.objects.all()
    serializer_class = RekeningSerializer
    name = 'rekening-list'


class RekeningDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rekening.objects.all()
    serializer_class = RekeningSerializer
    name = 'rekening-detail'

# Multiimage
class MultiImageList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = MultiImage.objects.all()
    serializer_class = MultiImageSerializer
    name = 'multiimage-list'
    filterset_fields = ['portofolio__slug']


class MultiImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MultiImage.objects.all()
    serializer_class = MultiImageSerializer
    name = 'multiimage-detail'

# SpecialInvitation
class SpecialInvitationList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = SpecialInvitation.objects.all()
    serializer_class = SpecialInvitationSerializer
    name = 'specialinvitation-list'
    filterset_fields = ['portofolio__slug']


class SpecialInvitationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SpecialInvitation.objects.all()
    serializer_class = SpecialInvitationSerializer
    name = 'specialinvitation-detail'

# Payment
class PaymentList(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    name = 'payment-list'


class PaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    name = 'payment-detail'

# Dompet
class DompetList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Dompet.objects.all()
    serializer_class = DompetSerializer
    name = 'dompet-list'
    filterset_fields = ['portofolio__slug']


class DompetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dompet.objects.all()
    serializer_class = DompetSerializer
    name = 'dompet-detail'

# Quote
class QuoteList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    name = 'quote-list'
    filterset_fields = ['portofolio__slug']


class QuoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    name = 'quote-detail'

# Ucapan
class UcapanList(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Ucapan.objects.all()
    serializer_class = UcapanSerializer
    name = 'ucapan-list'
    filterset_fields = ['portofolio__slug']

    def post(self, request, *args, **kwargs):
        resume = Resume.objects.filter(nama='resume').first()
        resume.quantity_ucapan=resume.quantity_ucapan + 1
        resume.save()
        return super().post(request, *args, **kwargs)


class UcapanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ucapan.objects.all()
    serializer_class = UcapanSerializer
    name = 'ucapan-detail'

# Hadir
class HadirList(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Hadir.objects.all()
    serializer_class = HadirSerializer
    name = 'hadir-list'
    filterset_fields = ['portofolio__slug']

    def post(self, request, *args, **kwargs):
        resume = Resume.objects.filter(nama='resume').first()
        resume.quantity_tamu=resume.quantity_tamu + 1
        resume.save()
        return super().post(request, *args, **kwargs)


class HadirDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hadir.objects.all()
    serializer_class = HadirSerializer
    name = 'hadir-detail'

# Fitur
class FiturList(generics.ListCreateAPIView):
    queryset = Fitur.objects.all()
    serializer_class = FiturSerializer
    name = 'fitur-list'


class FiturDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fitur.objects.all()
    serializer_class = FiturSerializer
    name = 'fitur-detail'

# Theme
class ThemeList(generics.ListCreateAPIView):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer
    name = 'theme-list'


class ThemeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer
    name = 'theme-detail'


# Theme Product
class ThemeProductList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = ThemeProduct.objects.all()
    serializer_class = ThemeProductSerializer
    name = 'themeproduct-list'
    filterset_fields = ['portofolio__slug']


class ThemeProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ThemeProduct.objects.all()
    serializer_class = ThemeProductSerializer
    name = 'themeproduct-detail'

# Story
class StoryList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    name = 'story-list'
    filterset_fields = ['portofolio__slug']

class StoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    name = 'story-detail'


# Acara
class AcaraList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Acara.objects.all()
    serializer_class = AcaraSerializer
    name = 'acara-list'
    filterset_fields = ['portofolio__slug']


class AcaraDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Acara.objects.all()
    serializer_class = AcaraSerializer
    name = 'acara-detail'

# Dana
class DanaList(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Dana.objects.all()
    serializer_class = DanaSerializer
    name = 'dana-list'
    filterset_fields = ['portofolio__slug']


class DanaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dana.objects.all()
    serializer_class = DanaSerializer
    name = 'dana-detail'

# Resume
class ResumeList(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    name = 'resume-list'
    filterset_fields = ['nama']


class ResumeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    name = 'resume-detail'

# MultiimageTheme
class MultiImageThemeList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = MultiImageTheme.objects.all()
    serializer_class = MultiImageThemeSerializer
    name = 'multiimagetheme-list'
    filterset_fields = ['portofolio__slug']


class MultiImageThemeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MultiImageTheme.objects.all()
    serializer_class = MultiImageThemeSerializer
    name = 'multiimagetheme-detail'


# PortoBackground
class PortoBackgroundList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = PortoBackground.objects.all()
    serializer_class = PortoBackgroundSerializer
    name = 'portobackground-list'
    filterset_fields = ['portofolio__slug']


class PortoBackgroundDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PortoBackground.objects.all()
    serializer_class = PortoBackgroundSerializer
    name = 'portobackground-detail'

# ROOT
class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'portofolios': reverse('api:portofolio:portofolio-list', request=request),
            'rekenings': reverse('api:portofolio:rekening-list', request=request),
            'dompets': reverse('api:portofolio:dompet-list', request=request),
            'multiimages': reverse('api:portofolio:multiimage-list', request=request),
            'specialinvitations': reverse('api:portofolio:specialinvitation-list', request=request),
            'payments': reverse('api:portofolio:payment-list', request=request),
            'quotes': reverse('api:portofolio:quote-list', request=request),
            'ucapans': reverse('api:portofolio:ucapan-list', request=request),
            'hadirs': reverse('api:portofolio:hadir-list', request=request),
            'fiturs': reverse('api:portofolio:fitur-list', request=request),
            'themeproducts': reverse('api:portofolio:themeproduct-list', request=request),
            'themes': reverse('api:portofolio:theme-list', request=request),
            'story': reverse('api:portofolio:story-list', request=request),
            'acara': reverse('api:portofolio:acara-list', request=request),
            'dana': reverse('api:portofolio:dana-list', request=request),
            'resume': reverse('api:portofolio:resume-list', request=request),
            'multiimagetheme': reverse('api:portofolio:multiimagetheme-list', request=request),
            'portobackground': reverse('api:portofolio:portobackground-list', request=request),
            })