from django import forms

from .models import Order

class OrderForm(forms.ModelForm):
    phone = forms.CharField(label="Nomor handphone",
        widget=forms.TextInput(attrs={
        "class": "input",
        "placeholder": "Nomor handphone"
    }))
    place = forms.CharField(label="Kabupaten",
        widget=forms.TextInput(attrs={
        "class": "input",
        "placeholder": "Asal kabupaten"

    }))
    nama_rekening = forms.CharField(label="Nama pemilik rekening",
        widget=forms.TextInput(attrs={
        "class": "input",
        "placeholder": "Nama pemilik rekening"

    }))

    class Meta:
        model = Order
        fields = "__all__"

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

        # 2. Select option
        self.fields["payment"].choices = [('', 'Pilih payment'),] + list(self.fields["payment"].choices)[1:]
