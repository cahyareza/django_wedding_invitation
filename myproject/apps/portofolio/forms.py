from django import forms
from .models import Couple

#class ProductForm(forms.Form):
#    title = forms.CharField()

class CoupleModelForm(forms.ModelForm):
    # title = forms.CharField()
    class Meta:
        model = Couple
        fields = "__all__"