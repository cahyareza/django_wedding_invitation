from django import forms
from django.core.validators import RegexValidator
from .models import Order

class OrderForm(forms.ModelForm):
    phone = forms.CharField(label="Nomor handphone", min_length=12, max_length=13,
        validators= [RegexValidator(r'^[0-9]*$',
        message="Only numbers is allowed !")],
        widget=forms.TextInput(attrs={
        "class": "input",
        "placeholder": "Nomor handphone",
        'style': 'font-size: 13px',
    }))
    place = forms.CharField(label="Kabupaten",
        validators= [RegexValidator(r'^[a-zA-ZA-y\s]*$',
        message="Only letters is allowed !")],
        widget=forms.TextInput(attrs={
        "class": "input",
        "placeholder": "Asal kabupaten",
        'style': 'font-size: 13px',
    }))
    nama_rekening = forms.CharField(label="Nama pemilik rekening", min_length=3,
        validators=[RegexValidator(r'^[a-zA-ZA-y\s]*$',
        message="Only letters is allowed !")],
        widget=forms.TextInput(attrs={
        "class": "input",
        "placeholder": "Nama pemilik rekening",
        'style': 'font-size: 13px',

    }))

    bukti = forms.FileField(
        label="Bukti pembayaran",
        widget=forms.ClearableFileInput(
            attrs={
                'placeholder': 'Select a picture',
                'class': 'image',
                'style': 'font-size: 15px',
            }
        )
    )

    class Meta:
        model = Order
        fields = "__all__"

        # OUTSIDE WIDGET
        widgets = {
            # payment
            'payment': forms.Select(
                attrs={
                    'class': 'input',
                    'style': 'font-size: 13px',
                }
            ),
        }

    # SUPER FUNCTION
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)

        # ========== CONTROL PANEL (Optional method to control ========== !
        # 1. Input required
        self.fields['user'].required = False
        self.fields['status'].required = False
        self.fields['paid'].required = False
        self.fields['bukti'].required = False

        # 2. Select option
        self.fields["payment"].choices = [('', 'Pilih payment'),] + list(self.fields["payment"].choices)[1:]
