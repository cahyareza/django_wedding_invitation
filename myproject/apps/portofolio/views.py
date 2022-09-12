from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.forms import modelformset_factory
from django.core.exceptions import ValidationError

from .models import MultiImage, Portofolio, SpecialInvitation, Dompet

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

    if request.method == "POST":
        form = PortofolioForm(request.POST or None, request.FILES)
        form2 = MultiImageForm(request.POST or None, request.FILES)
        form3 = QuoteForm(request.POST or None, request.FILES)
        formset = SpecialInviteFormSet(request.POST or None, prefix='invite')
        formset2 = DompetFormSet(request.POST or None, prefix='dompet')
        # get image from form2
        images = request.FILES.getlist('image')

        # print(request.POST)
        # form validation
        if form.is_valid() and form2.is_valid() and formset.is_valid():
            # create portofolio instance
            instance = form.save(commit=False)
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
            for i in images:
                MultiImage.objects.create(portofolio=porto_instance, image=i)

            # to create instance quote
            instance_quote = form3.save(commit=False)
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

            messages.success(request, "Registered Successfully !")
            return HttpResponseRedirect('/')
        else:
            return render(request, "portofolio/register_porto.html", {'form': form,
                'form2': form2, 'form3': form3, 'formset': formset, 'formset2': formset2})

    else:
        form = PortofolioForm()
        form2 = MultiImageForm()
        form3 = QuoteForm()
        formset = SpecialInviteFormSet(prefix='invite')
        formset2 = DompetFormSet(prefix='dompet')

        return render(request, "portofolio/register_porto.html", {'form': form,
            'form2': form2, 'form3': form3,'formset': formset, 'formset2': formset2})

def portofolio_detail(request, id):
    data = Portofolio.objects.get(pk=id)
    form = PortofolioForm(instance = data)
    context = {'form': form}
    return render(request, 'portofolio/portofolio_detail.html', context)