from django.shortcuts import render, redirect

from .models import Photo
from .forms import PhotoForm
from .forms import PhotoForm2


def photo_list(request):
    photos = Photo.objects.all()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        form2 = PhotoForm2(request.POST, request.FILES)
        print("unvalid")
        # if form.is_valid():
        #     print("valid")
        #     form.save()
        #     return redirect('cropping:photo_list')
        if form.is_valid() and form2.is_valid():
            print("valid")
            form2.save()
            form.save()
            return redirect('cropping:photo_list')
    else:
        form = PhotoForm()
        form2 = PhotoForm2()
    return render(request, 'cropping/photo_list.html', {'form': form, 'form2': form2, 'photos': photos})