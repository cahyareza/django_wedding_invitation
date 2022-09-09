from django import forms
import re
from django.forms import ClearableFileInput
from .models import Portofolio, MultiImage, SpecialInvitation, Dompet
from django.core.validators import RegexValidator
from django.contrib.admin import widgets
from django.forms import BaseFormSet
from django.core.exceptions import ValidationError

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


# ================== MODELFORM =================== !
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
        label='Tempat akad', min_length=3, max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Tempat akad',
                'class': 'input',
                'style': 'font-size: 13px; text-transform: capitalize'
            }
        )
    )

    link_gmap_akad = forms.CharField(
        label='Link google maps',
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Link ke google maps',
                'class': 'textarea',
                'style': 'font-size: 13px',
            }
        )
    )

    tempat_resepsi = forms.CharField(
        label='Tempat resepsi', min_length=3, max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Tempat resepsi',
                'class': 'input',
                'style': 'font-size: 13px; text-transform: capitalize'
            }
        )
    )

    link_gmap_resepsi = forms.CharField(
        label='Link google maps',
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Link ke google maps',
                'class': 'textarea',
                'style': 'font-size: 13px',
            }
        )
    )

    tempat_unduhmantu = forms.CharField(
        label='Tempat unduh mantu', min_length=3, max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Tempat unduh mantu',
                'class': 'input',
                'style': 'font-size: 13px; text-transform: capitalize'
            }
        )
    )

    link_gmap_unduhmantu = forms.CharField(
        label='Link google maps',
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Link ke google maps',
                'class': 'textarea',
                'style': 'font-size: 13px',
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

    # INFORMASI ADD TO CALENDER

    name = forms.CharField(
        label='Nama notifikasi', min_length=3, max_length=50,
        validators=[RegexValidator(r'^[a-zA-ZA-y\s]*$',
        message="Only letters is allowed !")],
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nama notifikasi',
                'class': 'input',
                'style': 'font-size: 13px; text-transform: capitalize'
            }
        )
    )

    description = forms.CharField(
        label='Deskripsi undangan', min_length=50, max_length=1000,
        required=True,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Deskripsi undangan',
                'class': 'textarea',
                'style': 'font-size: 13px',
            }
        )
    )

    location = forms.CharField(
        label='Lokasi acara',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Lokasi acara',
                'class': 'input',
                'style': 'font-size: 13px; text-transform: capitalize'
            }
        )
    )

    options = forms.CharField(
        label='Options',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Options',
                'class': 'input',
                'style': 'font-size: 13px; text-transform: capitalize'
            }
        )
    )

    trigger = forms.CharField(
        label='Trigger',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Trigger',
                'class': 'input',
                'style': 'font-size: 13px; text-transform: capitalize'
            }
        )
    )

    iCalFileName = forms.CharField(
        label='iCalFileName',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'iCalFileName',
                'class': 'input',
                'style': 'font-size: 13px; text-transform: capitalize'
            }
        )
    )

    # INFORMASI GO TO

    link_iframe = forms.CharField(
        label='Link embed map', min_length=50, max_length=1000,
        required=True,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Link embed map',
                'class': 'textarea',
                'style': 'font-size: 13px',
            }
        )
    )
    link_gmap = forms.CharField(
        label='Link ke google maps', min_length=50, max_length=1000,
        required=True,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Link ke google maps',
                'class': 'textarea',
                'style': 'font-size: 13px',
            }
        )
    )

    lokasi = forms.CharField(
        label='lokasi',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'lokasi',
                'class': 'input',
                'style': 'font-size: 13px; text-transform: capitalize'
            }
        )
    )

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
            # Tanggal acara di calender
            'startDate': forms.DateInput(
                attrs={
                    'style': 'font-size: 13px; cursor: pointer;',
                    'type': 'date',
                    'class': 'input',
                    'onkeydown': 'return false',  # Block typing inside field
                    'min': '2022-01-01',
                    'max': '2030-01-01'
                }
            ),
            # Waktu acara mulai di calender
            'startTime': forms.TimeInput(
                attrs={
                    'placeholder': 'Waktu mulai acara',
                    'style': 'font-size: 13px; cursor: pointer;',
                    'class': 'input',
                    'data-mask': '00:00'
                }
            ),
            # Waktu acara selesai di calender
            'endTime': forms.TimeInput(
                attrs={
                    'placeholder': 'Waktu selesai acara',
                    'style': 'font-size: 13px; cursor: pointer;',
                    'class': 'input',
                    'data-mask': '00:00'
                }
            ),
            # Timezone
            'timeZone' : forms.Select(
                attrs={
                    'class': 'input',
                    'style': 'font-size: 13px',
                }
            ),
        }

    # SUPER FUNCTION
    def __init__(self, *args, **kwargs):
        super(PortofolioForm, self).__init__(*args, **kwargs)

        # ========== CONTROL PANEL (Optional method to control ========== !
        # 1. Input required
        # self.fields['message'].required = True
        self.fields['name'].required = False
        self.fields['description'].required = False
        self.fields['startDate'].required = False
        self.fields['location'].required = False
        self.fields['startTime'].required = False
        self.fields['endTime'].required = False
        self.fields['options'].required = False
        self.fields['trigger'].required = False
        self.fields['iCalFileName'].required = False

        self.fields['lokasi'].required = False

        self.fields['lokasi'].required = False
        self.fields['lokasi'].required = False




        # ========== ADVANCE CONTROL PANEL (multiple <Inputs>) ========== !
        # 1. Input required
        # require = ['pname', 'pinsta_link', 'panak_ke', 'pnama_ayah', 'pnama_ibu',
        #     'ppicture', 'lname', 'linsta_link', 'lanak_ke', 'lnama_ayah', 'lnama_ibu',
        #     'lpicture', 'tanggal_akad','waktu_akad', 'waktu_selesai_akad', 'tempat_akad',
        #     'link_gmap_akad', 'tanggal_resepsi','waktu_resepsi', 'waktu_selesai_resepsi',
        #     'tempat_resepsi', 'link_gmap_resepsi', 'tanggal_unduhmantu','waktu_unduhmantu',
        #     'waktu_selesai_unduhmantu', 'tempat_unduhmantu','link_gmap_unduhmantu', 'video',
        #     'livestream',
        # ]
        # for field in require:
        #     self.fields[field].required = False

