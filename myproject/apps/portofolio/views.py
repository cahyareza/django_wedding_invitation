from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.forms import modelformset_factory
from django.core.exceptions import ValidationError
from .serializers import PortofolioSerializer, RekeningSerializer, DompetSerializer, \
    MultiImageSerializer, SpecialInvitationSerializer, PaymentSerializer, QuoteSerializer, \
    UcapanSerializer, HadirSerializer, FiturSerializer, FiturProductSerializer, ThemeSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework import filters
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet


from .models import MultiImage, Portofolio, SpecialInvitation, Dompet, Quote, Fitur, \
    Rekening, Payment, MultiImage, SpecialInvitation, Ucapan, Hadir, Fitur, FiturProduct, \
    Theme

from .forms import PortofolioForm, MultiImageForm, SpecialInvitationForm, \
    BaseRegisterFormSet, DompetForm, QuoteForm

def home(request):
    return render(request, 'index.html')

# Portofolio registration
def register(request, id=None):
    # initiate formset
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

    portofolio = Portofolio.objects.filter(user=request.user).exists()
    if portofolio == False:
        if request.method == "POST":
            form = PortofolioForm(request.POST or None, request.FILES)
            form2 = QuoteForm(request.POST or None, request.FILES)
            formset = SpecialInviteFormSet(request.POST or None, prefix='invite')
            formset2 = DompetFormSet(request.POST or None, prefix='dompet')
            formset3 = MultiImageFormSet(request.POST or None, request.FILES, prefix='multiimage')

            print(request.POST)
            # form validation
            if form.is_valid() and form2.is_valid() and formset.is_valid():
                # create portofolio instance
                instance = form.save(commit=False)
                # save user to porto
                user = request.user
                instance.user = user
                # save porto field ke field calender
                instance.name = instance.porto_name
                instance.location =  instance.tempat_resepsi
                instance.startDate = instance.tanggal_resepsi
                instance.startTime = instance.waktu_resepsi
                instance.endTime = instance.waktu_selesai_resepsi
                # save porto field ke field go to
                instance.lokasi = instance.tempat_resepsi


                instance.save()

                # to create multiple image instance
                porto_instance = Portofolio.objects.get(pk=instance.pk)

                # to create instance quote
                instance_quote = form2.save(commit=False)
                instance_quote.portofolio = porto_instance
                instance_quote.save()

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

                messages.success(request, "Registered Successfully !")
                return HttpResponseRedirect('/')
            else:
                return render(request, "portofolio/register_porto.html", {'form': form,
                    'form2': form2, 'formset': formset, 'formset2': formset2, 'formset3': formset3})

        else:
            form = PortofolioForm()
            form2 = QuoteForm()
            formset = SpecialInviteFormSet(prefix='invite')
            formset2 = DompetFormSet(prefix='dompet')
            formset3 = MultiImageFormSet(prefix='multiimage')

    else:
        return render(request, 'portofolio/regis_failed.html')

    return render(request, "portofolio/register_porto.html", {'form': form,
        'form2': form2,'formset': formset, 'formset2': formset2, 'formset3': formset3})

def update(request, slug):
    # get instance portofolio from id
    obj = get_object_or_404(Portofolio, slug=slug)
    # quote instance by porto id
    obj_quote = get_object_or_404(Quote, portofolio= obj)


    # Create formset factory, tidak menggunakan base formset agar menampilkan object instance
    SpecialInviteFormSet = modelformset_factory(
        SpecialInvitation,
        form=SpecialInvitationForm,
        extra=1,
    )
    DompetFormSet = modelformset_factory(
        Dompet,
        form=DompetForm,
        extra=1,
    )
    MultiImageFormSet = modelformset_factory(
        MultiImage,
        form=MultiImageForm,
        extra=1,
    )

    # create query set for multi image
    qs = SpecialInvitation.objects.filter(portofolio=obj)
    # create query set for multi image
    qs2 = Dompet.objects.filter(portofolio=obj)
    # create query set for multi image
    qs3 = MultiImage.objects.filter(portofolio=obj)

    # Define formset
    formset = SpecialInviteFormSet(request.POST or None,queryset= qs, prefix='invite')
    formset2 = DompetFormSet(request.POST or None,queryset= qs2, prefix='dompet')
    formset3 = MultiImageFormSet(request.POST or None, request.FILES, queryset= qs3, prefix='multiimage')

    if request.method == "POST":
        form = PortofolioForm(request.POST or None, request.FILES, instance=obj)
        form2 = QuoteForm(request.POST or None, request.FILES, instance=obj_quote)

        if form.is_valid() and form2.is_valid() and formset.is_valid():
            # create portofolio instance
            instance = form.save(commit=False)
            # save user to porto
            user = request.user
            print(user)
            instance.user = user
            # save porto field ke field calender
            instance.name = instance.porto_name
            instance.location =  instance.tempat_resepsi
            instance.startDate = instance.tanggal_resepsi
            instance.startTime = instance.waktu_resepsi
            instance.endTime = instance.waktu_selesai_resepsi
            # save porto field ke field go to
            instance.lokasi = instance.tempat_resepsi


            instance.save()

            # to create multiple image instance
            porto_instance = Portofolio.objects.get(pk=instance.pk)

            # to create instance quote
            instance_quote = form2.save(commit=False)
            instance_quote.portofolio = porto_instance
            instance_quote.save()

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

            messages.success(request, "Data saved!")
            return redirect("portofolio:update", slug=instance.slug)

    else:
        form = PortofolioForm(instance=obj)
        form2 = QuoteForm(instance=obj_quote)
        formset = SpecialInviteFormSet(queryset= qs, prefix='invite')
        formset2 = DompetFormSet(queryset= qs2, prefix='dompet')
        formset3 = MultiImageFormSet(queryset= qs3, prefix='multiimage')


    context = {
        'form': form,
        'form2': form2,
        'formset': formset,
        'formset2': formset2,
        'formset3': formset3,
    }

    return render(request, 'portofolio/portofolio_detail.html', context)

def myportofolio(request):
    user = request.user
    portofolios = Portofolio.objects.filter(user=user)
    context = {
        'portofolios': portofolios,
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

# FiturProduct
class FiturProductList(generics.ListCreateAPIView):
    queryset = FiturProduct.objects.all()
    serializer_class = FiturProductSerializer
    name = 'fiturproduct-list'


class FiturProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FiturProduct.objects.all()
    serializer_class = FiturProductSerializer
    name = 'fiturproduct-detail'

# Theme
class ThemeList(generics.ListCreateAPIView):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer
    name = 'theme-list'


class ThemeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer
    name = 'theme-detail'

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
            'fiturproducts': reverse('portofolio:fiturproduct-list', request=request),
            'themes': reverse('portofolio:theme-list', request=request),
            })