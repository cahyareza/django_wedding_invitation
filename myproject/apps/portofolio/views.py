from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
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

from rest_framework import filters
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet

from myproject.apps.coupon.models import Coupon
from myproject.apps.order.models import Order, OrderItem
from .models import MultiImage, Portofolio, SpecialInvitation, Dompet, Quote, Fitur, \
    Rekening, Payment, MultiImage, SpecialInvitation, Ucapan, Hadir, Fitur, \
    Theme, ThemeProduct, Story, Acara

from .forms import PortofolioForm, MultiImageForm, SpecialInvitationForm, \
    BaseRegisterFormSet, DompetForm, QuoteForm, ThemeProductForm, StoryForm, AcaraForm \

def home(request):
    portofolio = Portofolio.objects.all()
    ucapan = Ucapan.objects.all()
    dompet = Dompet.objects.all()
    hadir = Hadir.objects.all()

    obj_silver = Coupon.objects.filter(active=True, silver=True).first()
    obj_platinum = Coupon.objects.filter(active=True, platinum=True).first()
    obj_gold = Coupon.objects.filter(active=True, gold=True).first()

    current_time = timezone.now()

    # Check if instance available
    if obj_silver or obj_platinum or obj_gold:

        context = {
            'portofolio': portofolio,
            'ucapan': ucapan,
            'dompet': dompet,
            'hadir': hadir,
            'obj_silver': obj_silver,
            'obj_platinum': obj_platinum,
            'obj_gold': obj_gold,
            'discount_str_silver': False,
            'discount_value_silver': False,
            'discount_percent_silver': False,
            'discount_str_platinum': False,
            'discount_value_platinum': False,
            'discount_percent_platinum': False,
            'discount_str_gold': False,
            'discount_value_gold': False,
            'discount_percent_gold': False
        }

        # SILVER
        if obj_silver and obj_silver.valid_to >= current_time:
            discount_value_silver = obj_silver.discount
            discount_percent_silver = 1 - discount_value_silver/100
            discount_str_silver = f"{obj_silver.discount}%"

            context['discount_str_silver'] =  discount_str_silver
            context['discount_value_silver'] = discount_value_silver
            context['discount_percent_silver'] = discount_percent_silver

        # PLATINUM
        if obj_platinum and obj_platinum.valid_to >= current_time:
            discount_value_platinum = obj_platinum.discount
            discount_percent_platinum = 1 - discount_value_platinum/100
            discount_str_platinum = f"{obj_platinum.discount}%"

            context['discount_str_platinum'] = discount_str_platinum
            context['discount_value_platinum'] = discount_value_platinum
            context['discount_percent_platinum'] = discount_percent_platinum

        # GOLD
        if obj_gold and obj_gold.valid_to >= current_time:
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
            'portofolio': portofolio,
            'ucapan': ucapan,
            'dompet': dompet,
            'hadir': hadir,
            'obj_silver': obj_silver,
            'obj_platinum': obj_platinum,
            'obj_gold': obj_gold,
            'discount_str_silver': False,
            'discount_value_silver': False,
            'discount_percent_silver': False,
            'discount_str_platinum': False,
            'discount_value_platinum': False,
            'discount_percent_platinum': False,
            'discount_str_gold': False,
            'discount_value_gold': False,
            'discount_percent_gold': False
        }

        return render(request, 'index.html', context)

def configurasi_porto(request):
    user = request.user
    portofolio = Portofolio.objects.filter(user=user).first()
    context = {
        'portofolio': portofolio,
    }
    return render(request, 'portofolio/configurasi/icon_config.html', context)

# Portofolio registration
def register_awal(request, id=None):
    # initiate formset
    StoryFormSet = modelformset_factory(
        Story,
        form=StoryForm,
        formset=BaseRegisterFormSet,
        extra=1,
    )
    SpecialInviteFormSet = modelformset_factory(
        SpecialInvitation,
        form=SpecialInvitationForm,
        formset=BaseRegisterFormSet,
        extra=1,
    )
    DompetFormSet = modelformset_factory(
        Dompet,
        form=DompetForm,
        formset=BaseRegisterFormSet,
        extra=1,
    )
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

    AcaraFormSet = modelformset_factory(
        Acara,
        form=AcaraForm,
        formset=BaseRegisterFormSet,
        extra=1,
    )

    portofolio = Portofolio.objects.filter(user=request.user).exists()
    if portofolio == False:
        if request.method == "POST":
            form = PortofolioForm(request.POST or None, request.FILES)
            form2 = QuoteForm(request.POST or None, request.FILES)
            form3 = ThemeProductForm(request.POST or None, request.FILES)

            formset = SpecialInviteFormSet(request.POST or None, prefix='invite')
            formset2 = DompetFormSet(request.POST or None, prefix='dompet')
            formset3 = MultiImageFormSet(request.POST or None, request.FILES, prefix='multiimage')
            formset4 = StoryFormSet(request.POST or None, request.FILES, prefix='story')
            formset5 = MultiImageFormSet2(request.POST or None, request.FILES, prefix='multiimage2')
            formset6 = AcaraFormSet(request.POST or None, request.FILES, prefix='acara')
            print(request.POST)
            # form validation
            if form.is_valid():
                # create portofolio instance
                instance = form.save(commit=False)
                # save user to porto
                user = request.user
                instance.user = user
                # save porto field ke field calender
                instance.name = instance.porto_name
                instance.location = instance.location_countdown
                instance.startDate = instance.tanggal_countdown
                instance.startTime = instance.waktu_countdown
                instance.endTime = instance.waktu_countdown_selesai
                # save porto field ke field go to
                instance.lokasi = instance.location_countdown


                instance.save()

                # to create multiple image instance
                porto_instance = Portofolio.objects.get(pk=instance.pk)

                # to create instance quote
                instance_quote = form2.save(commit=False)
                instance_quote.portofolio = porto_instance
                instance_quote.save()

                # to create theme product
                instance_order = Order.objects.get(user=user)
                instance_orderitem = OrderItem.objects.get(order=instance_order)

                instance_orderitem = form3.save(commit=False)
                instance_orderitem.portofolio = porto_instance
                instance_orderitem.fitur = instance_orderitem.fitur
                instance_orderitem.save()

                # to create multiple value instance
                for form in formset:
                    # Not save blank field use has_changed()
                    if form.is_valid() and form.has_changed():
                        child = form.save(commit=False)
                        child.portofolio = porto_instance
                        child.save()

                for form in formset2:
                    # Not save blank field use has_changed()
                    if form.is_valid() and form.has_changed():
                        child = form.save(commit=False)
                        child.portofolio = porto_instance
                        child.save()

                for form in formset3:
                    # Not save blank field use has_changed()
                    if form.is_valid() and form.has_changed():
                        child = form.save(commit=False)
                        child.portofolio = porto_instance
                        child.save()

                for form in formset4:
                    # Not save blank field use has_changed()
                    if form.is_valid() and form.has_changed():
                        child = form.save(commit=False)
                        child.portofolio = porto_instance
                        child.save()

                for form in formset5:
                    # Not save blank field use has_changed()
                    if form.is_valid() and form.has_changed():
                        child = form.save(commit=False)
                        child.portofolio = porto_instance
                        child.save()

                for form in formset6:
                    # Not save blank field use has_changed()
                    if form.is_valid() and form.has_changed():
                        child = form.save(commit=False)
                        child.portofolio = porto_instance
                        child.save()

                messages.success(request, "Registered Successfully !")
                return redirect("portofolio:configurasi")

        else:
            form = PortofolioForm()
            form2 = QuoteForm()
            form3 = ThemeProductForm()
            formset = SpecialInviteFormSet(prefix='invite')
            formset2 = DompetFormSet(prefix='dompet')
            formset3 = MultiImageFormSet(prefix='multiimage')
            formset4 = StoryFormSet(prefix='story')
            formset5 = MultiImageFormSet2(prefix='multiimage2')
            formset6 = AcaraFormSet(prefix='acara')

    else:
        return render(request, 'portofolio/regis_failed.html')

    return render(request, "portofolio/configurasi/register_awal_form.html", {'form': form,
        'form2': form2, 'form3': form3, 'formset': formset, 'formset2': formset2, 'formset3': formset3,
        'formset4': formset4, 'formset5': formset5, 'formset6': formset6})

