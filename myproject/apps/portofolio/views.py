from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.forms import modelformset_factory
from django.core.exceptions import ValidationError

from .models import MultiImage, Portofolio, SpecialInvitation

from .forms import PortofolioForm, MultiImageForm, SpecialInvitationForm, BaseRegisterFormSet

# Create your views here.
def register(request, id=None):
    # initiate formset
    SpecialInviteFormSet = modelformset_factory(
        SpecialInvitation,
        form=SpecialInvitationForm,
        formset=BaseRegisterFormSet,
        extra=1,
    )

    if request.method == "POST":
        form = PortofolioForm(request.POST or None, request.FILES)
        form2 = MultiImageForm(request.POST or None, request.FILES)
        formset = SpecialInviteFormSet(request.POST or None)
        # get image from form2
        images = request.FILES.getlist('image')

        # form validation
        if form.is_valid() and form2.is_valid() and formset.is_valid():
            # create portofolio instance
            instance = form.save(commit=False)
            instance.save()

            # to create multiple image instance
            porto_instance = Portofolio.objects.get(pk=instance.pk)
            for i in images:
                MultiImage.objects.create(portofolio=porto_instance, image=i)

            # to create multiple value instance
            for form2 in formset:
                # Not save blank field use has_changed()
                if form2.is_valid() and form2.has_changed():
                    child = form2.save(commit=False)
                    child.portofolio = porto_instance
                    child.save()

            messages.success(request, "Registered Successfully !")
            return HttpResponseRedirect('/')
        else:
            return render(request, "portofolio/register_porto.html", {'form': form, 'form2': form2, 'formset': formset})

    else:
        form = PortofolioForm()
        form2 = MultiImageForm()
        formset = SpecialInviteFormSet()

        return render(request, "portofolio/register_porto.html", {'form': form, 'form2': form2, 'formset': formset})