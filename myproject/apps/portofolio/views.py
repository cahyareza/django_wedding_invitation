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
    StorySerializer, AcaraSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.utils import timezone
from django.utils.timezone import now
from datetime import datetime
from django.db.models import Q
from myproject.settings import dev, staging, production

from rest_framework import filters
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet

from django.contrib.auth.decorators import login_required # Login required to access private pages.
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import permission_required

from myproject.apps.coupon.models import Coupon
from myproject.apps.order.models import Order, OrderItem
from .models import MultiImage, Portofolio, SpecialInvitation, Dompet, Quote, Fitur, \
    Rekening, Payment, MultiImage, SpecialInvitation, Ucapan, Hadir, Fitur, \
    Theme, ThemeProduct, Story, Acara, Kata

# from .forms import PortofolioForm, MultiImageForm, SpecialInvitationForm, \
#     BaseRegisterFormSet, DompetForm, QuoteForm, ThemeProductForm, StoryForm, AcaraForm \

from .forms import PortoInfoForm, PasanganForm, AcaraForm, QuoteForm, PortoInfo2Form, \
    MultiImageForm, StoryForm, NavigasiForm, DompetForm, PortoInfo3Form, SpecialInvitationForm, \
    CalenderForm, PortoInfo4Form, ThemeProductForm, PortoInfo5Form, PasanganPictureForm, BaseRegisterFormSet

from myproject.apps.portofolio.services import AcaraFormSESSION, PasanganFormSESSION, MultiImageFormSESSION, \
    StoryFormSESSION, DompetFormSESSION, SpecialinviteFormSESSION

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.core.exceptions import PermissionDenied

TEMP_PROFILE_IMAGE_NAME = "temp_profile_image.png"

# ============== HOME ===============!
def home(request):
    porto_count = Portofolio.objects.count()
    ucapan_count = Ucapan.objects.count()
    dompet_count = Dompet.objects.count()
    hadir_count = Hadir.objects.count()
    objects_fitur = Fitur.objects.all()
    theme = Theme.objects.all()
    portofolio  = random.sample(list(Portofolio.objects.exclude(porto_picture='')), 5)

    obj_silver = Coupon.objects.filter(active=True, silver=True).first()
    obj_platinum = Coupon.objects.filter(active=True, platinum=True).first()
    obj_gold = Coupon.objects.filter(active=True, gold=True).first()

    current_time = timezone.now()

    # Check if instance available
    if obj_silver or obj_platinum or obj_gold:

        context = {
            'porto_count': porto_count,
            'ucapan_count': ucapan_count,
            'dompet_count': dompet_count,
            'hadir_count': hadir_count,
            'obj_silver': obj_silver,
            'obj_platinum': obj_platinum,
            'obj_gold': obj_gold,
            'fiturs': objects_fitur,
            'discount_str_silver': False,
            'discount_value_silver': False,
            'discount_percent_silver': False,
            'discount_str_platinum': False,
            'discount_value_platinum': False,
            'discount_percent_platinum': False,
            'discount_str_gold': False,
            'discount_value_gold': False,
            'discount_percent_gold': False,
            'themes': theme,
            'portofolios': portofolio,
        }

        # SILVER
        if obj_silver.valid_to >= current_time:
            discount_value_silver = obj_silver.discount
            discount_percent_silver = 1 - discount_value_silver/100
            discount_str_silver = f"{obj_silver.discount}%"

            context['discount_str_silver'] =  discount_str_silver
            context['discount_value_silver'] = discount_value_silver
            context['discount_percent_silver'] = discount_percent_silver

        # PLATINUM
        if obj_platinum.valid_to >= current_time:
            discount_value_platinum = obj_platinum.discount
            discount_percent_platinum = 1 - discount_value_platinum/100
            discount_str_platinum = f"{obj_platinum.discount}%"

            context['discount_str_platinum'] = discount_str_platinum
            context['discount_value_platinum'] = discount_value_platinum
            context['discount_percent_platinum'] = discount_percent_platinum

        # GOLD
        if obj_gold.valid_to >= current_time:
            discount_value_gold = obj_gold.discount
            discount_percent_gold = 1 - discount_value_gold/100
            discount_str_gold = f"{obj_gold.discount}%"

            context['discount_str_gold'] = discount_str_gold
            context['discount_value_gold'] = discount_value_gold
            context['discount_percent_gold'] = discount_percent_gold

        return render(request, 'index.html', context)

    #  Instance not available
    else:
        context = {
            'porto_count': porto_count,
            'ucapan_count': ucapan_count,
            'dompet_count': dompet_count,
            'hadir_count': hadir_count,
            'obj_silver': obj_silver,
            'obj_platinum': obj_platinum,
            'obj_gold': obj_gold,
            'fiturs': objects_fitur,
            'discount_str_silver': False,
            'discount_value_silver': False,
            'discount_percent_silver': False,
            'discount_str_platinum': False,
            'discount_value_platinum': False,
            'discount_percent_platinum': False,
            'discount_str_gold': False,
            'discount_value_gold': False,
            'discount_percent_gold': False,
            'themes': theme,
            'portofolios': portofolio,
        }

        return render(request, 'index.html', context)
# ============== HOME END ===============!


# ============== FITURLIST ===============!
def fitur_list(request):
    return render(request, 'portofolio/fitur_list.html')
# ============== FITURLIST ===============!


# ============== THEMELIST ===============!
def theme_list(request):
    themes = Theme.objects.all()
    context = {
        'themes': themes,
    }
    return render(request, 'portofolio/theme_list.html', context)
# ============== THEMELIST ===============!

# ============== THEMEDETAIL ===============!
def theme_detail(request, id):
    theme = Theme.objects.get(id=id)
    theme_products = ThemeProduct.objects.filter(theme=theme)
    if theme.fitur:
        theme_name = str(theme.fitur.name)
    else:
        theme_name = None

    paginator = Paginator(theme_products, 10)  # 3 posts in each page
    page = request.GET.get('page', 1)
    try:
        theme_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        theme_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        theme_list = paginator.page(paginator.num_pages)

    context = {
        'theme': theme,
        'theme_products': theme_products,
        'theme_name': theme_name,
        'theme_list': theme_list,
    }
    return render(request, 'portofolio/theme_detail.html', context)
# ============== THEMEDETAIL ===============!

# ============== PORTOLIST ===============!
def porto_list(request):
    portos = Portofolio.objects.exclude(porto_picture='')
    paginator = Paginator(portos, 10)  # 3 posts in each page
    page = request.GET.get('page', 1)
    try:
        porto_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        porto_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        porto_list = paginator.page(paginator.num_pages)

    context = {
        'porto_list': porto_list,
    }
    return render(request, 'portofolio/porto_list.html', context)
# ============== PORTOLIST ===============!

