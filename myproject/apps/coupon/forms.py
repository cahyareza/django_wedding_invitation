from django import forms
from .models import Coupon


class CouponForm(forms.ModelForm):

    code = forms.CharField(
        label='Coupon code',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'coupon',
                'class': 'input',
                'style': 'font-size: 13px; text-transform: capitalize'
            }
        )
    )
    class Meta:
        model = Coupon
        fields = ['code']

    def clean(self):
        self.cleaned_data = super().clean()
        self.cleaned_data['field'] = value
        return self.cleaned_data

    # SUPER FUNCTION
    def __init__(self, *args, **kwargs):
        super(CouponForm, self).__init__(*args, **kwargs)

        # ========== CONTROL PANEL (Optional method to control ========== !
        # 1. Input required
        self.fields['code'].required = False
