from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect

from .models import MultiImage, Portofolio

from .forms import PortofolioForm, MultiImageForm

# Create your views here.
def register(request):
    if request.method == "POST":
        form = PortofolioForm(request.POST or None, request.FILES)
        form2 = MultiImageForm(request.POST or None, request.FILES)
        images = request.FILES.getlist('image')
        if form.is_valid() and form2.is_valid():
            instance = form.save(commit=False)
            instance.save()

            porto_instance = Portofolio.objects.get(pk=instance.pk)

            for i in images:
                MultiImage.objects.create(portofolio=porto_instance, image=i)

            messages.success(request, "Registered Successfully !")
            return HttpResponseRedirect('/')
        else:
            return render(request, "portofolio/register_porto.html", {'form': form, 'form2': form2})

    else:
        form = PortofolioForm()
        form2 = MultiImageForm()

        return render(request, "portofolio/register_porto.html", {'form': form, 'form2': form2})