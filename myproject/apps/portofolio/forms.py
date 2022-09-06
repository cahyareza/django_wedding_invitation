from django import forms
from .models import Portofolio
from django.core.validators import RegexValidator

# Every letters to LowerCase
class Lowercase(forms.CharField):
    def to_python(self, value):
        if value:
            return value.lower()

# Every letters to UpperCase
class Uppercase(forms.CharField):
    def to_python(self, value):
        if value:
            return value.upper()

class PortofolioForm(forms.ModelForm):
    # INFORMASI UNDANGAN
    porto_name = forms.CharField(
        label='Nama undangan', min_length=3, max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Misal: Undangan Pernikahan Cahya dan Mila',
                'class': 'input',
                'style': 'font-size: 13px; text-transform: capitalize'
            }
        )
    )

    # INFORMASI PASANGAN
    # PEREMPUAN
    pname = forms.CharField(
        label='Nama', min_length=3, max_length=50,
        validators=[RegexValidator(r'^[a-zA-ZA-y\s]*$',
        message="Only letters is allowed !")],
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nama',
                'class': 'input',
                'style': 'font-size: 13px; text-transform: capitalize'
            }
        )
    )

    pinsta_link = Lowercase(
        label='Link instagram', min_length=25, max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'https://www.instagram.com/cahya_rez/',
                'class': 'input',
                'style': 'font-size: 13px;'
            }
        )
    )

    panak_ke = forms.CharField(
        label='Anak ke-', min_length=1, max_length=1,
        validators= [RegexValidator(r'^[0-9]*$',
        message="Only numbers is allowed !")],
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Anak ke-',
                'class': 'input',
                'style': 'font-size: 13px',
            }
        )
    )

    pnama_ayah = forms.CharField(
        label='Nama ayah', min_length=3, max_length=50,
        validators=[RegexValidator(r'^[a-zA-ZA-y\s]*$',
        message="Only letters is allowed !")],
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nama ayah',
                'class': 'input',
                'style': 'font-size: 13px; text-transform: capitalize'
            }
        )
    )

    pnama_ibu = forms.CharField(
        label='Nama ibu', min_length=3, max_length=50,
        validators=[RegexValidator(r'^[a-zA-ZA-y\s]*$',
        message="Only letters is allowed !")],
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nama ibu',
                'class': 'input',
                'style': 'font-size: 13px; text-transform: capitalize'
            }
        )
    )

    # Photo (Upload photo)
    ppicture = forms.FileField(
        label="Foto",
        widget=forms.ClearableFileInput(
            attrs={
                'placeholder': 'Select a picture',
                'class': 'image',
                'style': 'font-size: 15px',
                'accept': 'image/png, image/jpeg'
            }
        )
    )


    # LAKI - LAKI
    lname = forms.CharField(
        label='Nama', min_length=3, max_length=50,
        validators=[RegexValidator(r'^[a-zA-ZA-y\s]*$',
        message="Only letters is allowed !")],
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nama',
                'class': 'input',
                'style': 'font-size: 13px; text-transform: capitalize'
            }
        )
    )

    linsta_link = Lowercase(
        label='Link instagram', min_length=25, max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'https://www.instagram.com/cahya_rez/',
                'class': 'input',
                'style': 'font-size: 13px;'
            }
        )
    )

    lanak_ke = forms.CharField(
        label='Anak ke-', min_length=1, max_length=1,
        validators= [RegexValidator(r'^[0-9]*$',
        message="Only numbers is allowed !")],
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Anak ke-',
                'class': 'input',
                'style': 'font-size: 13px',
            }
        )
    )

    lnama_ayah = forms.CharField(
        label='Nama ayah', min_length=3, max_length=50,
        validators=[RegexValidator(r'^[a-zA-ZA-y\s]*$',
        message="Only letters is allowed !")],
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nama ayah',
                'class': 'input',
                'style': 'font-size: 13px; text-transform: capitalize'
            }
        )
    )

    lnama_ibu = forms.CharField(
        label='Nama ibu', min_length=3, max_length=50,
        validators=[RegexValidator(r'^[a-zA-ZA-y\s]*$',
        message="Only letters is allowed !")],
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nama ibu',
                'class': 'input',
                'style': 'font-size: 13px; text-transform: capitalize'
            }
        )
    )

    # Photo (Upload photo)
    lpicture = forms.FileField(
        label="Foto",
        widget=forms.ClearableFileInput(
            attrs={
                'placeholder': 'Select a picture',
                'class': 'image',
                'style': 'font-size: 15px',
                'accept': 'image/png, image/jpeg'
            }
        )
    )

    class Meta:
        model = Portofolio
        fields = "__all__"