from django import forms
from django.core.validators import RegexValidator
from .models import Order, OrderItem

class OrderForm(forms.ModelForm):
    phone = forms.CharField(label="Nomor handphone", min_length=12, max_length=13,
        validators= [RegexValidator(r'^[0-9]*$',
        message="Only numbers is allowed !")],
        widget=forms.TextInput(attrs={
        "class": "input",
        "placeholder": "Nomor handphone",
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

    bukti_upgrade = forms.FileField(
        label="Bukti pembayaran upgrade",
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
        labels = {
            'place': 'Kabupaten',
            'info_web': 'Dari Mana Mengetahui Kami?'
        }

        # OUTSIDE WIDGET
        widgets = {
            # payment
            'payment': forms.Select(
                attrs={
                    'class': 'input',
                    'style': 'font-size: 13px',
                }
            ),
            'place': forms.Select(
                attrs={
                    'class': 'input',
                    'style': 'font-size: 13px',
                }
            ),
            'info_web': forms.Select(
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
        self.fields['bukti_upgrade'].required = False
        self.fields['status_upgrade'].required = False
        self.fields['upgrade_status'].required = False
        self.fields['paid_upgrade'].required = False
        self.fields['discount'].required = False
        self.fields['info_web'].required = True

        # 2. Select option
        self.fields["payment"].choices = [('', 'Pilih payment'),] + list(self.fields["payment"].choices)[1:]
        self.fields["place"].choices = [('', 'Pilih kabupaten'),] + list(self.fields["place"].choices)[1:]
        self.fields["info_web"].choices = [('', 'Pilih info'), ] + list(self.fields["info_web"].choices)[1:]

        # 3. Help text
        self.fields['bukti'].help_text = 'Segera upload bukti pembayaran, agar order terkonfirmasi.'
        self.fields['bukti_upgrade'].help_text = 'Segera upload bukti pembayaran upgrade, agar order terkonfirmasi.'

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ["product_update"]
        labels = {
            'product_update': 'Fitur'
        }

        # OUTSIDE WIDGET
        widgets = {
            # payment
            'product_update': forms.Select(
                attrs={
                    'class': 'input',
                    'style': 'font-size: 13px',
                }
            ),
        }

    # SUPER FUNCTION
    def __init__(self, *args, **kwargs):
        super(OrderItemForm, self).__init__(*args, **kwargs)

        # ========== CONTROL PANEL (Optional method to control ========== !
        # 1. Input required
        self.fields['product_update'].required = False

        # 2. Select option
        self.fields["product_update"].choices = list(self.fields["product_update"].choices)[2:]
