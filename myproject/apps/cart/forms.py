from django import forms

class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(initial=1, widget=forms.HiddenInput)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
