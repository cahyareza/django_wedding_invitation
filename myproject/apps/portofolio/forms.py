from django import forms
from django.forms import ClearableFileInput
from .models import Portofolio, MultiImage
from django.core.validators import RegexValidator
from django.contrib.admin import widgets

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

    # INFORMASI ACARA
    tempat_akad = forms.CharField(
        label='Tempat akad', min_length=3, max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Tempat akad',
                'class': 'input',
                'style': 'font-size: 13px; text-transform: capitalize'
            }
        )
    )

    link_gmap_akad = forms.CharField(
        label='Link google maps', min_length=3, max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Link google maps',
                'class': 'input',
                'style': 'font-size: 13px;'
            }
        )
    )

    tempat_resepsi = forms.CharField(
        label='Tempat resepsi', min_length=3, max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Tempat resepsi',
                'class': 'input',
                'style': 'font-size: 13px; text-transform: capitalize'
            }
        )
    )

    link_gmap_resepsi = forms.CharField(
        label='Link google maps', min_length=3, max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Link google maps',
                'class': 'input',
                'style': 'font-size: 13px;'
            }
        )
    )

    tempat_unduhmantu = forms.CharField(
        label='Tempat unduh mantu', min_length=3, max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Tempat unduh mantu',
                'class': 'input',
                'style': 'font-size: 13px; text-transform: capitalize'
            }
        )
    )

    link_gmap_unduhmantu = forms.CharField(
        label='Link google maps', min_length=3, max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Link google maps',
                'class': 'input',
                'style': 'font-size: 13px;'
            }
        )
    )

    # INFORMASI OUR MOMENT

    video = forms.CharField(
        label='Link video',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Link video',
                'class': 'input',
                'style': 'font-size: 13px;'
            }
        )
    )

    livestream = forms.CharField(
        label='Link livestream',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Link livestream',
                'class': 'input',
                'style': 'font-size: 13px;'
            }
        )
    )

    # Photo (Upload photo)
    # photos = forms.MultiImageField(
    #     min_num=1, max_num=20,
    #     label="Foto",
    #     widget=forms.ClearableFileInput(
    #         attrs={
    #             'placeholder': 'Select a picture',
    #             'class': 'image',
    #             'style': 'font-size: 15px',
    #             'accept': 'image/png, image/jpeg'
    #         }
    #     )
    # )



    class Meta:
        model = Portofolio
        fields = "__all__"
        labels = {
            'tanggal_unduhmantu': "Tanggal unduh mantu",
            'waktu_unduhmantu': "Waktu unduh mantu",
            'waktu_selesai_unduhmantu': "Waktu selesai unduh mantu",
        }

        # OUTSIDE WIDGET
        widgets = {
            # Tanggal akad
            'tanggal_akad': forms.DateInput(
                attrs={
                    'style': 'font-size: 13px; cursor: pointer;',
                    'type': 'date',
                    'class': 'input',
                    'onkeydown': 'return false',  # Block typing inside field
                    'min': '2022-01-01',
                    'max': '2030-01-01'
                }
            ),
            # Waktu akad
            'waktu_akad': forms.TimeInput(
                attrs={
                    'placeholder': 'Waktu akad',
                    'style': 'font-size: 13px; cursor: pointer;',
                    'class': 'input',
                    'data-mask': '00:00'
                }
            ),
            # Waktu selesai akad
            'waktu_selesai_akad': forms.TimeInput(
                attrs={
                    'placeholder': 'Waktu selesai akad',
                    'style': 'font-size: 13px; cursor: pointer;',
                    'class': 'input',
                    'data-mask': '00:00'
                }
            ),
            # Tanggal resepsi
            'tanggal_resepsi': forms.DateInput(
                attrs={
                    'style': 'font-size: 13px; cursor: pointer;',
                    'type': 'date',
                    'class': 'input',
                    'onkeydown': 'return false',  # Block typing inside field
                    'min': '2022-01-01',
                    'max': '2030-01-01'
                }
            ),
            # Waktu resepsi
            'waktu_resepsi': forms.TimeInput(
                attrs={
                    'placeholder': 'Waktu resepsi',
                    'style': 'font-size: 13px; cursor: pointer;',
                    'class': 'input',
                    'data-mask': '00:00'
                }
            ),
            # Waktu selesai resepsi
            'waktu_selesai_resepsi': forms.TimeInput(
                attrs={
                    'placeholder': 'Waktu selesai resepsi',
                    'style': 'font-size: 13px; cursor: pointer;',
                    'class': 'input',
                    'data-mask': '00:00'
                }
            ),
            # Tanggal unduh mantu
            'tanggal_unduhmantu': forms.DateInput(
                attrs={
                    'style': 'font-size: 13px; cursor: pointer;',
                    'type': 'date',
                    'class': 'input',
                    'onkeydown': 'return false',  # Block typing inside field
                    'min': '2022-01-01',
                    'max': '2030-01-01'
                }
            ),
            # Waktu unduh mantu
            'waktu_unduhmantu': forms.TimeInput(
                attrs={
                    'placeholder': 'Waktu unduh mantu',
                    'style': 'font-size: 13px; cursor: pointer;',
                    'class': 'input',
                    'data-mask': '00:00'
                }
            ),
            # Waktu selesai unduh mantu
            'waktu_selesai_unduhmantu': forms.TimeInput(
                attrs={
                    'placeholder': 'Waktu selesai unduh mantu',
                    'style': 'font-size: 13px; cursor: pointer;',
                    'class': 'input',
                    'data-mask': '00:00'
                }
            ),
        }

    # SUPER FUNCTION
    # def __init__(self, *args, **kwargs):
    #     super(PortofolioForm, self).__init__(*args, **kwargs)
    #
    #     self.fields['waktu_akad'].widget = widgets.AdminTimeWidget()

class MultiImageForm(forms.ModelForm):
    class Meta:
        model = MultiImage
        fields = ['image']
        widgets = {
            'image': ClearableFileInput(attrs={'multiple': True}),
        }