# ============== MYPORTOFOLIO ===============!
@login_required(login_url="account_login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def myportofolio(request):
    user = request.user
    portofolios = Portofolio.objects.filter(user=user)
    context = {
        'portofolios': portofolios,
        'today': now().date()
    }
    return render(request, 'portofolio/myportofolio.html', context)
# ============== MYPORTOFOLIO ===============!


# ============== CONFIGURASI ===============!
@login_required(login_url="account_login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def configurasi_porto(request):
    user = request.user
    portofolio = Portofolio.objects.filter(user=user).first()
    if portofolio != None:
        orderproduct = str(Order.objects.filter(user=request.user).first().items.first().product)
        context = {
            'portofolio': portofolio,
            'orderproduct': orderproduct,
        }
        return render(request, 'portofolio/configurasi/icon_config.html', context)
    else:
        return render(request, 'portofolio/parts/porto_notfound.html')
# ============== CONFIGURASI END ===============!



@login_required(login_url="account_login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def step1(request):
    user = request.user
    portofolio = Portofolio.objects.filter(user=user).exists()
    if portofolio == False:
        if request.method == 'POST':
            form = PortoInfoForm(request.POST or None)
            if form.is_valid():
                # create session
                request.session['porto_name'] = form.cleaned_data.get('porto_name')
                if form.cleaned_data.get('description') == "":
                    request.session['description'] = "Merupakan undangan pernikahan kami. Besar harapan untuk kehadiran bapak/ibu, dan atas perhatianya diucapkan terimakasih"
                else:
                    request.session['description'] = form.cleaned_data.get('description')
                print(request.session.get('description', None))
                request.session.modified = True

                return redirect("portofolio:step2")
        else:
            form = PortoInfoForm()
        return render(request, "portofolio/configurasi/register_awal_form.html", {'form': form})
    else:
        return render(request, 'portofolio/regis_failed.html')

@login_required(login_url="account_login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def step1_update(request, slug):
    # get instance portofolio from id
    obj = get_object_or_404(Portofolio, slug=slug)

    # verify user
    if obj.user != request.user:
        raise PermissionDenied

    if request.method == "POST":
        form = PortoInfoForm(request.POST or None, request.FILES, instance=obj)
        if form.is_valid():
            # create portofolio instance
            instance = form.save(commit=False)
            instance.save()
            return redirect("portofolio:configurasi")

    else:
        form = PortoInfoForm(instance=obj)

    context = {
        'form': form,
    }
    return render(request, 'portofolio/configurasi/register_awal_form.html', context)

@login_required(login_url="account_login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def step2(request):
    if request.method == 'POST':
        pasanganform = PasanganFormSESSION(request)
        form = PasanganForm(request.POST or None, request.FILES)
        if form.is_valid():
            pasanganform.add(1,form)
            return redirect("portofolio:step3")
    else:
        form = PasanganForm()
    return render(request, "portofolio/configurasi/pasangan_form.html", {'form': form})

@login_required(login_url="account_login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def step2_update(request, slug):
    # get instance portofolio from id
    obj = get_object_or_404(Portofolio, slug=slug)

    # verify user
    if obj.user != request.user:
        raise PermissionDenied

    if request.method == "POST":
        form = PasanganForm(request.POST or None, request.FILES, instance=obj)

        if form.is_valid():
            # create portofolio instance
            instance = form.save(commit=False)
            instance.save()
            return redirect("portofolio:configurasi")

    else:
        form = PasanganForm(instance=obj)

    context = {
        'form': form,
    }
    return render(request, 'portofolio/configurasi/pasangan_form.html', context)

@login_required(login_url="account_login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def step3(request):
    AcaraFormSet = modelformset_factory(
        Acara,
        form=AcaraForm,
        formset=BaseRegisterFormSet,
        extra=1,
    )
    if request.method == 'POST':
        acaraform = AcaraFormSESSION(request)
        formset6 = AcaraFormSet(request.POST or None, request.FILES, prefix='acara')
        if formset6.is_valid():
            for count,form in enumerate(formset6):
                # Not save blank field use has_changed()
                if form.is_valid() and form.has_changed():
                    acaraform.add(id=count, form=form)
            return redirect("portofolio:step4")
    else:
        formset6 = AcaraFormSet(prefix='acara')

    return render(request, "portofolio/configurasi/acara_form.html", {'formset6': formset6})

@login_required(login_url="account_login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def step3_update(request, slug):
    # get instance portofolio from id
    obj = get_object_or_404(Portofolio, slug=slug)

    # verify user
    if obj.user != request.user:
        raise PermissionDenied

    # Create formset factory, tidak menggunakan base formset agar menampilkan object instance
    AcaraFormSet = modelformset_factory(
        Acara,
        form=AcaraForm,
        extra=0,
        can_delete=True,
        can_delete_extra=True
    )

    qs5 = Acara.objects.filter(portofolio=obj)

    # Define formset
    formset6 = AcaraFormSet(request.POST or None, request.FILES, queryset=qs5, prefix='acara')

    if request.method == "POST":
        if formset6.is_valid():
            # to create multiple image instance
            porto_instance = Portofolio.objects.filter(user=request.user).first()

            for form in formset6:
                # Not save blank field use has_changed()
                if form.is_valid() and form.has_changed():
                    child = form.save(commit=False)
                    child.portofolio = porto_instance
                    child.save()
            # Save deleted obj
            instances = formset6.save(commit=False)
            for obj in formset6.deleted_objects:
                obj.delete()

            return redirect("portofolio:configurasi")

    else:
        formset6 = AcaraFormSet(queryset=qs5, prefix='acara')


    context = {
        'formset6': formset6
    }

    # return redirect("portofolio:update_tampilan", slug=slug)
    return render(request, 'portofolio/configurasi/acara_form.html', context)

@login_required(login_url="account_login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def step4(request):
    user = request.user
    # get instance order
    order = get_object_or_404(Order, user=user)
    # orderitem instance by order
    orderitem = get_object_or_404(OrderItem, order= order)
    orderitem_product_str = str(orderitem.product)

    if request.method == 'POST':
        form2 = QuoteForm(request.POST or None, request.FILES)
        if form2.is_valid():
            # ============== QUOTE ===============!
            request.session['pembuka'] = form2.cleaned_data.get('pembuka')
            request.session['ayat'] = form2.cleaned_data.get('ayat')
            request.session['kutipan'] = form2.cleaned_data.get('kutipan')
            request.session.modified = True

            if orderitem_product_str == "PLATINUM" or orderitem_product_str == "GOLD":
                return redirect("portofolio:step5")
            else:
                return redirect("portofolio:step7")
    else:
        form2 = QuoteForm()

    return render(request, "portofolio/configurasi/quote_form.html", {'form2': form2})

@login_required(login_url="account_login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def step4_update(request, slug):
    # get instance portofolio from id
    obj = get_object_or_404(Portofolio, slug=slug)
    # quote instance by porto id
    obj_quote = get_object_or_404(Quote, portofolio= obj)

    # verify user
    if obj.user != request.user:
        raise PermissionDenied

    if request.method == "POST":
        form2 = QuoteForm(request.POST or None, request.FILES, instance=obj_quote)

        if form2.is_valid():
            # to create multiple image instance
            porto_instance = Portofolio.objects.filter(user=request.user).first()

            # to create instance quote
            instance_quote = form2.save(commit=False)
            instance_quote.portofolio = porto_instance
            instance_quote.save()

            return redirect("portofolio:configurasi")

    else:
        form2 = QuoteForm(instance=obj_quote)

    context = {
        'form2': form2,
    }

    # return redirect("portofolio:update_tampilan", slug=slug)
    return render(request, 'portofolio/configurasi/quote_form.html', context)

@login_required(login_url="account_login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def step5(request):
    orderproduct = str(Order.objects.filter(user=request.user).first().items.first().product)

    MultiImageFormSet = modelformset_factory(
        MultiImage,
        form=MultiImageForm,
        formset=BaseRegisterFormSet,
        extra=1,
    )
    MultiImageFormSet2 = modelformset_factory(
        MultiImage,
        form=MultiImageForm,
        formset=BaseRegisterFormSet,
        extra=1,
    )
    multiimageform = MultiImageFormSESSION(request)
    if request.method == 'POST':
        form2 = PortoInfo2Form(request.POST or None, request.FILES)
        formset3 = MultiImageFormSet(request.POST or None, request.FILES, prefix='multiimage')
        formset5 = MultiImageFormSet2(request.POST or None, request.FILES, prefix='multiimage2')
        if form2.is_valid() and (formset3.is_valid() or formset5.is_valid()):

            if formset5:
                for count,form in enumerate(formset5):
                    # Not save blank field use has_changed()
                    if form.is_valid() and form.has_changed():
                        multiimageform.add(id=count, form=form)
            else:
                for count,form in enumerate(formset3):
                    # Not save blank field use has_changed()
                    if form.is_valid() and form.has_changed():
                        multiimageform.add(id=count, form=form)

            # ============== PORTOINFO2 ===============!
            request.session['video'] = form2.cleaned_data.get('video')
            request.session['livestream'] = form2.cleaned_data.get('livestream')
            request.session['kata_live_streaming'] = form2.cleaned_data.get('kata_live_streaming')
            request.session['kata_moment'] = form2.cleaned_data.get('kata_moment')
            request.session.modified = True

            return redirect("portofolio:step6")
    else:
        form2 = PortoInfo2Form()
        formset3 = MultiImageFormSet(prefix='multiimage')
        formset5 = MultiImageFormSet2(prefix='multiimage2')

    return render(request, "portofolio/configurasi/moment_form.html", {'form2': form2,
       'formset3': formset3, 'formset5': formset5, 'orderproduct': orderproduct})

@login_required(login_url="account_login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def step5_update(request, slug):
    orderproduct = str(Order.objects.filter(user=request.user).first().items.first().product)
    # get instance portofolio from id
    obj = get_object_or_404(Portofolio, slug=slug)

    # verify user
    if obj.user != request.user:
        raise PermissionDenied

    # Create formset factory, tidak menggunakan base formset agar menampilkan object instance
    MultiImageFormSet = modelformset_factory(
        MultiImage,
        form=MultiImageForm,
        extra=0,
        can_delete=True,
        can_delete_extra=True
    )
    MultiImageFormSet2 = modelformset_factory(
        MultiImage,
        form=MultiImageForm,
        extra=0,
        can_delete=True,
        can_delete_extra=True
    )

    # create query set for multi image
    qs3 = MultiImage.objects.filter(portofolio=obj)

    # Define formset
    formset3 = MultiImageFormSet(request.POST or None, request.FILES, queryset= qs3, prefix='multiimage')
    formset5 = MultiImageFormSet2(request.POST or None, request.FILES, queryset=qs3, prefix='multiimage2')

    if request.method == "POST":
        form2 = PortoInfo2Form(request.POST or None, request.FILES, instance=obj)

        if form2.is_valid() and (formset3.is_valid() or formset5.is_valid()):
            # create portofolio instance
            instance = form2.save(commit=False)
            instance.save()

            # to create multiple image instance
            porto_instance = Portofolio.objects.get(pk=instance.pk)

            for form in formset3:
                # Not save blank field use has_changed()
                if form.is_valid() and form.has_changed():
                    child = form.save(commit=False)
                    child.portofolio = porto_instance
                    child.save()
            # Save deleted obj
            instances = formset3.save(commit=False)
            for obj in formset3.deleted_objects:
                obj.delete()

            for form in formset5:
                # Not save blank field use has_changed()
                if form.is_valid() and form.has_changed():
                    child = form.save(commit=False)
                    child.portofolio = porto_instance
                    child.save()
            # Save deleted obj
            instances = formset5.save(commit=False)
            for obj in formset5.deleted_objects:
                obj.delete()

            return redirect("portofolio:configurasi")

    else:
        form2 = PortoInfo2Form(instance=obj)
        formset3 = MultiImageFormSet(queryset= qs3, prefix='multiimage')
        formset5 = MultiImageFormSet2(queryset=qs3, prefix='multiimage2')

    context = {
        'form2': form2,
        'formset3': formset3,
        'formset5': formset5,
        'orderproduct': orderproduct,
    }

    # return redirect("portofolio:update_tampilan", slug=slug)
    return render(request, 'portofolio/configurasi/moment_form.html', context)

@login_required(login_url="account_login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def step6(request):
    orderproduct = str(Order.objects.filter(user=request.user).first().items.first().product)

    StoryFormSet = modelformset_factory(
        Story,
        form=StoryForm,
        formset=BaseRegisterFormSet,
        extra=1,
    )
    if request.method == 'POST':
        storyform = StoryFormSESSION(request)
        formset4 = StoryFormSet(request.POST or None, request.FILES, prefix='story')
        if formset4.is_valid():
            for count,form in enumerate(formset4):
                # Not save blank field use has_changed()
                if form.is_valid() and form.has_changed():
                    storyform.add(id=count, form=form)
            return redirect("portofolio:step7")
    else:
        formset4 = StoryFormSet(prefix='story')

    return render(request, "portofolio/configurasi/story_form.html", {'formset4': formset4, 'orderproduct': orderproduct,})

@login_required(login_url="account_login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def step6_update(request, slug):
    orderproduct = str(Order.objects.filter(user=request.user).first().items.first().product)
    # get instance portofolio from id
    obj = get_object_or_404(Portofolio, slug=slug)

    # verify user
    if obj.user != request.user:
        raise PermissionDenied

    StoryFormSet = modelformset_factory(
        Story,
        form=StoryForm,
        extra=0,
        can_delete=True,
        can_delete_extra=True
    )

    # create query set for story
    qs4 = Story.objects.filter(portofolio=obj)

    # Define formset
    formset4 = StoryFormSet(request.POST or None, request.FILES, queryset=qs4, prefix='story')
    print(formset4)
    if request.method == "POST":
        if formset4.is_valid():
            # to create multiple image instance
            porto_instance = Portofolio.objects.filter(user=request.user).first()

            for form in formset4:
                # Not save blank field use has_changed()
                if form.is_valid() and form.has_changed():
                    child = form.save(commit=False)
                    child.portofolio = porto_instance
                    child.save()
            # Save deleted obj
            instances = formset4.save(commit=False)
            for obj in formset4.deleted_objects:
                obj.delete()

            return redirect("portofolio:configurasi")

    else:
        formset4 = StoryFormSet(queryset=qs4, prefix='story')

    context = {
        'formset4': formset4,
        'orderproduct': orderproduct,
    }

    return render(request, 'portofolio/configurasi/story_form.html', context)

@login_required(login_url="account_login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def step7(request):
    user = request.user
    # get instance order
    order = get_object_or_404(Order, user=user)
    # orderitem instance by order
    orderitem = get_object_or_404(OrderItem, order= order)
    orderitem_product_str = str(orderitem.product)

    if request.method == 'POST':
        form = NavigasiForm(request.POST or None)
        if form.is_valid():
            request.session['link_iframe'] = form.cleaned_data.get('link_iframe')
            request.session['link_gmap'] = form.cleaned_data.get('link_gmap')
            request.session.modified = True

            if orderitem_product_str == "PLATINUM" or orderitem_product_str == "GOLD":
                return redirect("portofolio:step8")
            else:
                return redirect("portofolio:step9")
    else:
        form = NavigasiForm()

    return render(request, "portofolio/configurasi/map_form.html", {'form': form})

@login_required(login_url="account_login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def step7_update(request, slug):
    # get instance portofolio from id
    obj = get_object_or_404(Portofolio, slug=slug)

    # verify user
    if obj.user != request.user:
        raise PermissionDenied

    if request.method == "POST":
        form = NavigasiForm(request.POST or None, request.FILES, instance=obj)

        if form.is_valid():
            # create portofolio instance
            instance = form.save(commit=False)
            instance.save()
            return redirect("portofolio:configurasi")

    else:
        form = NavigasiForm(instance=obj)

    context = {
        'form': form,
    }
    return render(request, 'portofolio/configurasi/map_form.html', context)

@login_required(login_url="account_login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def step8(request):
    orderproduct = str(Order.objects.filter(user=request.user).first().items.first().product)

    DompetFormSet = modelformset_factory(
        Dompet,
        form=DompetForm,
        formset=BaseRegisterFormSet,
        extra=1,
    )
    if request.method == 'POST':
        dompetform = DompetFormSESSION(request)
        formset2 = DompetFormSet(request.POST or None, prefix='dompet')
        if formset2.is_valid():

            for count,form in enumerate(formset2):
                # Not save blank field use has_changed()
                if form.is_valid() and form.has_changed():
                    dompetform.add(id=count, form=form)
            return redirect("portofolio:step9")
    else:
        formset2 = DompetFormSet(prefix='dompet')

    return render(request, "portofolio/configurasi/dompet_form.html", {'formset2': formset2, 'orderproduct': orderproduct,})

@login_required(login_url="account_login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def step8_update(request, slug):
    orderproduct = str(Order.objects.filter(user=request.user).first().items.first().product)
    # get instance portofolio from id
    obj = get_object_or_404(Portofolio, slug=slug)

    # verify user
    if obj.user != request.user:
        raise PermissionDenied

    # Create formset factory, tidak menggunakan base formset agar menampilkan object instance
    DompetFormSet = modelformset_factory(
        Dompet,
        form=DompetForm,
        extra=0,
        can_delete=True,
        can_delete_extra=True
    )

    # create query set for specialinvitation
    qs2 = Dompet.objects.filter(portofolio=obj)

    # Define formset
    formset2 = DompetFormSet(request.POST or None,queryset= qs2, prefix='dompet')

    if request.method == "POST":
        if formset2.is_valid():
            # to create multiple image instance
            porto_instance = Portofolio.objects.filter(user=request.user).first()

            for form in formset2:
                # Not save blank field use has_changed()
                if form.is_valid() and form.has_changed():
                    child = form.save(commit=False)
                    child.portofolio = porto_instance
                    child.save()
            # Save deleted obj
            instances = formset2.save(commit=False)
            for obj in formset2.deleted_objects:
                obj.delete()

            return redirect("portofolio:configurasi")

    else:
        formset2 = DompetFormSet(queryset= qs2, prefix='dompet')


    context = {
        'formset2': formset2,
        'orderproduct': orderproduct,
    }

    # return redirect("portofolio:update_tampilan", slug=slug)
    return render(request, 'portofolio/configurasi/dompet_form.html', context)

@login_required(login_url="account_login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def step9(request):
    SpecialInviteFormSet = modelformset_factory(
        SpecialInvitation,
        form=SpecialInvitationForm,
        formset=BaseRegisterFormSet,
        extra=1,
    )
    specialinviteform = SpecialinviteFormSESSION(request)
    if request.method == 'POST':
        form2 = PortoInfo3Form(request.POST or None)
        formset = SpecialInviteFormSet(request.POST or None, prefix='invite')
        if form2.is_valid() and formset.is_valid():
            for count,form in enumerate(formset):
                # Not save blank field use has_changed()
                if form.is_valid() and form.has_changed():
                    specialinviteform.add(id=count, form=form)

            # ============== PORTOINFO3 ===============!
            request.session['kata_special_invite'] = form2.cleaned_data.get('kata_special_invite')
            request.session.modified = True

            return redirect("portofolio:step10")
    else:
        form2 = PortoInfo3Form()
        formset = SpecialInviteFormSet(prefix='invite')

    return render(request, "portofolio/configurasi/specialinvite_form.html", {'formset': formset, 'form2': form2})

@login_required(login_url="account_login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def step9_update(request, slug):
    # get instance portofolio from id
    obj = get_object_or_404(Portofolio, slug=slug)

    # verify user
    if obj.user != request.user:
        raise PermissionDenied

    # Create formset factory, tidak menggunakan base formset agar menampilkan object instance
    SpecialInviteFormSet = modelformset_factory(
        SpecialInvitation,
        form=SpecialInvitationForm,
        extra=0,
        can_delete=True,
        can_delete_extra=True
    )

    # create query set for specialinvitation
    qs = SpecialInvitation.objects.filter(portofolio=obj)

    # Define formset
    formset = SpecialInviteFormSet(request.POST or None,queryset= qs, prefix='invite')

    if request.method == "POST":
        form2 = PortoInfo3Form(request.POST or None, request.FILES, instance=obj)

        if form2.is_valid() and formset.is_valid():
            # create portofolio instance
            instance = form2.save(commit=False)
            instance.save()

            # to create multiple image instance
            porto_instance = Portofolio.objects.get(pk=instance.pk)

            # to create multiple value instance
            for form in formset:
                # Not save blank field use has_changed()
                if form.is_valid() and form.has_changed():
                    child = form.save(commit=False)
                    child.portofolio = porto_instance
                    child.save()
            # Save deleted obj
            instances = formset.save(commit=False)
            for obj in formset.deleted_objects:
                obj.delete()

            return redirect("portofolio:configurasi")

    else:
        form2 = PortoInfo3Form(instance=obj)
        formset = SpecialInviteFormSet(queryset= qs, prefix='invite')


    context = {
        'form2': form2,
        'formset': formset,
    }

    # return redirect("portofolio:update_tampilan", slug=slug)
    return render(request, 'portofolio/configurasi/specialinvite_form.html', context)

@login_required(login_url="account_login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def step10(request):
    if request.method == 'POST':
        form = CalenderForm(request.POST or None)
        if form.is_valid():
            request.session['location_countdown'] = form.cleaned_data.get('location_countdown')
            request.session['tanggal_countdown'] = form.cleaned_data.get('tanggal_countdown')
            request.session['waktu_countdown'] = form.cleaned_data.get('waktu_countdown')
            request.session['waktu_countdown_selesai'] = form.cleaned_data.get('waktu_countdown_selesai')
            request.session['timeZone'] = form.cleaned_data.get('timeZone')
            request.session.modified = True

            return redirect("portofolio:step11")
    else:
        form = CalenderForm()

    return render(request, "portofolio/configurasi/countdown_form.html", {'form': form})

@login_required(login_url="account_login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def step10_update(request, slug):
    # get instance portofolio from id
    obj = get_object_or_404(Portofolio, slug=slug)

    # verify user
    if obj.user != request.user:
        raise PermissionDenied

    if request.method == "POST":
        form = CalenderForm(request.POST or None, request.FILES, instance=obj)

        if form.is_valid():
            # create portofolio instance
            instance = form.save(commit=False)
            # save porto field ke field calender
            instance.name = instance.porto_name
            instance.location =  instance.location_countdown
            instance.startDate = instance.tanggal_countdown
            instance.startTime = instance.waktu_countdown
            instance.endTime = instance.waktu_countdown_selesai
            # save porto field ke field go to
            instance.lokasi = instance.location_countdown


            instance.save()

            return redirect("portofolio:configurasi")

    else:
        form = CalenderForm(instance=obj)


    context = {
        'form': form,
    }

    # return redirect("portofolio:update_tampilan", slug=slug)
    return render(request, 'portofolio/configurasi/countdown_form.html', context)

@login_required(login_url="account_login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def step11(request):
    if request.method == 'POST':
        form = PortoInfo5Form(request.POST or None, request.FILES)
        if form.is_valid():

            request.session['track'] = form.cleaned_data.get('track')
            request.session.modified = True

            return redirect("portofolio:step12")
    else:
        form = PortoInfo5Form()

    return render(request, "portofolio/configurasi/track_form.html", {'form': form})

@login_required(login_url="account_login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def step11_update(request, slug):
    # get instance portofolio from id
    obj = get_object_or_404(Portofolio, slug=slug)

    # verify user
    if obj.user != request.user:
        raise PermissionDenied

    if request.method == 'POST':
        form = PortoInfo5Form(request.POST or None, request.FILES, instance=obj)

        if form.is_valid():
            # create portofolio instance
            instance = form.save(commit=False)
            instance.save()
            # instance.delete()
            return redirect("portofolio:configurasi")

    else:
        form = PortoInfo5Form(instance=obj)

    context = {
        'form': form,
    }

    return render(request, "portofolio/configurasi/track_form.html", context)


@login_required(login_url="account_login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def step12(request):
    if request.method == 'POST':
        form3 = ThemeProductForm(request.POST or None, request.FILES)
        if form3.is_valid():
            user = request.user
            # get instance order
            order = get_object_or_404(Order, user=user)
            # orderitem instance by order
            orderitem = get_object_or_404(OrderItem, order=order)

            if str(orderitem.product) == "PLATINUM" or str(orderitem.product) == "GOLD":
                acaraform = AcaraFormSESSION(request)
                pasanganform = PasanganFormSESSION(request)
                multiimageform = MultiImageFormSESSION(request)
                storyform = StoryFormSESSION(request)
                dompetform = DompetFormSESSION(request)
                specialinviteform = SpecialinviteFormSESSION(request)
            else:
                acaraform = AcaraFormSESSION(request)
                pasanganform = PasanganFormSESSION(request)
                specialinviteform = SpecialinviteFormSESSION(request)

            # ============== PASANGAN ===============!
            for item in pasanganform:
                user = request.user
                Portofolio.objects.create(
                    user=user,
                    porto_name=request.session.get('porto_name', None),
                    description=request.session.get('description', None),
                    pname=item.get('pname'),
                    pinsta_link=f"https://www.instagram.com/{item.get('pinsta_link')}/",
                    panak_ke=item.get('panak_ke'),
                    pnama_ayah=item.get('pnama_ayah'),
                    pnama_ibu=item.get('pnama_ibu'),
                    ppicture=item.get('ppicture'),
                    lname=item.get('lname'),
                    linsta_link=f"https://www.instagram.com/{item.get('linsta_link')}/",
                    lanak_ke=item.get('lanak_ke'),
                    lnama_ayah=item.get('lnama_ayah'),
                    lnama_ibu=item.get('lnama_ibu'),
                    lpicture=item.get('lpicture'),
                    # add to calender
                    name=request.session.get('porto_name', None),
                )
            pasanganform.clear()
            # ============== PASANGAN END ===============!

            # to create multiple image instance
            user = request.user
            porto_instance = Portofolio.objects.filter(user=user).first()

            # ============== ACARA ===============!
            for item in acaraform:
                Acara.objects.create(
                    portofolio=porto_instance,
                    tempat_acara=item.get('tempat_acara'),
                    nama_acara=item.get('nama_acara'),
                    tanggal_acara=item.get('tanggal_acara'),
                    waktu_mulai_acara=item.get('waktu_mulai_acara'),
                    waktu_selesai_acara=item.get('waktu_selesai_acara'),
                    link_gmap_acara=item.get('link_gmap_acara'),

                )
            acaraform.clear()
            # ============== ACARA END ===============!

            # ============== QUOTE ===============!
            Quote.objects.create(
                portofolio=porto_instance,
                pembuka=request.session.get('pembuka', None),
                ayat=request.session.get('ayat', None),
                kutipan=request.session.get('kutipan', None),
            )

            # del portiinfo sessions
            del request.session['porto_name']
            del request.session['description']

            if 'ayat' in request.session:
                # del quote sessions
                del request.session['ayat']
                request.session.modified = True
            if 'pembuka' in request.session:
                # del quote sessions
                del request.session['pembuka']
                request.session.modified = True
            if 'kutipan' in request.session:
                # del quote sessions
                del request.session['kutipan']
                request.session.modified = True

            # ============== QUOTE END ===============!

            if str(orderitem.product) == "PLATINUM" or str(orderitem.product) == "GOLD":
                # ============== MOMENT ===============!
                for item in multiimageform:
                    MultiImage.objects.create(
                        portofolio=porto_instance,
                        image=item.get('image'),
                    )
                multiimageform.clear()


                url_video = request.session.get('video', None)
                if url_video != "":
                    video = re.search('(?P<name>https?://[^\s]+\w)', url_video).group('name')
                else:
                    video = None

                Portofolio.objects.filter(user=user).update(
                    video=video,
                    livestream=request.session.get('livestream', None),
                    kata_live_streaming=request.session.get('kata_live_streaming', None),
                    kata_moment=request.session.get('kata_moment', None),
                )

                # del portiinfo sessions
                if 'video' in request.session:
                    del request.session['video']
                if 'livestream' in request.session:
                    if orderitem.product == "GOLD":
                        del request.session['livestream']
                if 'kata_live_streaming' in request.session:
                    del request.session['kata_live_streaming']
                if 'kata_live_streaming' in request.session:
                    del request.session['kata_live_streaming']
                # ============== MOMENT END ===============!

                # ============== STORY ===============!
                for item in storyform:
                    Story.objects.create(
                        portofolio=porto_instance,
                        image=item.get('image'),
                        cerita=item.get('cerita'),
                        year=item.get('year'),
                    )
                storyform.clear()
                # ============== STORY END ===============!

                # ============== DOMPET ===============!
                for item in dompetform:
                    Dompet.objects.create(
                        portofolio=porto_instance,
                        nomor=item.get('nomor'),
                        pemilik=item.get('pemilik'),
                        rekening=item.get('rekening'),
                    )
                dompetform.clear()
                # ============== DOMPET END ===============!

            # ============== NAVIGASI ===============!
            url = request.session.get('link_iframe', None)
            link_iframe = re.search('(?P<name>https?://[^\s]+\w)', url).group('name')

            Portofolio.objects.filter(user=user).update(
                link_iframe=link_iframe,
                link_gmap=request.session.get('link_gmap', None),
            )

            # del portiinfo sessions
            if 'link_iframe' in request.session:
                del request.session['link_iframe']
            if 'link_gmap' in request.session:
                del request.session['link_gmap']
            # ============== NAVIGASI END ===============!

            # ============== SPECIAL INVITE ===============!
            for item in specialinviteform:
                SpecialInvitation.objects.create(
                    portofolio=porto_instance,
                    name_invite=item.get('name_invite'),
                )
            specialinviteform.clear()

            Portofolio.objects.filter(user=user).update(
                kata_special_invite=request.session.get('kata_special_invite', None),
            )

            # del portiinfo sessions
            if 'kata_special_invite' in request.session:
                del request.session['kata_special_invite']
            # ============== SPECIAL INVITE END ===============!

            # ============== CALENDER ===============!
            tanggal_countdown = request.session.get('tanggal_countdown', None)
            waktu_countdown = request.session.get('waktu_countdown', None)
            datetime_countdown = datetime.combine(tanggal_countdown, waktu_countdown).strftime("%Y-%m-%d %H:%M")

            Portofolio.objects.filter(user=user).update(
                location_countdown=request.session.get('location_countdown', None),
                timeZone=request.session.get('timeZone', None),
                tanggal_countdown=tanggal_countdown,
                waktu_countdown=waktu_countdown,
                waktu_countdown_selesai=request.session.get('waktu_countdown_selesai', None),
                datetime_countdown=datetime_countdown,
                # add to calender
                startDate=tanggal_countdown,
                location=str(request.session.get('location_countdown', None)),
                startTime=request.session.get('waktu_countdown', None),
                endTime=request.session.get('waktu_countdown_selesai', None),
                #  navigasi
                lokasi=request.session.get('location_countdown', None),
            )

            # del portiinfo sessions
            del request.session['location_countdown']
            del request.session['timeZone']
            del request.session['tanggal_countdown']
            del request.session['waktu_countdown']
            del request.session['waktu_countdown_selesai']
            # ============== NAVIGASI END ===============!

            # # ============== COVER BACKGROUND ===============!
            # Portofolio.objects.filter(user=user).update(
            #     cover_background=request.session.get('cover_background', None),
            #     open_background=request.session.get('open_background', None),
            # )
            #
            # # del portiinfo sessions
            # if 'cover_background' in request.session:
            #     del request.session['cover_background']
            # if 'open_background' in request.session:
            #     del request.session['open_background']
            # # ============== NAVIGASI END ===============!

            # ============== COVER TRACK ===============!
            Portofolio.objects.filter(user=user).update(
                track=request.session.get('track', None),
            )

            # del portiinfo sessions
            if 'track' in request.session:
                del request.session['track']
            # ============== TRACK END ===============!


            request.session['theme'] = form3.cleaned_data.get('theme')
            request.session.modified = True

            # ============== THEME ===============!
            # to create theme product
            instance_order = Order.objects.get(user=user)
            instance_orderitem = OrderItem.objects.get(order=instance_order)

            ThemeProduct.objects.create(
                portofolio = porto_instance,
                theme = request.session.get('theme', None),
                fitur = instance_orderitem.product,
            )

            # del portiinfo sessions
            del request.session['theme']
            # ============== THEME END ===============!


            return redirect("portofolio:step13")
    else:
        form3 = ThemeProductForm()

    return render(request, "portofolio/configurasi/tampilan_form.html", {'form3': form3})

@login_required(login_url="account_login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def step12_update(request, slug):
    # get instance portofolio from id
    obj = get_object_or_404(Portofolio, slug=slug)
    # theme product instance by porto id
    obj_themeproduct = get_object_or_404(ThemeProduct, portofolio= obj)

    # verify user
    if obj.user != request.user:
        raise PermissionDenied

    if request.method == "POST":
        form3 = ThemeProductForm(request.POST or None, request.FILES, instance=obj_themeproduct)

        if form3.is_valid():
            # to create multiple image instance
            porto_instance = Portofolio.objects.filter(user=request.user).first()

            # to create theme product
            user = request.user
            instance_order = Order.objects.get(user=user)
            instance_orderitemfiture = OrderItem.objects.get(order=instance_order)

            instance_orderitem = form3.save(commit=False)
            instance_orderitem.portofolio = porto_instance
            instance_orderitem.product = instance_orderitemfiture.product
            instance_orderitem.save()

            return redirect("portofolio:configurasi")

    else:
        form3 = ThemeProductForm(instance=obj_themeproduct)


    context = {
        'form3': form3,
    }

    # return redirect("portofolio:update_tampilan", slug=slug)
    return render(request, 'portofolio/configurasi/tampilan_form.html', context)

@login_required(login_url="account_login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def step13(request):
    porto_instance = Portofolio.objects.filter(user=request.user).first()
    print(Portofolio.objects.filter(user=request.user))
    if request.method == 'POST':
        form = PortoInfo4Form(request.POST or None, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            porto_instance.cover_background = form.cleaned_data.get("cover_background")
            porto_instance.open_background = form.cleaned_data.get("open_background")

            porto_instance.save()
            # request.session['cover_background'] = form.cleaned_data.get('cover_background')
            # request.session['open_background'] = form.cleaned_data.get('open_background')
            # request.session.modified = True

            return redirect("portofolio:step14")
    else:
        form = PortoInfo4Form()

    return render(request, "portofolio/configurasi/cover_form.html", {'form': form})

@login_required(login_url="account_login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def step13_update(request, slug):
    # get instance portofolio from id
    obj = get_object_or_404(Portofolio, slug=slug)

    # verify user
    if obj.user != request.user:
        raise PermissionDenied

    if request.method == "POST":
        form = PortoInfo4Form(request.POST or None, request.FILES, instance=obj)

        if form.is_valid():
            # create portofolio instance
            instance = form.save(commit=False)
            instance.save()
            # instance.delete()
            return redirect("portofolio:configurasi")

    else:
        form = PortoInfo4Form(instance=obj)

    context = {
        'form': form,
        'obj': obj,
    }
    return render(request, 'portofolio/configurasi/cover_form.html', context)

@login_required(login_url="account_login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def step14(request):
    porto_instance = Portofolio.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = PasanganPictureForm(request.POST or None, request.FILES)
        if form.is_valid():
            imagestring = form.cleaned_data.get("ppicture")
            imagestring2 = form.cleaned_data.get("lpicture")

            x = form.cleaned_data.get('x')
            y = form.cleaned_data.get('y')
            w = form.cleaned_data.get('width')
            h = form.cleaned_data.get('height')

            x2 = form.cleaned_data.get('x2')
            y2 = form.cleaned_data.get('y2')
            w2 = form.cleaned_data.get('width2')
            h2 = form.cleaned_data.get('height2')


            if imagestring != None:
                img = Image.open(imagestring).convert('RGB')
                if x != None and y != None and w != None and h != None:
                    crop_img = img.crop((x, y, w + x, h + y))
                    thumb_io = BytesIO()
                    crop_img.save(thumb_io, 'JPEG', quality=85)
                    porto_instance.ppicture.save('ppicture.jpeg', ContentFile(thumb_io.getvalue()))

            if imagestring2 != None:
                img2 = Image.open(imagestring2).convert('RGB')
                if x2 != None and y2 != None and w2 != None and h2 != None:
                    crop_img2 = img2.crop((x2, y2, w2 + x2, h2 + y2))
                    thumb_io2 = BytesIO()
                    crop_img2.save(thumb_io2, 'JPEG', quality=85)
                    porto_instance.lpicture.save('lpicture.jpeg', ContentFile(thumb_io2.getvalue()))

            porto_instance.save()

            return redirect("portofolio:configurasi")
    else:
        form = PasanganPictureForm()

    return render(request, "portofolio/configurasi/pasangan_picture_form.html", {'form': form})

@login_required(login_url="account_login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def step14_update(request, slug):
    # get instance portofolio from id
    obj = get_object_or_404(Portofolio, slug=slug)

    # verify user
    if obj.user != request.user:
        raise PermissionDenied

    porto_instance = Portofolio.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = PasanganPictureForm(request.POST or None, request.FILES, instance=obj)
        if form.is_valid():
            imagestring = form.cleaned_data.get("ppicture")
            imagestring2 = form.cleaned_data.get("lpicture")

            x = form.cleaned_data.get('x')
            y = form.cleaned_data.get('y')
            w = form.cleaned_data.get('width')
            h = form.cleaned_data.get('height')

            x2 = form.cleaned_data.get('x2')
            y2 = form.cleaned_data.get('y2')
            w2 = form.cleaned_data.get('width2')
            h2 = form.cleaned_data.get('height2')

            if imagestring != None:
                img = Image.open(imagestring).convert('RGB')
                if x != None and y != None and w != None and h != None:
                    crop_img = img.crop((x, y, w + x, h + y))
                    thumb_io = BytesIO()
                    crop_img.save(thumb_io, 'JPEG', quality=85)
                    porto_instance.ppicture.save('ppicture.jpeg', ContentFile(thumb_io.getvalue()))

            if imagestring2 != None:
                img2 = Image.open(imagestring2).convert('RGB')
                if x2 != None and y2 != None and w2 != None and h2 != None:
                    crop_img2 = img2.crop((x2, y2, w2 + x2, h2 + y2))
                    thumb_io2 = BytesIO()
                    crop_img2.save(thumb_io2, 'JPEG', quality=85)
                    porto_instance.lpicture.save('lpicture.jpeg', ContentFile(thumb_io2.getvalue()))
            porto_instance.save()

            return redirect("portofolio:configurasi")
    else:
        form = PasanganPictureForm(instance=obj)

    return render(request, "portofolio/configurasi/pasangan_picture_form.html", {'form': form})
# ============== SHARE UNDANGAN ===============!

@login_required(login_url="account_login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def share_undangan(request):
    context = {
        "website_frontend" : production.WEBSITE_URL_FRONTEND,
        "website_backend" : production.WEBSITE_URL,
        "katas" : Kata.objects.all(),
    }
    return render(request, 'portofolio/configurasi/share_undangan.html', context)

# ============== END SHARE UNDANGAN ===============!


# ============== DELETE BACKGROUND ===============!

def open_background_delete(request, slug):
    obj = get_object_or_404(Portofolio, slug=slug)
    obj.open_background = None
    obj.save()

    return redirect("portofolio:step11_update", slug=obj.slug)

def cover_background_delete(request, slug):
    obj = get_object_or_404(Portofolio, slug=slug)
    obj.cover_background = None
    obj.save()

    return redirect("portofolio:step11_update", slug=obj.slug)

# ============== DELETE BACKGROUND END ===============!



#
# # ============== REGISTER ===============!
# def register(request, id=None):
#     # initiate formset
#     StoryFormSet = modelformset_factory(
#         Story,
#         form=StoryForm,
#         formset=BaseRegisterFormSet,
#         extra=1,
#     )
#     SpecialInviteFormSet = modelformset_factory(
#         SpecialInvitation,
#         form=SpecialInvitationForm,
#         formset=BaseRegisterFormSet,
#         extra=1,
#     )
#     DompetFormSet = modelformset_factory(
#         Dompet,
#         form=DompetForm,
#         formset=BaseRegisterFormSet,
#         extra=1,
#     )
#     MultiImageFormSet = modelformset_factory(
#         MultiImage,
#         form=MultiImageForm,
#         formset=BaseRegisterFormSet,
#         extra=1,
#     )
#     MultiImageFormSet2 = modelformset_factory(
#         MultiImage,
#         form=MultiImageForm,
#         formset=BaseRegisterFormSet,
#         extra=1,
#     )
#
#     AcaraFormSet = modelformset_factory(
#         Acara,
#         form=AcaraForm,
#         formset=BaseRegisterFormSet,
#         extra=1,
#     )
#
#     portofolio = Portofolio.objects.filter(user=request.user).exists()
#     if portofolio == False:
#         if request.method == "POST":
#             form = PortofolioForm(request.POST or None, request.FILES)
#             form2 = QuoteForm(request.POST or None, request.FILES)
#             form3 = ThemeProductForm(request.POST or None, request.FILES)
#
#             formset = SpecialInviteFormSet(request.POST or None, prefix='invite')
#             formset2 = DompetFormSet(request.POST or None, prefix='dompet')
#             formset3 = MultiImageFormSet(request.POST or None, request.FILES, prefix='multiimage')
#             formset4 = StoryFormSet(request.POST or None, request.FILES, prefix='story')
#             formset5 = MultiImageFormSet2(request.POST or None, request.FILES, prefix='multiimage2')
#             formset6 = AcaraFormSet(request.POST or None, request.FILES, prefix='acara')
#             print(request.POST)
#             # form validation
#             if form.is_valid() and form2.is_valid() and form3.is_valid() and formset.is_valid() \
#                 and formset2.is_valid() and formset4.is_valid():
#                 # create portofolio instance
#                 instance = form.save(commit=False)
#                 # save user to porto
#                 user = request.user
#                 instance.user = user
#                 # save porto field ke field calender
#                 instance.name = instance.porto_name
#                 instance.location = instance.location_countdown
#                 instance.startDate = instance.tanggal_countdown
#                 instance.startTime = instance.waktu_countdown
#                 instance.endTime = instance.waktu_countdown_selesai
#                 # save porto field ke field go to
#                 instance.lokasi = instance.location_countdown
#
#
#                 instance.save()
#
#                 # to create multiple image instance
#                 porto_instance = Portofolio.objects.get(pk=instance.pk)
#
#                 # to create instance quote
#                 instance_quote = form2.save(commit=False)
#                 instance_quote.portofolio = porto_instance
#                 instance_quote.save()
#
#                 # to create theme product
#                 instance_order = Order.objects.get(user=user)
#                 instance_orderitem = OrderItem.objects.get(order=instance_order)
#
#                 instance_orderitem2 = form3.save(commit=False)
#                 instance_orderitem2.portofolio = porto_instance
#                 instance_orderitem2.product = instance_orderitem.product
#                 instance_orderitem2.save()
#
#                 # to create multiple value instance
#                 for form in formset:
#                     # Not save blank field use has_changed()
#                     if form.is_valid() and form.has_changed():
#                         child = form.save(commit=False)
#                         child.portofolio = porto_instance
#                         child.save()
#
#                 for form in formset2:
#                     # Not save blank field use has_changed()
#                     if form.is_valid() and form.has_changed():
#                         child = form.save(commit=False)
#                         child.portofolio = porto_instance
#                         child.save()
#
#                 for form in formset3:
#                     # Not save blank field use has_changed()
#                     if form.is_valid() and form.has_changed():
#                         child = form.save(commit=False)
#                         child.portofolio = porto_instance
#                         child.save()
#
#                 for form in formset4:
#                     # Not save blank field use has_changed()
#                     if form.is_valid() and form.has_changed():
#                         child = form.save(commit=False)
#                         child.portofolio = porto_instance
#                         child.save()
#
#                 for form in formset5:
#                     # Not save blank field use has_changed()
#                     if form.is_valid() and form.has_changed():
#                         child = form.save(commit=False)
#                         child.portofolio = porto_instance
#                         child.save()
#
#                 for form in formset6:
#                     # Not save blank field use has_changed()
#                     if form.is_valid() and form.has_changed():
#                         child = form.save(commit=False)
#                         child.portofolio = porto_instance
#                         child.save()
#
#                 messages.success(request, "Registered Successfully !")
#                 return redirect("portofolio:configurasi")
#
#             else:
#                 return render(request, "portofolio/register_porto.html", {'form': form,
#                     'form2': form2, 'form3': form3, 'formset': formset, 'formset2': formset2, 'formset3': formset3,
#                     'formset4': formset4, 'formset5': formset5, 'formset6': formset6})
#
#         else:
#             form = PortofolioForm()
#             form2 = QuoteForm()
#             form3 = ThemeProductForm()
#             formset = SpecialInviteFormSet(prefix='invite')
#             formset2 = DompetFormSet(prefix='dompet')
#             formset3 = MultiImageFormSet(prefix='multiimage')
#             formset4 = StoryFormSet(prefix='story')
#             formset5 = MultiImageFormSet2(prefix='multiimage2')
#             formset6 = AcaraFormSet(prefix='acara')
#
#     else:
#         return render(request, 'portofolio/regis_failed.html')
#
#     return render(request, "portofolio/register_porto.html", {'form': form,
#         'form2': form2, 'form3': form3, 'formset': formset, 'formset2': formset2, 'formset3': formset3,
#         'formset4': formset4, 'formset5': formset5, 'formset6': formset6})

# def update(request, slug):
#     # get instance portofolio from id
#     obj = get_object_or_404(Portofolio, slug=slug)
#     # quote instance by porto id
#     obj_quote = get_object_or_404(Quote, portofolio= obj)
#     # theme product instance by porto id
#     obj_themeproduct = get_object_or_404(ThemeProduct, portofolio= obj)
#
#     # Create formset factory, tidak menggunakan base formset agar menampilkan object instance
#     SpecialInviteFormSet = modelformset_factory(
#         SpecialInvitation,
#         form=SpecialInvitationForm,
#         extra=1,
#         can_delete=True,
#         can_delete_extra=True
#     )
#     DompetFormSet = modelformset_factory(
#         Dompet,
#         form=DompetForm,
#         extra=1,
#         can_delete=True,
#         can_delete_extra=True
#     )
#     MultiImageFormSet = modelformset_factory(
#         MultiImage,
#         form=MultiImageForm,
#         extra=1,
#         can_delete=True,
#         can_delete_extra=True
#     )
#     StoryFormSet = modelformset_factory(
#         Story,
#         form=StoryForm,
#         extra=1,
#         can_delete=True,
#         can_delete_extra=True
#     )
#     MultiImageFormSet2 = modelformset_factory(
#         MultiImage,
#         form=MultiImageForm,
#         extra=1,
#         can_delete=True,
#         can_delete_extra=True
#     )
#     AcaraFormSet = modelformset_factory(
#         Acara,
#         form=AcaraForm,
#         extra=1,
#         can_delete=True,
#         can_delete_extra=True
#     )
#
#     # create query set for specialinvitation
#     qs = SpecialInvitation.objects.filter(portofolio=obj)
#     # create query set for dompet
#     qs2 = Dompet.objects.filter(portofolio=obj)
#     # create query set for multi image
#     qs3 = MultiImage.objects.filter(portofolio=obj)
#     # create query set for story
#     qs4 = Story.objects.filter(portofolio=obj)
#     # create query set for acara
#     qs5 = Acara.objects.filter(portofolio=obj)
#
#     # Define formset
#     formset = SpecialInviteFormSet(request.POST or None,queryset= qs, prefix='invite')
#     formset2 = DompetFormSet(request.POST or None,queryset= qs2, prefix='dompet')
#     formset3 = MultiImageFormSet(request.POST or None, request.FILES, queryset= qs3, prefix='multiimage')
#     formset4 = StoryFormSet(request.POST or None, request.FILES, queryset=qs4, prefix='story')
#     formset5 = MultiImageFormSet2(request.POST or None, request.FILES, queryset=qs3, prefix='multiimage2')
#     formset6 = AcaraFormSet(request.POST or None, request.FILES, queryset=qs5, prefix='acara')
#
#     if request.method == "POST":
#         form = PortofolioForm(request.POST or None, request.FILES, instance=obj)
#         form2 = QuoteForm(request.POST or None, request.FILES, instance=obj_quote)
#         form3 = ThemeProductForm(request.POST or None, request.FILES, instance=obj_themeproduct)
#
#         if form.is_valid() and form2.is_valid() and form3.is_valid() and formset.is_valid() \
#             and formset2.is_valid() and formset4.is_valid():
#             # create portofolio instance
#             instance = form.save(commit=False)
#             # save user to porto
#             user = request.user
#             print(user)
#             instance.user = user
#             # save porto field ke field calender
#             instance.name = instance.porto_name
#             instance.location =  instance.location_countdown
#             instance.startDate = instance.tanggal_countdown
#             instance.startTime = instance.waktu_countdown
#             instance.endTime = instance.waktu_countdown_selesai
#             # save porto field ke field go to
#             instance.lokasi = instance.location_countdown
#
#
#             instance.save()
#
#             # to create multiple image instance
#             porto_instance = Portofolio.objects.get(pk=instance.pk)
#
#             # to create instance quote
#             instance_quote = form2.save(commit=False)
#             instance_quote.portofolio = porto_instance
#             instance_quote.save()
#
#             # to create theme product
#             instance_order = Order.objects.get(user=user)
#             instance_orderitemfiture = OrderItem.objects.get(order=instance_order)
#
#             instance_orderitem = form3.save(commit=False)
#             instance_orderitem.portofolio = porto_instance
#             instance_orderitem.fitur = instance_orderitemfiture.product
#             instance_orderitem.save()
#
#             # to create multiple value instance
#             for form in formset:
#                 # Not save blank field use has_changed()
#                 if form.is_valid() and form.has_changed():
#                     child = form.save(commit=False)
#                     child.portofolio = porto_instance
#                     child.save()
#             # Save deleted obj
#             instances = formset.save(commit=False)
#             for obj in formset.deleted_objects:
#                 obj.delete()
#
#             for form in formset2:
#                 # Not save blank field use has_changed()
#                 if form.is_valid() and form.has_changed():
#                     child = form.save(commit=False)
#                     child.portofolio = porto_instance
#                     child.save()
#             # Save deleted obj
#             instances = formset2.save(commit=False)
#             for obj in formset2.deleted_objects:
#                 obj.delete()
#
#             for form in formset3:
#                 # Not save blank field use has_changed()
#                 if form.is_valid() and form.has_changed():
#                     child = form.save(commit=False)
#                     child.portofolio = porto_instance
#                     child.save()
#             # Save deleted obj
#             instances = formset3.save(commit=False)
#             for obj in formset3.deleted_objects:
#                 obj.delete()
#
#             for form in formset4:
#                 # Not save blank field use has_changed()
#                 if form.is_valid() and form.has_changed():
#                     child = form.save(commit=False)
#                     child.portofolio = porto_instance
#                     child.save()
#             # Save deleted obj
#             instances = formset4.save(commit=False)
#             for obj in formset4.deleted_objects:
#                 obj.delete()
#
#             for form in formset5:
#                 # Not save blank field use has_changed()
#                 if form.is_valid() and form.has_changed():
#                     child = form.save(commit=False)
#                     child.portofolio = porto_instance
#                     child.save()
#             # Save deleted obj
#             instances = formset5.save(commit=False)
#             for obj in formset5.deleted_objects:
#                 obj.delete()
#
#             for form in formset6:
#                 # Not save blank field use has_changed()
#                 if form.is_valid() and form.has_changed():
#                     child = form.save(commit=False)
#                     child.portofolio = porto_instance
#                     child.save()
#             # Save deleted obj
#             instances = formset6.save(commit=False)
#             for obj in formset6.deleted_objects:
#                 obj.delete()
#
#             messages.success(request, "Data saved!")
#             return redirect("portofolio:configurasi")
#
#     else:
#         form = PortofolioForm(instance=obj)
#         form2 = QuoteForm(instance=obj_quote)
#         form3 = ThemeProductForm(instance=obj_themeproduct)
#         formset = SpecialInviteFormSet(queryset= qs, prefix='invite')
#         formset2 = DompetFormSet(queryset= qs2, prefix='dompet')
#         formset3 = MultiImageFormSet(queryset= qs3, prefix='multiimage')
#         formset4 = StoryFormSet(queryset=qs4, prefix='story')
#         formset5 = MultiImageFormSet2(queryset=qs3, prefix='multiimage2')
#         formset6 = AcaraFormSet(queryset=qs5, prefix='acara')
#
#
#     context = {
#         'form': form,
#         'form2': form2,
#         'form3': form3,
#         'formset': formset,
#         'formset2': formset2,
#         'formset3': formset3,
#         'formset4': formset4,
#         'formset5': formset5,
#         'formset6': formset6
#     }
#
#     return render(request, 'portofolio/portofolio_detail.html', context)


#################### SERIALIZER #######################
# Portofolio
class PortofolioList(generics.ListCreateAPIView):
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
    queryset = Ucapan.objects.all()
    serializer_class = UcapanSerializer
    name = 'ucapan-list'
    filterset_fields = ['portofolio__slug']


class UcapanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ucapan.objects.all()
    serializer_class = UcapanSerializer
    name = 'ucapan-detail'

# Hadir
class HadirList(generics.ListCreateAPIView):
    queryset = Hadir.objects.all()
    serializer_class = HadirSerializer
    name = 'hadir-list'
    filterset_fields = ['portofolio__slug']


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
    queryset = Acara.objects.all()
    serializer_class = AcaraSerializer
    name = 'acara-list'
    filterset_fields = ['portofolio__slug']


class AcaraDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Acara.objects.all()
    serializer_class = AcaraSerializer
    name = 'acara-detail'


# ROOT
class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'portofolios': reverse('portofolio:portofolio-list', request=request),
            'rekenings': reverse('portofolio:rekening-list', request=request),
            'dompets': reverse('portofolio:dompet-list', request=request),
            'multiimages': reverse('portofolio:multiimage-list', request=request),
            'specialinvitations': reverse('portofolio:specialinvitation-list', request=request),
            'payments': reverse('portofolio:payment-list', request=request),
            'quotes': reverse('portofolio:quote-list', request=request),
            'ucapans': reverse('portofolio:ucapan-list', request=request),
            'hadirs': reverse('portofolio:hadir-list', request=request),
            'fiturs': reverse('portofolio:fitur-list', request=request),
            'themeproducts': reverse('portofolio:themeproduct-list', request=request),
            'themes': reverse('portofolio:theme-list', request=request),
            'story': reverse('portofolio:story-list', request=request),
            'acara': reverse('portofolio:acara-list', request=request),
            })