# Portofolio registration
def register(request, id=None):
    # initiate formset
    StoryFormSet = modelformset_factory(
        Story,
        form=StoryForm,
        formset=BaseRegisterFormSet,
        extra=1,
    )
    SpecialInviteFormSet = modelformset_factory(
        SpecialInvitation,
        form=SpecialInvitationForm,
        formset=BaseRegisterFormSet,
        extra=1,
    )
    DompetFormSet = modelformset_factory(
        Dompet,
        form=DompetForm,
        formset=BaseRegisterFormSet,
        extra=1,
    )
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

    AcaraFormSet = modelformset_factory(
        Acara,
        form=AcaraForm,
        formset=BaseRegisterFormSet,
        extra=1,
    )

    portofolio = Portofolio.objects.filter(user=request.user).exists()
    if portofolio == False:
        if request.method == "POST":
            form = PortofolioForm(request.POST or None, request.FILES)
            form2 = QuoteForm(request.POST or None, request.FILES)
            form3 = ThemeProductForm(request.POST or None, request.FILES)

            formset = SpecialInviteFormSet(request.POST or None, prefix='invite')
            formset2 = DompetFormSet(request.POST or None, prefix='dompet')
            formset3 = MultiImageFormSet(request.POST or None, request.FILES, prefix='multiimage')
            formset4 = StoryFormSet(request.POST or None, request.FILES, prefix='story')
            formset5 = MultiImageFormSet2(request.POST or None, request.FILES, prefix='multiimage2')
            formset6 = AcaraFormSet(request.POST or None, request.FILES, prefix='acara')
            print(request.POST)
            # form validation
            if form.is_valid() and form2.is_valid() and form3.is_valid() and formset.is_valid() \
                and formset2.is_valid() and formset4.is_valid():
                # create portofolio instance
                instance = form.save(commit=False)
                # save user to porto
                user = request.user
                instance.user = user
                # save porto field ke field calender
                instance.name = instance.porto_name
                instance.location = instance.location_countdown
                instance.startDate = instance.tanggal_countdown
                instance.startTime = instance.waktu_countdown
                instance.endTime = instance.waktu_countdown_selesai
                # save porto field ke field go to
                instance.lokasi = instance.location_countdown


                instance.save()

                # to create multiple image instance
                porto_instance = Portofolio.objects.get(pk=instance.pk)

                # to create instance quote
                instance_quote = form2.save(commit=False)
                instance_quote.portofolio = porto_instance
                instance_quote.save()

                # to create theme product
                instance_order = Order.objects.get(user=user)
                instance_orderitem = OrderItem.objects.get(order=instance_order)

                instance_orderitem = form3.save(commit=False)
                instance_orderitem.portofolio = porto_instance
                instance_orderitem.fitur = instance_orderitem.fitur
                instance_orderitem.save()

                # to create multiple value instance
                for form in formset:
                    # Not save blank field use has_changed()
                    if form.is_valid() and form.has_changed():
                        child = form.save(commit=False)
                        child.portofolio = porto_instance
                        child.save()

                for form in formset2:
                    # Not save blank field use has_changed()
                    if form.is_valid() and form.has_changed():
                        child = form.save(commit=False)
                        child.portofolio = porto_instance
                        child.save()

                for form in formset3:
                    # Not save blank field use has_changed()
                    if form.is_valid() and form.has_changed():
                        child = form.save(commit=False)
                        child.portofolio = porto_instance
                        child.save()

                for form in formset4:
                    # Not save blank field use has_changed()
                    if form.is_valid() and form.has_changed():
                        child = form.save(commit=False)
                        child.portofolio = porto_instance
                        child.save()

                for form in formset5:
                    # Not save blank field use has_changed()
                    if form.is_valid() and form.has_changed():
                        child = form.save(commit=False)
                        child.portofolio = porto_instance
                        child.save()

                for form in formset6:
                    # Not save blank field use has_changed()
                    if form.is_valid() and form.has_changed():
                        child = form.save(commit=False)
                        child.portofolio = porto_instance
                        child.save()

                messages.success(request, "Registered Successfully !")
                return redirect("portofolio:configurasi")

            else:
                return render(request, "portofolio/register_porto.html", {'form': form,
                    'form2': form2, 'form3': form3, 'formset': formset, 'formset2': formset2, 'formset3': formset3,
                    'formset4': formset4, 'formset5': formset5, 'formset6': formset6})

        else:
            form = PortofolioForm()
            form2 = QuoteForm()
            form3 = ThemeProductForm()
            formset = SpecialInviteFormSet(prefix='invite')
            formset2 = DompetFormSet(prefix='dompet')
            formset3 = MultiImageFormSet(prefix='multiimage')
            formset4 = StoryFormSet(prefix='story')
            formset5 = MultiImageFormSet2(prefix='multiimage2')
            formset6 = AcaraFormSet(prefix='acara')

    else:
        return render(request, 'portofolio/regis_failed.html')

    return render(request, "portofolio/register_porto.html", {'form': form,
        'form2': form2, 'form3': form3, 'formset': formset, 'formset2': formset2, 'formset3': formset3,
        'formset4': formset4, 'formset5': formset5, 'formset6': formset6})

