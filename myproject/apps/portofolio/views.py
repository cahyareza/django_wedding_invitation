from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.forms import modelformset_factory
from django.core.exceptions import ValidationError

from .models import MultiImage, Portofolio, SpecialInvitation, Dompet, Quote

from .forms import PortofolioForm, MultiImageForm, SpecialInvitationForm, \
    BaseRegisterFormSet, DompetForm, QuoteForm

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