class MultiImageForm(forms.ModelForm):
    class Meta:
        model = MultiImage
        fields = ['image']
        widgets = {
            'image': ClearableFileInput(
                attrs={
                    'multiple': True,
                    'class': 'image',
                    'style': 'font-size: 15px',
                    'accept': 'image/png, image/jpeg'
               }),
        }

    # SUPER FUNCTION
    def __init__(self, *args, **kwargs):
        super(MultiImageForm, self).__init__(*args, **kwargs)

        # ========== CONTROL PANEL (Optional method to control ========== !
        # 1. Input required
        self.fields['image'].required = False


class SpecialInvitationForm(forms.ModelForm):
    class Meta:
        model = SpecialInvitation
        fields = ['name_invite']
        labels = {
            'name_invite': "Nama tamu",
        }
        widgets = {
            'name_invite': forms.TextInput(
                attrs={
                    'style': 'font-size: 13px',
                    'placeholder': 'Nama undangan',
                    'class': 'input'
                }
            ),
        }

    # SUPER FUNCTION
    def __init__(self, *args, **kwargs):
        super(SpecialInvitationForm, self).__init__(*args, **kwargs)

        # ========== CONTROL PANEL (Optional method to control ========== !
        # 1. Input required
        self.fields['name_invite'].required = True

class DompetForm(forms.ModelForm):

    nomor = forms.CharField(
        label='Nomor rekening',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'lokasi',
                'class': 'input',
                'style': 'font-size: 13px; text-transform: capitalize'
            }
        )
    )

    pemilik = forms.CharField(
        label='Atas nama',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Atas nama',
                'class': 'input',
                'style': 'font-size: 13px; text-transform: capitalize'
            }
        )
    )
    class Meta:
        model = Dompet
        fields = ['nomor', 'pemilik', 'rekening']
        # labels = {
        #     'name_invite': "Nama tamu",
        # }
        widgets = {
            'rekening': forms.Select(
                attrs={
                    'class': 'input',
                    'style': 'font-size: 13px',
                }
            ),
        }

    # SUPER FUNCTION
    def __init__(self, *args, **kwargs):
        super(DompetForm, self).__init__(*args, **kwargs)

        # ========== CONTROL PANEL (Optional method to control ========== !
        # 1. Input required
        # self.fields['nomor'].required = True



# ================== FORMSET =================== !
class BaseRegisterFormSet(BaseFormSet):
    def clean(self):
        super().clean()
        """Checks that no two articles have the same title."""
        if any(self.errors):
            # Don't bother validating the formset unless each form is valid on its own
            return
        name_invites = []
        for form in self.forms:
            cd = form.cleaned_data
            if cd:
                if self.can_delete and self._should_delete_form(form):
                    continue
                name_invite = cd['name_invite']
                if name_invite in name_invites:
                    raise ValidationError("Name in a set must have distinct title.")
                name_invites.append(name_invite)
                if name_invite == "":
                    raise ValidationError("This field cannot be empty!")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.queryset = SpecialInvitation.objects.filter(pk=id)
