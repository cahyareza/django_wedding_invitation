from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect

from .forms import PortofolioForm

# Create your views here.
def register(request):
    if request.method == "POST":
        form = PortofolioForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Registered Successfully !")
            return HttpResponseRedirect('/')
        else:
            return render(request, "portofolio/register_porto.html", {'form': form})

    else:
        form = PortofolioForm()
        return render(request, "portofolio/register_porto.html", {'form':form})