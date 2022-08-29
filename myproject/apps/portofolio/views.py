from django.shortcuts import render, redirect, get_object_or_404

from .forms import CoupleModelForm
from .models import Couple

# Create your views here.
def register_couple(request, id=None):
    couple = None

    if id:
        couple = get_object_or_404(couple, id=id)

    if request.method == "POST":
        form = CoupleModelForm(
            data=request.POST,
            files=request.FILES,
            instance=couple
        )

        if form.is_valid():
            couple = form.save()
            redirect("couple:idea_detail", pk=idea.pk)
    else:
        form = CoupleModelForm(instance=couple)

    context = {
        "form_couple":  form
    }

    return render(request, "portofolio/register_porto.html", context)