def theme_update(request, slug):
    # get instance portofolio from id
    obj = get_object_or_404(Portofolio, slug=slug)
    # quote instance by porto id
    obj_quote = get_object_or_404(Quote, portofolio= obj)
    # theme product instance by porto id
    obj_themeproduct = get_object_or_404(ThemeProduct, portofolio= obj)

    # Create formset factory, tidak menggunakan base formset agar menampilkan object instance
    SpecialInviteFormSet = modelformset_factory(
        SpecialInvitation,
        form=SpecialInvitationForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    DompetFormSet = modelformset_factory(
        Dompet,
        form=DompetForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    MultiImageFormSet = modelformset_factory(
        MultiImage,
        form=MultiImageForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    StoryFormSet = modelformset_factory(
        Story,
        form=StoryForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    MultiImageFormSet2 = modelformset_factory(
        MultiImage,
        form=MultiImageForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    AcaraFormSet = modelformset_factory(
        Acara,
        form=AcaraForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )

    # create query set for specialinvitation
    qs = SpecialInvitation.objects.filter(portofolio=obj)
    # create query set for dompet
    qs2 = Dompet.objects.filter(portofolio=obj)
    # create query set for multi image
    qs3 = MultiImage.objects.filter(portofolio=obj)
    # create query set for story
    qs4 = Story.objects.filter(portofolio=obj)
    # create query set for acara
    qs5 = Acara.objects.filter(portofolio=obj)

    # Define formset
    formset = SpecialInviteFormSet(request.POST or None,queryset= qs, prefix='invite')
    formset2 = DompetFormSet(request.POST or None,queryset= qs2, prefix='dompet')
    formset3 = MultiImageFormSet(request.POST or None, request.FILES, queryset= qs3, prefix='multiimage')
    formset4 = StoryFormSet(request.POST or None, request.FILES, queryset=qs4, prefix='story')
    formset5 = MultiImageFormSet2(request.POST or None, request.FILES, queryset=qs3, prefix='multiimage2')
    formset6 = AcaraFormSet(request.POST or None, request.FILES, queryset=qs5, prefix='acara')

    if request.method == "POST":
        form = PortofolioForm(request.POST or None, request.FILES, instance=obj)
        form2 = QuoteForm(request.POST or None, request.FILES, instance=obj_quote)
        form3 = ThemeProductForm(request.POST or None, request.FILES, instance=obj_themeproduct)

        if form.is_valid() and form2.is_valid() and form3.is_valid() and formset.is_valid() \
            and formset2.is_valid() and formset4.is_valid():
            # create portofolio instance
            instance = form.save(commit=False)
            # save user to porto
            user = request.user
            print(user)
            instance.user = user
            # save porto field ke field calender
            instance.name = instance.porto_name
            instance.location =  instance.location_countdown
            instance.startDate = instance.tanggal_countdown
            instance.startTime = instance.waktu_countdown
            instance.endTime = instance.waktu_countdown_selesai
            # save porto field ke field go to
            instance.lokasi = instance.location_countdown


            instance.save()

            # to create multiple image instance
            porto_instance = Portofolio.objects.get(pk=instance.pk)

            # to create instance quote
            instance_quote = form2.save(commit=False)
            instance_quote.portofolio = porto_instance
            instance_quote.save()

            # to create theme product
            instance_order = Order.objects.get(user=user)
            instance_orderitemfiture = OrderItem.objects.get(order=instance_order)

            instance_orderitem = form3.save(commit=False)
            instance_orderitem.portofolio = porto_instance
            instance_orderitem.fitur = instance_orderitemfiture.product
            instance_orderitem.save()

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

            messages.success(request, "Data saved!")
            return redirect("portofolio:configurasi")

    else:
        form = PortofolioForm(instance=obj)
        form2 = QuoteForm(instance=obj_quote)
        form3 = ThemeProductForm(instance=obj_themeproduct)
        formset = SpecialInviteFormSet(queryset= qs, prefix='invite')
        formset2 = DompetFormSet(queryset= qs2, prefix='dompet')
        formset3 = MultiImageFormSet(queryset= qs3, prefix='multiimage')
        formset4 = StoryFormSet(queryset=qs4, prefix='story')
        formset5 = MultiImageFormSet2(queryset=qs3, prefix='multiimage2')
        formset6 = AcaraFormSet(queryset=qs5, prefix='acara')


    context = {
        'form': form,
        'form2': form2,
        'form3': form3,
        'formset': formset,
        'formset2': formset2,
        'formset3': formset3,
        'formset4': formset4,
        'formset5': formset5,
        'formset6': formset6
    }

    # return redirect("portofolio:update_tampilan", slug=slug)
    return render(request, 'portofolio/configurasi/tampilan_form.html', context)

def cover_update(request, slug):
    # get instance portofolio from id
    obj = get_object_or_404(Portofolio, slug=slug)
    # quote instance by porto id
    obj_quote = get_object_or_404(Quote, portofolio= obj)
    # theme product instance by porto id
    obj_themeproduct = get_object_or_404(ThemeProduct, portofolio= obj)

    # Create formset factory, tidak menggunakan base formset agar menampilkan object instance
    SpecialInviteFormSet = modelformset_factory(
        SpecialInvitation,
        form=SpecialInvitationForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    DompetFormSet = modelformset_factory(
        Dompet,
        form=DompetForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    MultiImageFormSet = modelformset_factory(
        MultiImage,
        form=MultiImageForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    StoryFormSet = modelformset_factory(
        Story,
        form=StoryForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    MultiImageFormSet2 = modelformset_factory(
        MultiImage,
        form=MultiImageForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    AcaraFormSet = modelformset_factory(
        Acara,
        form=AcaraForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )

    # create query set for specialinvitation
    qs = SpecialInvitation.objects.filter(portofolio=obj)
    # create query set for dompet
    qs2 = Dompet.objects.filter(portofolio=obj)
    # create query set for multi image
    qs3 = MultiImage.objects.filter(portofolio=obj)
    # create query set for story
    qs4 = Story.objects.filter(portofolio=obj)
    # create query set for acara
    qs5 = Acara.objects.filter(portofolio=obj)

    # Define formset
    formset = SpecialInviteFormSet(request.POST or None,queryset= qs, prefix='invite')
    formset2 = DompetFormSet(request.POST or None,queryset= qs2, prefix='dompet')
    formset3 = MultiImageFormSet(request.POST or None, request.FILES, queryset= qs3, prefix='multiimage')
    formset4 = StoryFormSet(request.POST or None, request.FILES, queryset=qs4, prefix='story')
    formset5 = MultiImageFormSet2(request.POST or None, request.FILES, queryset=qs3, prefix='multiimage2')
    formset6 = AcaraFormSet(request.POST or None, request.FILES, queryset=qs5, prefix='acara')

    if request.method == "POST":
        form = PortofolioForm(request.POST or None, request.FILES, instance=obj)
        form2 = QuoteForm(request.POST or None, request.FILES, instance=obj_quote)
        form3 = ThemeProductForm(request.POST or None, request.FILES, instance=obj_themeproduct)

        if form.is_valid() and form2.is_valid() and form3.is_valid() and formset.is_valid() \
            and formset2.is_valid() and formset4.is_valid():
            # create portofolio instance
            instance = form.save(commit=False)
            # save user to porto
            user = request.user
            print(user)
            instance.user = user
            # save porto field ke field calender
            instance.name = instance.porto_name
            instance.location =  instance.location_countdown
            instance.startDate = instance.tanggal_countdown
            instance.startTime = instance.waktu_countdown
            instance.endTime = instance.waktu_countdown_selesai
            # save porto field ke field go to
            instance.lokasi = instance.location_countdown


            instance.save()

            # to create multiple image instance
            porto_instance = Portofolio.objects.get(pk=instance.pk)

            # to create instance quote
            instance_quote = form2.save(commit=False)
            instance_quote.portofolio = porto_instance
            instance_quote.save()

            # to create theme product
            instance_order = Order.objects.get(user=user)
            instance_orderitemfiture = OrderItem.objects.get(order=instance_order)

            instance_orderitem = form3.save(commit=False)
            instance_orderitem.portofolio = porto_instance
            instance_orderitem.fitur = instance_orderitemfiture.product
            instance_orderitem.save()

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

            messages.success(request, "Data saved!")
            return redirect("portofolio:configurasi")

    else:
        form = PortofolioForm(instance=obj)
        form2 = QuoteForm(instance=obj_quote)
        form3 = ThemeProductForm(instance=obj_themeproduct)
        formset = SpecialInviteFormSet(queryset= qs, prefix='invite')
        formset2 = DompetFormSet(queryset= qs2, prefix='dompet')
        formset3 = MultiImageFormSet(queryset= qs3, prefix='multiimage')
        formset4 = StoryFormSet(queryset=qs4, prefix='story')
        formset5 = MultiImageFormSet2(queryset=qs3, prefix='multiimage2')
        formset6 = AcaraFormSet(queryset=qs5, prefix='acara')


    context = {
        'form': form,
        'form2': form2,
        'form3': form3,
        'formset': formset,
        'formset2': formset2,
        'formset3': formset3,
        'formset4': formset4,
        'formset5': formset5,
        'formset6': formset6
    }

    # return redirect("portofolio:update_tampilan", slug=slug)
    return render(request, 'portofolio/configurasi/cover_form.html', context)

def pasangan_update(request, slug):
    # get instance portofolio from id
    obj = get_object_or_404(Portofolio, slug=slug)
    # quote instance by porto id
    obj_quote = get_object_or_404(Quote, portofolio= obj)
    # theme product instance by porto id
    obj_themeproduct = get_object_or_404(ThemeProduct, portofolio= obj)

    # Create formset factory, tidak menggunakan base formset agar menampilkan object instance
    SpecialInviteFormSet = modelformset_factory(
        SpecialInvitation,
        form=SpecialInvitationForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    DompetFormSet = modelformset_factory(
        Dompet,
        form=DompetForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    MultiImageFormSet = modelformset_factory(
        MultiImage,
        form=MultiImageForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    StoryFormSet = modelformset_factory(
        Story,
        form=StoryForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    MultiImageFormSet2 = modelformset_factory(
        MultiImage,
        form=MultiImageForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    AcaraFormSet = modelformset_factory(
        Acara,
        form=AcaraForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )

    # create query set for specialinvitation
    qs = SpecialInvitation.objects.filter(portofolio=obj)
    # create query set for dompet
    qs2 = Dompet.objects.filter(portofolio=obj)
    # create query set for multi image
    qs3 = MultiImage.objects.filter(portofolio=obj)
    # create query set for story
    qs4 = Story.objects.filter(portofolio=obj)
    # create query set for acara
    qs5 = Acara.objects.filter(portofolio=obj)

    # Define formset
    formset = SpecialInviteFormSet(request.POST or None,queryset= qs, prefix='invite')
    formset2 = DompetFormSet(request.POST or None,queryset= qs2, prefix='dompet')
    formset3 = MultiImageFormSet(request.POST or None, request.FILES, queryset= qs3, prefix='multiimage')
    formset4 = StoryFormSet(request.POST or None, request.FILES, queryset=qs4, prefix='story')
    formset5 = MultiImageFormSet2(request.POST or None, request.FILES, queryset=qs3, prefix='multiimage2')
    formset6 = AcaraFormSet(request.POST or None, request.FILES, queryset=qs5, prefix='acara')

    if request.method == "POST":
        form = PortofolioForm(request.POST or None, request.FILES, instance=obj)
        form2 = QuoteForm(request.POST or None, request.FILES, instance=obj_quote)
        form3 = ThemeProductForm(request.POST or None, request.FILES, instance=obj_themeproduct)

        if form.is_valid() and form2.is_valid() and form3.is_valid() and formset.is_valid() \
            and formset2.is_valid() and formset4.is_valid():
            # create portofolio instance
            instance = form.save(commit=False)
            # save user to porto
            user = request.user
            print(user)
            instance.user = user
            # save porto field ke field calender
            instance.name = instance.porto_name
            instance.location =  instance.location_countdown
            instance.startDate = instance.tanggal_countdown
            instance.startTime = instance.waktu_countdown
            instance.endTime = instance.waktu_countdown_selesai
            # save porto field ke field go to
            instance.lokasi = instance.location_countdown


            instance.save()

            # to create multiple image instance
            porto_instance = Portofolio.objects.get(pk=instance.pk)

            # to create instance quote
            instance_quote = form2.save(commit=False)
            instance_quote.portofolio = porto_instance
            instance_quote.save()

            # to create theme product
            instance_order = Order.objects.get(user=user)
            instance_orderitemfiture = OrderItem.objects.get(order=instance_order)

            instance_orderitem = form3.save(commit=False)
            instance_orderitem.portofolio = porto_instance
            instance_orderitem.fitur = instance_orderitemfiture.product
            instance_orderitem.save()

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

            messages.success(request, "Data saved!")
            return redirect("portofolio:configurasi")

    else:
        form = PortofolioForm(instance=obj)
        form2 = QuoteForm(instance=obj_quote)
        form3 = ThemeProductForm(instance=obj_themeproduct)
        formset = SpecialInviteFormSet(queryset= qs, prefix='invite')
        formset2 = DompetFormSet(queryset= qs2, prefix='dompet')
        formset3 = MultiImageFormSet(queryset= qs3, prefix='multiimage')
        formset4 = StoryFormSet(queryset=qs4, prefix='story')
        formset5 = MultiImageFormSet2(queryset=qs3, prefix='multiimage2')
        formset6 = AcaraFormSet(queryset=qs5, prefix='acara')


    context = {
        'form': form,
        'form2': form2,
        'form3': form3,
        'formset': formset,
        'formset2': formset2,
        'formset3': formset3,
        'formset4': formset4,
        'formset5': formset5,
        'formset6': formset6
    }

    return render(request, 'portofolio/configurasi/pasangan_form.html', context)

def quote_update(request, slug):
    # get instance portofolio from id
    obj = get_object_or_404(Portofolio, slug=slug)
    # quote instance by porto id
    obj_quote = get_object_or_404(Quote, portofolio= obj)
    # theme product instance by porto id
    obj_themeproduct = get_object_or_404(ThemeProduct, portofolio= obj)

    # Create formset factory, tidak menggunakan base formset agar menampilkan object instance
    SpecialInviteFormSet = modelformset_factory(
        SpecialInvitation,
        form=SpecialInvitationForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    DompetFormSet = modelformset_factory(
        Dompet,
        form=DompetForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    MultiImageFormSet = modelformset_factory(
        MultiImage,
        form=MultiImageForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    StoryFormSet = modelformset_factory(
        Story,
        form=StoryForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    MultiImageFormSet2 = modelformset_factory(
        MultiImage,
        form=MultiImageForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    AcaraFormSet = modelformset_factory(
        Acara,
        form=AcaraForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )

    # create query set for specialinvitation
    qs = SpecialInvitation.objects.filter(portofolio=obj)
    # create query set for dompet
    qs2 = Dompet.objects.filter(portofolio=obj)
    # create query set for multi image
    qs3 = MultiImage.objects.filter(portofolio=obj)
    # create query set for story
    qs4 = Story.objects.filter(portofolio=obj)
    # create query set for acara
    qs5 = Acara.objects.filter(portofolio=obj)

    # Define formset
    formset = SpecialInviteFormSet(request.POST or None,queryset= qs, prefix='invite')
    formset2 = DompetFormSet(request.POST or None,queryset= qs2, prefix='dompet')
    formset3 = MultiImageFormSet(request.POST or None, request.FILES, queryset= qs3, prefix='multiimage')
    formset4 = StoryFormSet(request.POST or None, request.FILES, queryset=qs4, prefix='story')
    formset5 = MultiImageFormSet2(request.POST or None, request.FILES, queryset=qs3, prefix='multiimage2')
    formset6 = AcaraFormSet(request.POST or None, request.FILES, queryset=qs5, prefix='acara')

    if request.method == "POST":
        form = PortofolioForm(request.POST or None, request.FILES, instance=obj)
        form2 = QuoteForm(request.POST or None, request.FILES, instance=obj_quote)
        form3 = ThemeProductForm(request.POST or None, request.FILES, instance=obj_themeproduct)

        if form.is_valid() and form2.is_valid() and form3.is_valid() and formset.is_valid() \
            and formset2.is_valid() and formset4.is_valid():
            # create portofolio instance
            instance = form.save(commit=False)
            # save user to porto
            user = request.user
            print(user)
            instance.user = user
            # save porto field ke field calender
            instance.name = instance.porto_name
            instance.location =  instance.location_countdown
            instance.startDate = instance.tanggal_countdown
            instance.startTime = instance.waktu_countdown
            instance.endTime = instance.waktu_countdown_selesai
            # save porto field ke field go to
            instance.lokasi = instance.location_countdown


            instance.save()

            # to create multiple image instance
            porto_instance = Portofolio.objects.get(pk=instance.pk)

            # to create instance quote
            instance_quote = form2.save(commit=False)
            instance_quote.portofolio = porto_instance
            instance_quote.save()

            # to create theme product
            instance_order = Order.objects.get(user=user)
            instance_orderitemfiture = OrderItem.objects.get(order=instance_order)

            instance_orderitem = form3.save(commit=False)
            instance_orderitem.portofolio = porto_instance
            instance_orderitem.fitur = instance_orderitemfiture.product
            instance_orderitem.save()

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

            messages.success(request, "Data saved!")
            return redirect("portofolio:configurasi")

    else:
        form = PortofolioForm(instance=obj)
        form2 = QuoteForm(instance=obj_quote)
        form3 = ThemeProductForm(instance=obj_themeproduct)
        formset = SpecialInviteFormSet(queryset= qs, prefix='invite')
        formset2 = DompetFormSet(queryset= qs2, prefix='dompet')
        formset3 = MultiImageFormSet(queryset= qs3, prefix='multiimage')
        formset4 = StoryFormSet(queryset=qs4, prefix='story')
        formset5 = MultiImageFormSet2(queryset=qs3, prefix='multiimage2')
        formset6 = AcaraFormSet(queryset=qs5, prefix='acara')


    context = {
        'form': form,
        'form2': form2,
        'form3': form3,
        'formset': formset,
        'formset2': formset2,
        'formset3': formset3,
        'formset4': formset4,
        'formset5': formset5,
        'formset6': formset6
    }

    # return redirect("portofolio:update_tampilan", slug=slug)
    return render(request, 'portofolio/configurasi/quote_form.html', context)

def acara_update(request, slug):
    # get instance portofolio from id
    obj = get_object_or_404(Portofolio, slug=slug)
    # quote instance by porto id
    obj_quote = get_object_or_404(Quote, portofolio= obj)
    # theme product instance by porto id
    obj_themeproduct = get_object_or_404(ThemeProduct, portofolio= obj)

    # Create formset factory, tidak menggunakan base formset agar menampilkan object instance
    SpecialInviteFormSet = modelformset_factory(
        SpecialInvitation,
        form=SpecialInvitationForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    DompetFormSet = modelformset_factory(
        Dompet,
        form=DompetForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    MultiImageFormSet = modelformset_factory(
        MultiImage,
        form=MultiImageForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    StoryFormSet = modelformset_factory(
        Story,
        form=StoryForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    MultiImageFormSet2 = modelformset_factory(
        MultiImage,
        form=MultiImageForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    AcaraFormSet = modelformset_factory(
        Acara,
        form=AcaraForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )

    # create query set for specialinvitation
    qs = SpecialInvitation.objects.filter(portofolio=obj)
    # create query set for dompet
    qs2 = Dompet.objects.filter(portofolio=obj)
    # create query set for multi image
    qs3 = MultiImage.objects.filter(portofolio=obj)
    # create query set for story
    qs4 = Story.objects.filter(portofolio=obj)
    # create query set for acara
    qs5 = Acara.objects.filter(portofolio=obj)

    # Define formset
    formset = SpecialInviteFormSet(request.POST or None,queryset= qs, prefix='invite')
    formset2 = DompetFormSet(request.POST or None,queryset= qs2, prefix='dompet')
    formset3 = MultiImageFormSet(request.POST or None, request.FILES, queryset= qs3, prefix='multiimage')
    formset4 = StoryFormSet(request.POST or None, request.FILES, queryset=qs4, prefix='story')
    formset5 = MultiImageFormSet2(request.POST or None, request.FILES, queryset=qs3, prefix='multiimage2')
    formset6 = AcaraFormSet(request.POST or None, request.FILES, queryset=qs5, prefix='acara')

    if request.method == "POST":
        form = PortofolioForm(request.POST or None, request.FILES, instance=obj)
        form2 = QuoteForm(request.POST or None, request.FILES, instance=obj_quote)
        form3 = ThemeProductForm(request.POST or None, request.FILES, instance=obj_themeproduct)

        if form.is_valid() and form2.is_valid() and form3.is_valid() and formset.is_valid() \
            and formset2.is_valid() and formset4.is_valid():
            # create portofolio instance
            instance = form.save(commit=False)
            # save user to porto
            user = request.user
            print(user)
            instance.user = user
            # save porto field ke field calender
            instance.name = instance.porto_name
            instance.location =  instance.location_countdown
            instance.startDate = instance.tanggal_countdown
            instance.startTime = instance.waktu_countdown
            instance.endTime = instance.waktu_countdown_selesai
            # save porto field ke field go to
            instance.lokasi = instance.location_countdown


            instance.save()

            # to create multiple image instance
            porto_instance = Portofolio.objects.get(pk=instance.pk)

            # to create instance quote
            instance_quote = form2.save(commit=False)
            instance_quote.portofolio = porto_instance
            instance_quote.save()

            # to create theme product
            instance_order = Order.objects.get(user=user)
            instance_orderitemfiture = OrderItem.objects.get(order=instance_order)

            instance_orderitem = form3.save(commit=False)
            instance_orderitem.portofolio = porto_instance
            instance_orderitem.fitur = instance_orderitemfiture.product
            instance_orderitem.save()

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

            messages.success(request, "Data saved!")
            return redirect("portofolio:configurasi")

    else:
        form = PortofolioForm(instance=obj)
        form2 = QuoteForm(instance=obj_quote)
        form3 = ThemeProductForm(instance=obj_themeproduct)
        formset = SpecialInviteFormSet(queryset= qs, prefix='invite')
        formset2 = DompetFormSet(queryset= qs2, prefix='dompet')
        formset3 = MultiImageFormSet(queryset= qs3, prefix='multiimage')
        formset4 = StoryFormSet(queryset=qs4, prefix='story')
        formset5 = MultiImageFormSet2(queryset=qs3, prefix='multiimage2')
        formset6 = AcaraFormSet(queryset=qs5, prefix='acara')


    context = {
        'form': form,
        'form2': form2,
        'form3': form3,
        'formset': formset,
        'formset2': formset2,
        'formset3': formset3,
        'formset4': formset4,
        'formset5': formset5,
        'formset6': formset6
    }
    # return redirect("portofolio:update_tampilan", slug=slug)
    return render(request, 'portofolio/configurasi/acara_form.html', context)

def moment_update(request, slug):
    # get instance portofolio from id
    obj = get_object_or_404(Portofolio, slug=slug)
    # quote instance by porto id
    obj_quote = get_object_or_404(Quote, portofolio= obj)
    # theme product instance by porto id
    obj_themeproduct = get_object_or_404(ThemeProduct, portofolio= obj)

    # Create formset factory, tidak menggunakan base formset agar menampilkan object instance
    SpecialInviteFormSet = modelformset_factory(
        SpecialInvitation,
        form=SpecialInvitationForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    DompetFormSet = modelformset_factory(
        Dompet,
        form=DompetForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    MultiImageFormSet = modelformset_factory(
        MultiImage,
        form=MultiImageForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    StoryFormSet = modelformset_factory(
        Story,
        form=StoryForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    MultiImageFormSet2 = modelformset_factory(
        MultiImage,
        form=MultiImageForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    AcaraFormSet = modelformset_factory(
        Acara,
        form=AcaraForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )

    # create query set for specialinvitation
    qs = SpecialInvitation.objects.filter(portofolio=obj)
    # create query set for dompet
    qs2 = Dompet.objects.filter(portofolio=obj)
    # create query set for multi image
    qs3 = MultiImage.objects.filter(portofolio=obj)
    # create query set for story
    qs4 = Story.objects.filter(portofolio=obj)
    # create query set for acara
    qs5 = Acara.objects.filter(portofolio=obj)

    # Define formset
    formset = SpecialInviteFormSet(request.POST or None,queryset= qs, prefix='invite')
    formset2 = DompetFormSet(request.POST or None,queryset= qs2, prefix='dompet')
    formset3 = MultiImageFormSet(request.POST or None, request.FILES, queryset= qs3, prefix='multiimage')
    formset4 = StoryFormSet(request.POST or None, request.FILES, queryset=qs4, prefix='story')
    formset5 = MultiImageFormSet2(request.POST or None, request.FILES, queryset=qs3, prefix='multiimage2')
    formset6 = AcaraFormSet(request.POST or None, request.FILES, queryset=qs5, prefix='acara')

    if request.method == "POST":
        form = PortofolioForm(request.POST or None, request.FILES, instance=obj)
        form2 = QuoteForm(request.POST or None, request.FILES, instance=obj_quote)
        form3 = ThemeProductForm(request.POST or None, request.FILES, instance=obj_themeproduct)

        if form.is_valid() and form2.is_valid() and form3.is_valid() and formset.is_valid() \
            and formset2.is_valid() and formset4.is_valid():
            # create portofolio instance
            instance = form.save(commit=False)
            # save user to porto
            user = request.user
            print(user)
            instance.user = user
            # save porto field ke field calender
            instance.name = instance.porto_name
            instance.location =  instance.location_countdown
            instance.startDate = instance.tanggal_countdown
            instance.startTime = instance.waktu_countdown
            instance.endTime = instance.waktu_countdown_selesai
            # save porto field ke field go to
            instance.lokasi = instance.location_countdown


            instance.save()

            # to create multiple image instance
            porto_instance = Portofolio.objects.get(pk=instance.pk)

            # to create instance quote
            instance_quote = form2.save(commit=False)
            instance_quote.portofolio = porto_instance
            instance_quote.save()

            # to create theme product
            instance_order = Order.objects.get(user=user)
            instance_orderitemfiture = OrderItem.objects.get(order=instance_order)

            instance_orderitem = form3.save(commit=False)
            instance_orderitem.portofolio = porto_instance
            instance_orderitem.fitur = instance_orderitemfiture.product
            instance_orderitem.save()

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

            messages.success(request, "Data saved!")
            return redirect("portofolio:configurasi")

    else:
        form = PortofolioForm(instance=obj)
        form2 = QuoteForm(instance=obj_quote)
        form3 = ThemeProductForm(instance=obj_themeproduct)
        formset = SpecialInviteFormSet(queryset= qs, prefix='invite')
        formset2 = DompetFormSet(queryset= qs2, prefix='dompet')
        formset3 = MultiImageFormSet(queryset= qs3, prefix='multiimage')
        formset4 = StoryFormSet(queryset=qs4, prefix='story')
        formset5 = MultiImageFormSet2(queryset=qs3, prefix='multiimage2')
        formset6 = AcaraFormSet(queryset=qs5, prefix='acara')


    context = {
        'form': form,
        'form2': form2,
        'form3': form3,
        'formset': formset,
        'formset2': formset2,
        'formset3': formset3,
        'formset4': formset4,
        'formset5': formset5,
        'formset6': formset6
    }

    # return redirect("portofolio:update_tampilan", slug=slug)
    return render(request, 'portofolio/configurasi/moment_form.html', context)

def stories_update(request, slug):
    # get instance portofolio from id
    obj = get_object_or_404(Portofolio, slug=slug)
    # quote instance by porto id
    obj_quote = get_object_or_404(Quote, portofolio= obj)
    # theme product instance by porto id
    obj_themeproduct = get_object_or_404(ThemeProduct, portofolio= obj)

    # Create formset factory, tidak menggunakan base formset agar menampilkan object instance
    SpecialInviteFormSet = modelformset_factory(
        SpecialInvitation,
        form=SpecialInvitationForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    DompetFormSet = modelformset_factory(
        Dompet,
        form=DompetForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    MultiImageFormSet = modelformset_factory(
        MultiImage,
        form=MultiImageForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    StoryFormSet = modelformset_factory(
        Story,
        form=StoryForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    MultiImageFormSet2 = modelformset_factory(
        MultiImage,
        form=MultiImageForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    AcaraFormSet = modelformset_factory(
        Acara,
        form=AcaraForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )

    # create query set for specialinvitation
    qs = SpecialInvitation.objects.filter(portofolio=obj)
    # create query set for dompet
    qs2 = Dompet.objects.filter(portofolio=obj)
    # create query set for multi image
    qs3 = MultiImage.objects.filter(portofolio=obj)
    # create query set for story
    qs4 = Story.objects.filter(portofolio=obj)
    # create query set for acara
    qs5 = Acara.objects.filter(portofolio=obj)

    # Define formset
    formset = SpecialInviteFormSet(request.POST or None,queryset= qs, prefix='invite')
    formset2 = DompetFormSet(request.POST or None,queryset= qs2, prefix='dompet')
    formset3 = MultiImageFormSet(request.POST or None, request.FILES, queryset= qs3, prefix='multiimage')
    formset4 = StoryFormSet(request.POST or None, request.FILES, queryset=qs4, prefix='story')
    formset5 = MultiImageFormSet2(request.POST or None, request.FILES, queryset=qs3, prefix='multiimage2')
    formset6 = AcaraFormSet(request.POST or None, request.FILES, queryset=qs5, prefix='acara')

    if request.method == "POST":
        form = PortofolioForm(request.POST or None, request.FILES, instance=obj)
        form2 = QuoteForm(request.POST or None, request.FILES, instance=obj_quote)
        form3 = ThemeProductForm(request.POST or None, request.FILES, instance=obj_themeproduct)

        if form.is_valid() and form2.is_valid() and form3.is_valid() and formset.is_valid() \
            and formset2.is_valid() and formset4.is_valid():
            # create portofolio instance
            instance = form.save(commit=False)
            # save user to porto
            user = request.user
            print(user)
            instance.user = user
            # save porto field ke field calender
            instance.name = instance.porto_name
            instance.location =  instance.location_countdown
            instance.startDate = instance.tanggal_countdown
            instance.startTime = instance.waktu_countdown
            instance.endTime = instance.waktu_countdown_selesai
            # save porto field ke field go to
            instance.lokasi = instance.location_countdown


            instance.save()

            # to create multiple image instance
            porto_instance = Portofolio.objects.get(pk=instance.pk)

            # to create instance quote
            instance_quote = form2.save(commit=False)
            instance_quote.portofolio = porto_instance
            instance_quote.save()

            # to create theme product
            instance_order = Order.objects.get(user=user)
            instance_orderitemfiture = OrderItem.objects.get(order=instance_order)

            instance_orderitem = form3.save(commit=False)
            instance_orderitem.portofolio = porto_instance
            instance_orderitem.fitur = instance_orderitemfiture.product
            instance_orderitem.save()

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

            messages.success(request, "Data saved!")
            return redirect("portofolio:configurasi")

    else:
        form = PortofolioForm(instance=obj)
        form2 = QuoteForm(instance=obj_quote)
        form3 = ThemeProductForm(instance=obj_themeproduct)
        formset = SpecialInviteFormSet(queryset= qs, prefix='invite')
        formset2 = DompetFormSet(queryset= qs2, prefix='dompet')
        formset3 = MultiImageFormSet(queryset= qs3, prefix='multiimage')
        formset4 = StoryFormSet(queryset=qs4, prefix='story')
        formset5 = MultiImageFormSet2(queryset=qs3, prefix='multiimage2')
        formset6 = AcaraFormSet(queryset=qs5, prefix='acara')


    context = {
        'form': form,
        'form2': form2,
        'form3': form3,
        'formset': formset,
        'formset2': formset2,
        'formset3': formset3,
        'formset4': formset4,
        'formset5': formset5,
        'formset6': formset6
    }
    # return redirect("portofolio:update_tampilan", slug=slug)
    return render(request, 'portofolio/configurasi/story_form.html', context)

def map_update(request, slug):
    # get instance portofolio from id
    obj = get_object_or_404(Portofolio, slug=slug)
    # quote instance by porto id
    obj_quote = get_object_or_404(Quote, portofolio= obj)
    # theme product instance by porto id
    obj_themeproduct = get_object_or_404(ThemeProduct, portofolio= obj)

    # Create formset factory, tidak menggunakan base formset agar menampilkan object instance
    SpecialInviteFormSet = modelformset_factory(
        SpecialInvitation,
        form=SpecialInvitationForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    DompetFormSet = modelformset_factory(
        Dompet,
        form=DompetForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    MultiImageFormSet = modelformset_factory(
        MultiImage,
        form=MultiImageForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    StoryFormSet = modelformset_factory(
        Story,
        form=StoryForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    MultiImageFormSet2 = modelformset_factory(
        MultiImage,
        form=MultiImageForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    AcaraFormSet = modelformset_factory(
        Acara,
        form=AcaraForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )

    # create query set for specialinvitation
    qs = SpecialInvitation.objects.filter(portofolio=obj)
    # create query set for dompet
    qs2 = Dompet.objects.filter(portofolio=obj)
    # create query set for multi image
    qs3 = MultiImage.objects.filter(portofolio=obj)
    # create query set for story
    qs4 = Story.objects.filter(portofolio=obj)
    # create query set for acara
    qs5 = Acara.objects.filter(portofolio=obj)

    # Define formset
    formset = SpecialInviteFormSet(request.POST or None,queryset= qs, prefix='invite')
    formset2 = DompetFormSet(request.POST or None,queryset= qs2, prefix='dompet')
    formset3 = MultiImageFormSet(request.POST or None, request.FILES, queryset= qs3, prefix='multiimage')
    formset4 = StoryFormSet(request.POST or None, request.FILES, queryset=qs4, prefix='story')
    formset5 = MultiImageFormSet2(request.POST or None, request.FILES, queryset=qs3, prefix='multiimage2')
    formset6 = AcaraFormSet(request.POST or None, request.FILES, queryset=qs5, prefix='acara')

    if request.method == "POST":
        form = PortofolioForm(request.POST or None, request.FILES, instance=obj)
        form2 = QuoteForm(request.POST or None, request.FILES, instance=obj_quote)
        form3 = ThemeProductForm(request.POST or None, request.FILES, instance=obj_themeproduct)

        if form.is_valid() and form2.is_valid() and form3.is_valid() and formset.is_valid() \
            and formset2.is_valid() and formset4.is_valid():
            # create portofolio instance
            instance = form.save(commit=False)
            # save user to porto
            user = request.user
            print(user)
            instance.user = user
            # save porto field ke field calender
            instance.name = instance.porto_name
            instance.location =  instance.location_countdown
            instance.startDate = instance.tanggal_countdown
            instance.startTime = instance.waktu_countdown
            instance.endTime = instance.waktu_countdown_selesai
            # save porto field ke field go to
            instance.lokasi = instance.location_countdown


            instance.save()

            # to create multiple image instance
            porto_instance = Portofolio.objects.get(pk=instance.pk)

            # to create instance quote
            instance_quote = form2.save(commit=False)
            instance_quote.portofolio = porto_instance
            instance_quote.save()

            # to create theme product
            instance_order = Order.objects.get(user=user)
            instance_orderitemfiture = OrderItem.objects.get(order=instance_order)

            instance_orderitem = form3.save(commit=False)
            instance_orderitem.portofolio = porto_instance
            instance_orderitem.fitur = instance_orderitemfiture.product
            instance_orderitem.save()

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

            messages.success(request, "Data saved!")
            return redirect("portofolio:configurasi")

    else:
        form = PortofolioForm(instance=obj)
        form2 = QuoteForm(instance=obj_quote)
        form3 = ThemeProductForm(instance=obj_themeproduct)
        formset = SpecialInviteFormSet(queryset= qs, prefix='invite')
        formset2 = DompetFormSet(queryset= qs2, prefix='dompet')
        formset3 = MultiImageFormSet(queryset= qs3, prefix='multiimage')
        formset4 = StoryFormSet(queryset=qs4, prefix='story')
        formset5 = MultiImageFormSet2(queryset=qs3, prefix='multiimage2')
        formset6 = AcaraFormSet(queryset=qs5, prefix='acara')


    context = {
        'form': form,
        'form2': form2,
        'form3': form3,
        'formset': formset,
        'formset2': formset2,
        'formset3': formset3,
        'formset4': formset4,
        'formset5': formset5,
        'formset6': formset6
    }
    # return redirect("portofolio:update_tampilan", slug=slug)
    return render(request, 'portofolio/configurasi/map_form.html', context)

def dompet_update(request, slug):
    # get instance portofolio from id
    obj = get_object_or_404(Portofolio, slug=slug)
    # quote instance by porto id
    obj_quote = get_object_or_404(Quote, portofolio= obj)
    # theme product instance by porto id
    obj_themeproduct = get_object_or_404(ThemeProduct, portofolio= obj)

    # Create formset factory, tidak menggunakan base formset agar menampilkan object instance
    SpecialInviteFormSet = modelformset_factory(
        SpecialInvitation,
        form=SpecialInvitationForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    DompetFormSet = modelformset_factory(
        Dompet,
        form=DompetForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    MultiImageFormSet = modelformset_factory(
        MultiImage,
        form=MultiImageForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    StoryFormSet = modelformset_factory(
        Story,
        form=StoryForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    MultiImageFormSet2 = modelformset_factory(
        MultiImage,
        form=MultiImageForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    AcaraFormSet = modelformset_factory(
        Acara,
        form=AcaraForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )

    # create query set for specialinvitation
    qs = SpecialInvitation.objects.filter(portofolio=obj)
    # create query set for dompet
    qs2 = Dompet.objects.filter(portofolio=obj)
    # create query set for multi image
    qs3 = MultiImage.objects.filter(portofolio=obj)
    # create query set for story
    qs4 = Story.objects.filter(portofolio=obj)
    # create query set for acara
    qs5 = Acara.objects.filter(portofolio=obj)

    # Define formset
    formset = SpecialInviteFormSet(request.POST or None,queryset= qs, prefix='invite')
    formset2 = DompetFormSet(request.POST or None,queryset= qs2, prefix='dompet')
    formset3 = MultiImageFormSet(request.POST or None, request.FILES, queryset= qs3, prefix='multiimage')
    formset4 = StoryFormSet(request.POST or None, request.FILES, queryset=qs4, prefix='story')
    formset5 = MultiImageFormSet2(request.POST or None, request.FILES, queryset=qs3, prefix='multiimage2')
    formset6 = AcaraFormSet(request.POST or None, request.FILES, queryset=qs5, prefix='acara')

    if request.method == "POST":
        form = PortofolioForm(request.POST or None, request.FILES, instance=obj)
        form2 = QuoteForm(request.POST or None, request.FILES, instance=obj_quote)
        form3 = ThemeProductForm(request.POST or None, request.FILES, instance=obj_themeproduct)

        if form.is_valid() and form2.is_valid() and form3.is_valid() and formset.is_valid() \
            and formset2.is_valid() and formset4.is_valid():
            # create portofolio instance
            instance = form.save(commit=False)
            # save user to porto
            user = request.user
            print(user)
            instance.user = user
            # save porto field ke field calender
            instance.name = instance.porto_name
            instance.location =  instance.location_countdown
            instance.startDate = instance.tanggal_countdown
            instance.startTime = instance.waktu_countdown
            instance.endTime = instance.waktu_countdown_selesai
            # save porto field ke field go to
            instance.lokasi = instance.location_countdown


            instance.save()

            # to create multiple image instance
            porto_instance = Portofolio.objects.get(pk=instance.pk)

            # to create instance quote
            instance_quote = form2.save(commit=False)
            instance_quote.portofolio = porto_instance
            instance_quote.save()

            # to create theme product
            instance_order = Order.objects.get(user=user)
            instance_orderitemfiture = OrderItem.objects.get(order=instance_order)

            instance_orderitem = form3.save(commit=False)
            instance_orderitem.portofolio = porto_instance
            instance_orderitem.fitur = instance_orderitemfiture.product
            instance_orderitem.save()

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

            messages.success(request, "Data saved!")
            return redirect("portofolio:configurasi")

    else:
        form = PortofolioForm(instance=obj)
        form2 = QuoteForm(instance=obj_quote)
        form3 = ThemeProductForm(instance=obj_themeproduct)
        formset = SpecialInviteFormSet(queryset= qs, prefix='invite')
        formset2 = DompetFormSet(queryset= qs2, prefix='dompet')
        formset3 = MultiImageFormSet(queryset= qs3, prefix='multiimage')
        formset4 = StoryFormSet(queryset=qs4, prefix='story')
        formset5 = MultiImageFormSet2(queryset=qs3, prefix='multiimage2')
        formset6 = AcaraFormSet(queryset=qs5, prefix='acara')


    context = {
        'form': form,
        'form2': form2,
        'form3': form3,
        'formset': formset,
        'formset2': formset2,
        'formset3': formset3,
        'formset4': formset4,
        'formset5': formset5,
        'formset6': formset6
    }

    # return redirect("portofolio:update_tampilan", slug=slug)
    return render(request, 'portofolio/configurasi/dompet_form.html', context)

def specialinvite_update(request, slug):
    # get instance portofolio from id
    obj = get_object_or_404(Portofolio, slug=slug)
    # quote instance by porto id
    obj_quote = get_object_or_404(Quote, portofolio= obj)
    # theme product instance by porto id
    obj_themeproduct = get_object_or_404(ThemeProduct, portofolio= obj)

    # Create formset factory, tidak menggunakan base formset agar menampilkan object instance
    SpecialInviteFormSet = modelformset_factory(
        SpecialInvitation,
        form=SpecialInvitationForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    DompetFormSet = modelformset_factory(
        Dompet,
        form=DompetForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    MultiImageFormSet = modelformset_factory(
        MultiImage,
        form=MultiImageForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    StoryFormSet = modelformset_factory(
        Story,
        form=StoryForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    MultiImageFormSet2 = modelformset_factory(
        MultiImage,
        form=MultiImageForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    AcaraFormSet = modelformset_factory(
        Acara,
        form=AcaraForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )

    # create query set for specialinvitation
    qs = SpecialInvitation.objects.filter(portofolio=obj)
    # create query set for dompet
    qs2 = Dompet.objects.filter(portofolio=obj)
    # create query set for multi image
    qs3 = MultiImage.objects.filter(portofolio=obj)
    # create query set for story
    qs4 = Story.objects.filter(portofolio=obj)
    # create query set for acara
    qs5 = Acara.objects.filter(portofolio=obj)

    # Define formset
    formset = SpecialInviteFormSet(request.POST or None,queryset= qs, prefix='invite')
    formset2 = DompetFormSet(request.POST or None,queryset= qs2, prefix='dompet')
    formset3 = MultiImageFormSet(request.POST or None, request.FILES, queryset= qs3, prefix='multiimage')
    formset4 = StoryFormSet(request.POST or None, request.FILES, queryset=qs4, prefix='story')
    formset5 = MultiImageFormSet2(request.POST or None, request.FILES, queryset=qs3, prefix='multiimage2')
    formset6 = AcaraFormSet(request.POST or None, request.FILES, queryset=qs5, prefix='acara')

    if request.method == "POST":
        form = PortofolioForm(request.POST or None, request.FILES, instance=obj)
        form2 = QuoteForm(request.POST or None, request.FILES, instance=obj_quote)
        form3 = ThemeProductForm(request.POST or None, request.FILES, instance=obj_themeproduct)

        if form.is_valid() and form2.is_valid() and form3.is_valid() and formset.is_valid() \
            and formset2.is_valid() and formset4.is_valid():
            # create portofolio instance
            instance = form.save(commit=False)
            # save user to porto
            user = request.user
            print(user)
            instance.user = user
            # save porto field ke field calender
            instance.name = instance.porto_name
            instance.location =  instance.location_countdown
            instance.startDate = instance.tanggal_countdown
            instance.startTime = instance.waktu_countdown
            instance.endTime = instance.waktu_countdown_selesai
            # save porto field ke field go to
            instance.lokasi = instance.location_countdown


            instance.save()

            # to create multiple image instance
            porto_instance = Portofolio.objects.get(pk=instance.pk)

            # to create instance quote
            instance_quote = form2.save(commit=False)
            instance_quote.portofolio = porto_instance
            instance_quote.save()

            # to create theme product
            instance_order = Order.objects.get(user=user)
            instance_orderitemfiture = OrderItem.objects.get(order=instance_order)

            instance_orderitem = form3.save(commit=False)
            instance_orderitem.portofolio = porto_instance
            instance_orderitem.fitur = instance_orderitemfiture.product
            instance_orderitem.save()

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

            messages.success(request, "Data saved!")
            return redirect("portofolio:configurasi")

    else:
        form = PortofolioForm(instance=obj)
        form2 = QuoteForm(instance=obj_quote)
        form3 = ThemeProductForm(instance=obj_themeproduct)
        formset = SpecialInviteFormSet(queryset= qs, prefix='invite')
        formset2 = DompetFormSet(queryset= qs2, prefix='dompet')
        formset3 = MultiImageFormSet(queryset= qs3, prefix='multiimage')
        formset4 = StoryFormSet(queryset=qs4, prefix='story')
        formset5 = MultiImageFormSet2(queryset=qs3, prefix='multiimage2')
        formset6 = AcaraFormSet(queryset=qs5, prefix='acara')


    context = {
        'form': form,
        'form2': form2,
        'form3': form3,
        'formset': formset,
        'formset2': formset2,
        'formset3': formset3,
        'formset4': formset4,
        'formset5': formset5,
        'formset6': formset6
    }
    # return redirect("portofolio:update_tampilan", slug=slug)
    return render(request, 'portofolio/configurasi/specialinvite_form.html', context)


def info_update(request, slug):
    # get instance portofolio from id
    obj = get_object_or_404(Portofolio, slug=slug)
    # quote instance by porto id
    obj_quote = get_object_or_404(Quote, portofolio= obj)
    # theme product instance by porto id
    obj_themeproduct = get_object_or_404(ThemeProduct, portofolio= obj)

    # Create formset factory, tidak menggunakan base formset agar menampilkan object instance
    SpecialInviteFormSet = modelformset_factory(
        SpecialInvitation,
        form=SpecialInvitationForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    DompetFormSet = modelformset_factory(
        Dompet,
        form=DompetForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    MultiImageFormSet = modelformset_factory(
        MultiImage,
        form=MultiImageForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    StoryFormSet = modelformset_factory(
        Story,
        form=StoryForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    MultiImageFormSet2 = modelformset_factory(
        MultiImage,
        form=MultiImageForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    AcaraFormSet = modelformset_factory(
        Acara,
        form=AcaraForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )

    # create query set for specialinvitation
    qs = SpecialInvitation.objects.filter(portofolio=obj)
    # create query set for dompet
    qs2 = Dompet.objects.filter(portofolio=obj)
    # create query set for multi image
    qs3 = MultiImage.objects.filter(portofolio=obj)
    # create query set for story
    qs4 = Story.objects.filter(portofolio=obj)
    # create query set for acara
    qs5 = Acara.objects.filter(portofolio=obj)

    # Define formset
    formset = SpecialInviteFormSet(request.POST or None,queryset= qs, prefix='invite')
    formset2 = DompetFormSet(request.POST or None,queryset= qs2, prefix='dompet')
    formset3 = MultiImageFormSet(request.POST or None, request.FILES, queryset= qs3, prefix='multiimage')
    formset4 = StoryFormSet(request.POST or None, request.FILES, queryset=qs4, prefix='story')
    formset5 = MultiImageFormSet2(request.POST or None, request.FILES, queryset=qs3, prefix='multiimage2')
    formset6 = AcaraFormSet(request.POST or None, request.FILES, queryset=qs5, prefix='acara')

    if request.method == "POST":
        form = PortofolioForm(request.POST or None, request.FILES, instance=obj)
        form2 = QuoteForm(request.POST or None, request.FILES, instance=obj_quote)
        form3 = ThemeProductForm(request.POST or None, request.FILES, instance=obj_themeproduct)

        if form.is_valid() and form2.is_valid() and form3.is_valid() and formset.is_valid() \
            and formset2.is_valid() and formset4.is_valid():
            # create portofolio instance
            instance = form.save(commit=False)
            # save user to porto
            user = request.user
            print(user)
            instance.user = user
            # save porto field ke field calender
            instance.name = instance.porto_name
            instance.location =  instance.location_countdown
            instance.startDate = instance.tanggal_countdown
            instance.startTime = instance.waktu_countdown
            instance.endTime = instance.waktu_countdown_selesai
            # save porto field ke field go to
            instance.lokasi = instance.location_countdown


            instance.save()

            # to create multiple image instance
            porto_instance = Portofolio.objects.get(pk=instance.pk)

            # to create instance quote
            instance_quote = form2.save(commit=False)
            instance_quote.portofolio = porto_instance
            instance_quote.save()

            # to create theme product
            instance_order = Order.objects.get(user=user)
            instance_orderitemfiture = OrderItem.objects.get(order=instance_order)

            instance_orderitem = form3.save(commit=False)
            instance_orderitem.portofolio = porto_instance
            instance_orderitem.fitur = instance_orderitemfiture.product
            instance_orderitem.save()

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

            messages.success(request, "Data saved!")
            return redirect("portofolio:configurasi")

    else:
        form = PortofolioForm(instance=obj)
        form2 = QuoteForm(instance=obj_quote)
        form3 = ThemeProductForm(instance=obj_themeproduct)
        formset = SpecialInviteFormSet(queryset= qs, prefix='invite')
        formset2 = DompetFormSet(queryset= qs2, prefix='dompet')
        formset3 = MultiImageFormSet(queryset= qs3, prefix='multiimage')
        formset4 = StoryFormSet(queryset=qs4, prefix='story')
        formset5 = MultiImageFormSet2(queryset=qs3, prefix='multiimage2')
        formset6 = AcaraFormSet(queryset=qs5, prefix='acara')


    context = {
        'form': form,
        'form2': form2,
        'form3': form3,
        'formset': formset,
        'formset2': formset2,
        'formset3': formset3,
        'formset4': formset4,
        'formset5': formset5,
        'formset6': formset6
    }

    # return redirect("portofolio:update_tampilan", slug=slug)
    return render(request, 'portofolio/configurasi/info_form.html', context)

def countdown_update(request, slug):
    # get instance portofolio from id
    obj = get_object_or_404(Portofolio, slug=slug)
    # quote instance by porto id
    obj_quote = get_object_or_404(Quote, portofolio= obj)
    # theme product instance by porto id
    obj_themeproduct = get_object_or_404(ThemeProduct, portofolio= obj)

    # Create formset factory, tidak menggunakan base formset agar menampilkan object instance
    SpecialInviteFormSet = modelformset_factory(
        SpecialInvitation,
        form=SpecialInvitationForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    DompetFormSet = modelformset_factory(
        Dompet,
        form=DompetForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    MultiImageFormSet = modelformset_factory(
        MultiImage,
        form=MultiImageForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    StoryFormSet = modelformset_factory(
        Story,
        form=StoryForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    MultiImageFormSet2 = modelformset_factory(
        MultiImage,
        form=MultiImageForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    AcaraFormSet = modelformset_factory(
        Acara,
        form=AcaraForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )

    # create query set for specialinvitation
    qs = SpecialInvitation.objects.filter(portofolio=obj)
    # create query set for dompet
    qs2 = Dompet.objects.filter(portofolio=obj)
    # create query set for multi image
    qs3 = MultiImage.objects.filter(portofolio=obj)
    # create query set for story
    qs4 = Story.objects.filter(portofolio=obj)
    # create query set for acara
    qs5 = Acara.objects.filter(portofolio=obj)

    # Define formset
    formset = SpecialInviteFormSet(request.POST or None,queryset= qs, prefix='invite')
    formset2 = DompetFormSet(request.POST or None,queryset= qs2, prefix='dompet')
    formset3 = MultiImageFormSet(request.POST or None, request.FILES, queryset= qs3, prefix='multiimage')
    formset4 = StoryFormSet(request.POST or None, request.FILES, queryset=qs4, prefix='story')
    formset5 = MultiImageFormSet2(request.POST or None, request.FILES, queryset=qs3, prefix='multiimage2')
    formset6 = AcaraFormSet(request.POST or None, request.FILES, queryset=qs5, prefix='acara')

    if request.method == "POST":
        form = PortofolioForm(request.POST or None, request.FILES, instance=obj)
        form2 = QuoteForm(request.POST or None, request.FILES, instance=obj_quote)
        form3 = ThemeProductForm(request.POST or None, request.FILES, instance=obj_themeproduct)

        if form.is_valid() and form2.is_valid() and form3.is_valid() and formset.is_valid() \
            and formset2.is_valid() and formset4.is_valid():
            # create portofolio instance
            instance = form.save(commit=False)
            # save user to porto
            user = request.user
            print(user)
            instance.user = user
            # save porto field ke field calender
            instance.name = instance.porto_name
            instance.location =  instance.location_countdown
            instance.startDate = instance.tanggal_countdown
            instance.startTime = instance.waktu_countdown
            instance.endTime = instance.waktu_countdown_selesai
            # save porto field ke field go to
            instance.lokasi = instance.location_countdown


            instance.save()

            # to create multiple image instance
            porto_instance = Portofolio.objects.get(pk=instance.pk)

            # to create instance quote
            instance_quote = form2.save(commit=False)
            instance_quote.portofolio = porto_instance
            instance_quote.save()

            # to create theme product
            instance_order = Order.objects.get(user=user)
            instance_orderitemfiture = OrderItem.objects.get(order=instance_order)

            instance_orderitem = form3.save(commit=False)
            instance_orderitem.portofolio = porto_instance
            instance_orderitem.fitur = instance_orderitemfiture.product
            instance_orderitem.save()

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

            messages.success(request, "Data saved!")
            return redirect("portofolio:configurasi")

    else:
        form = PortofolioForm(instance=obj)
        form2 = QuoteForm(instance=obj_quote)
        form3 = ThemeProductForm(instance=obj_themeproduct)
        formset = SpecialInviteFormSet(queryset= qs, prefix='invite')
        formset2 = DompetFormSet(queryset= qs2, prefix='dompet')
        formset3 = MultiImageFormSet(queryset= qs3, prefix='multiimage')
        formset4 = StoryFormSet(queryset=qs4, prefix='story')
        formset5 = MultiImageFormSet2(queryset=qs3, prefix='multiimage2')
        formset6 = AcaraFormSet(queryset=qs5, prefix='acara')


    context = {
        'form': form,
        'form2': form2,
        'form3': form3,
        'formset': formset,
        'formset2': formset2,
        'formset3': formset3,
        'formset4': formset4,
        'formset5': formset5,
        'formset6': formset6
    }

    return render(request, 'portofolio/configurasi/countdown_form.html', context)

def update(request, slug):
    # get instance portofolio from id
    obj = get_object_or_404(Portofolio, slug=slug)
    # quote instance by porto id
    obj_quote = get_object_or_404(Quote, portofolio= obj)
    # theme product instance by porto id
    obj_themeproduct = get_object_or_404(ThemeProduct, portofolio= obj)

    # Create formset factory, tidak menggunakan base formset agar menampilkan object instance
    SpecialInviteFormSet = modelformset_factory(
        SpecialInvitation,
        form=SpecialInvitationForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    DompetFormSet = modelformset_factory(
        Dompet,
        form=DompetForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    MultiImageFormSet = modelformset_factory(
        MultiImage,
        form=MultiImageForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    StoryFormSet = modelformset_factory(
        Story,
        form=StoryForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    MultiImageFormSet2 = modelformset_factory(
        MultiImage,
        form=MultiImageForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )
    AcaraFormSet = modelformset_factory(
        Acara,
        form=AcaraForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True
    )

    # create query set for specialinvitation
    qs = SpecialInvitation.objects.filter(portofolio=obj)
    # create query set for dompet
    qs2 = Dompet.objects.filter(portofolio=obj)
    # create query set for multi image
    qs3 = MultiImage.objects.filter(portofolio=obj)
    # create query set for story
    qs4 = Story.objects.filter(portofolio=obj)
    # create query set for acara
    qs5 = Acara.objects.filter(portofolio=obj)

    # Define formset
    formset = SpecialInviteFormSet(request.POST or None,queryset= qs, prefix='invite')
    formset2 = DompetFormSet(request.POST or None,queryset= qs2, prefix='dompet')
    formset3 = MultiImageFormSet(request.POST or None, request.FILES, queryset= qs3, prefix='multiimage')
    formset4 = StoryFormSet(request.POST or None, request.FILES, queryset=qs4, prefix='story')
    formset5 = MultiImageFormSet2(request.POST or None, request.FILES, queryset=qs3, prefix='multiimage2')
    formset6 = AcaraFormSet(request.POST or None, request.FILES, queryset=qs5, prefix='acara')

    if request.method == "POST":
        form = PortofolioForm(request.POST or None, request.FILES, instance=obj)
        form2 = QuoteForm(request.POST or None, request.FILES, instance=obj_quote)
        form3 = ThemeProductForm(request.POST or None, request.FILES, instance=obj_themeproduct)

        if form.is_valid() and form2.is_valid() and form3.is_valid() and formset.is_valid() \
            and formset2.is_valid() and formset4.is_valid():
            # create portofolio instance
            instance = form.save(commit=False)
            # save user to porto
            user = request.user
            print(user)
            instance.user = user
            # save porto field ke field calender
            instance.name = instance.porto_name
            instance.location =  instance.location_countdown
            instance.startDate = instance.tanggal_countdown
            instance.startTime = instance.waktu_countdown
            instance.endTime = instance.waktu_countdown_selesai
            # save porto field ke field go to
            instance.lokasi = instance.location_countdown


            instance.save()

            # to create multiple image instance
            porto_instance = Portofolio.objects.get(pk=instance.pk)

            # to create instance quote
            instance_quote = form2.save(commit=False)
            instance_quote.portofolio = porto_instance
            instance_quote.save()

            # to create theme product
            instance_order = Order.objects.get(user=user)
            instance_orderitemfiture = OrderItem.objects.get(order=instance_order)

            instance_orderitem = form3.save(commit=False)
            instance_orderitem.portofolio = porto_instance
            instance_orderitem.fitur = instance_orderitemfiture.product
            instance_orderitem.save()

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

            messages.success(request, "Data saved!")
            return redirect("portofolio:configurasi")

    else:
        form = PortofolioForm(instance=obj)
        form2 = QuoteForm(instance=obj_quote)
        form3 = ThemeProductForm(instance=obj_themeproduct)
        formset = SpecialInviteFormSet(queryset= qs, prefix='invite')
        formset2 = DompetFormSet(queryset= qs2, prefix='dompet')
        formset3 = MultiImageFormSet(queryset= qs3, prefix='multiimage')
        formset4 = StoryFormSet(queryset=qs4, prefix='story')
        formset5 = MultiImageFormSet2(queryset=qs3, prefix='multiimage2')
        formset6 = AcaraFormSet(queryset=qs5, prefix='acara')


    context = {
        'form': form,
        'form2': form2,
        'form3': form3,
        'formset': formset,
        'formset2': formset2,
        'formset3': formset3,
        'formset4': formset4,
        'formset5': formset5,
        'formset6': formset6
    }

    return render(request, 'portofolio/portofolio_detail.html', context)

def myportofolio(request):
    user = request.user
    portofolios = Portofolio.objects.filter(user=user)
    context = {
        'portofolios': portofolios,
        'today': now().date()
    }
    return render(request, 'portofolio/myportofolio.html', context)



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