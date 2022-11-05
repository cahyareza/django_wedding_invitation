from django import forms
import re
from django.forms import ClearableFileInput
from .models import Portofolio, MultiImage, SpecialInvitation, Dompet, Quote, Rekening, ThemeProduct
from django.core.validators import RegexValidator
from django.contrib.admin import widgets
from django.forms import BaseFormSet
from django.core.exceptions import ValidationError
from django.conf import settings

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
                'placeholder': 'Nama lengkap',
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
        label='Nama lengkap', min_length=3, max_length=50,
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
        label='Link google map lokasi akad',
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
        label='Link google map lokasi resepsi',
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
        label='Link google map lokasi unduh mantu',
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
        required=True,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Link embed video',
                'class': 'textarea',
                'style': 'font-size: 13px',
            }
        )
    )

    livestream = forms.CharField(
        label='Link livestream',
        required=True,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Link livestream',
                'class': 'textarea',
                'style': 'font-size: 13px',
            }
        )
    )

    # livestream = forms.CharField(
    #     label='Link livestream',
    #     widget=forms.TextInput(
    #         attrs={
    #             'placeholder': 'Link livestream',
    #             'class': 'input',
    #             'style': 'font-size: 13px;'
    #         }
    #     )
    # )

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
        label='Informasi/deskripsi undangan', min_length=50, max_length=1000,
        required=True,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Misal: Merupakan undangan online untuk pernikahan kami(Cahya dan Mila). Besar harapan untuk kehadiran bapak/ibu, dan atas perhatianya diucapkan terimakasih',
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
        label='Link embed map tempat acara di google map', min_length=50, max_length=1000,
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
        label='Link tempat acara di google maps', min_length=50, max_length=1000,
        required=True,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Link google maps',
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

    # tanggal_akad = forms.DateField(
    #     label='Tanggal akad',
    #     input_formats=['%d-%m-%Y'],
    #     widget=forms.DateInput(
    #         format='%d-%m-%Y',
    #         attrs = {
    #             'style': 'font-size: 13px; cursor: pointer;',
    #             # 'type': 'date',
    #             'class': 'input',
    #             # 'onkeydown': 'return false',  # Block typing inside field
    #             # 'min': '2022-01-01',
    #             # 'max': '2030-01-01'
    #         },
    #     )
    # )




    class Meta:
        model = Portofolio
        fields = "__all__"
        labels = {
            'tanggal_unduhmantu': "Tanggal unduh mantu",
            'waktu_unduhmantu': "Waktu unduh mantu",
            'waktu_selesai_unduhmantu': "Waktu selesai unduh mantu",
            'panak_ke': "Anak ke-",
            'lanak_ke': "Anak ke-",

        }

        # OUTSIDE WIDGET
        widgets = {
            # Tanggal akad
            'tanggal_akad': forms.DateInput(
                format='%d-%m-%Y',
                attrs={
                    'placeholder': 'dd-mm-yyyy',
                    'style': 'font-size: 13px; cursor: pointer;',
                    # 'type': 'date',
                    'class': 'input',
                    # 'onkeydown': 'return false',  # Block typing inside field
                    # 'min': '2022-01-01',
                    # 'max': '2030-01-01',
                    'data-mask': '00-00-0000'
                },
            ),
            # Waktu akad
            'waktu_akad': forms.TimeInput(
                attrs={
                    'placeholder': 'Misal: 09:00',
                    'style': 'font-size: 13px; cursor: pointer;',
                    'class': 'input',
                    'data-mask': '00:00'
                }
            ),
            # Waktu selesai akad
            'waktu_selesai_akad': forms.TimeInput(
                attrs={
                    'placeholder': 'Misal: 11:00',
                    'style': 'font-size: 13px; cursor: pointer;',
                    'class': 'input',
                    'data-mask': '00:00'
                }
            ),
            # Tanggal resepsi
            'tanggal_resepsi': forms.DateInput(
                format='%d-%m-%Y',
                attrs={
                    'placeholder': 'dd-mm-yyyy',
                    'style': 'font-size: 13px; cursor: pointer;',
                    # 'type': 'date',
                    'class': 'input',
                    # 'onkeydown': 'return false',  # Block typing inside field
                    # 'min': '2022-01-01',
                    # 'max': '2030-01-01',
                    'data-mask': '00-00-0000'
                },
            ),
            # Waktu resepsi
            'waktu_resepsi': forms.TimeInput(
                attrs={
                    'placeholder': 'Misal: 13:00',
                    'style': 'font-size: 13px; cursor: pointer;',
                    'class': 'input',
                    'data-mask': '00:00'
                }
            ),
            # Datetime resepsi
            'datetime_resepsi': forms.DateTimeInput(
                format='%d-%m-%Y %H:%M',
                attrs={
                    'placeholder': 'dd-mm-yyyy hh:mm',
                    'style': 'font-size: 13px; cursor: pointer;',
                    # 'type': 'date',
                    'class': 'input',
                    # 'onkeydown': 'return false',  # Block typing inside field
                    # 'min': '2022-01-01',
                    # 'max': '2030-01-01',
                    'data-mask': '00-00-0000 00:00'
                },
            ),
            # Waktu selesai resepsi
            'waktu_selesai_resepsi': forms.TimeInput(
                attrs={
                    'placeholder': 'Misal: 15:00',
                    'style': 'font-size: 13px; cursor: pointer;',
                    'class': 'input',
                    'data-mask': '00:00'
                }
            ),
            # Tanggal unduh mantu
            'tanggal_unduhmantu': forms.DateInput(
                format='%d-%m-%Y',
                attrs={
                    'placeholder': 'dd-mm-yyyy',
                    'style': 'font-size: 13px; cursor: pointer;',
                    # 'type': 'date',
                    'class': 'input',
                    # 'onkeydown': 'return false',  # Block typing inside field
                    # 'min': '2022-01-01',
                    # 'max': '2030-01-01',
                    'data-mask': '00-00-0000'
                },
            ),
            # Waktu unduh mantu
            'waktu_unduhmantu': forms.TimeInput(
                attrs={
                    'placeholder': 'Misal: 09:00',
                    'style': 'font-size: 13px; cursor: pointer;',
                    'class': 'input',
                    'data-mask': '00:00'
                }
            ),
            # Waktu selesai unduh mantu
            'waktu_selesai_unduhmantu': forms.TimeInput(
                attrs={
                    'placeholder': 'Misal: 12:00',
                    'style': 'font-size: 13px; cursor: pointer;',
                    'class': 'input',
                    'data-mask': '00:00'
                }
            ),
            # Tanggal acara di calender
            'startDate': forms.DateInput(
                format='%d-%m-%Y',
                attrs={
                    'placeholder': 'dd-mm-yyyy',
                    'style': 'font-size: 13px; cursor: pointer;',
                    # 'type': 'date',
                    'class': 'input',
                    # 'onkeydown': 'return false',  # Block typing inside field
                    # 'min': '2022-01-01',
                    # 'max': '2030-01-01',
                    'data-mask': '00-00-0000'
                },
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
            'panak_ke': forms.Select(
                attrs={
                    'class': 'input',
                    'style': 'font-size: 13px',
                }
            ),
            'lanak_ke': forms.Select(
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

        self.fields['user'].required = False
        self.fields['slug'].required = False

        self.fields['datetime_resepsi'].required = False

        # ========== CONTROL PANEL (Optional method to control ========== !
        # 1. Select option
        self.fields["panak_ke"].choices = [('', 'Pilih anak ke-'), ] + list(self.fields["panak_ke"].choices)[1:]
        self.fields["lanak_ke"].choices = [('', 'Pilih anak ke-'), ] + list(self.fields["lanak_ke"].choices)[1:]

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

    # ========== MeTHOD ========== !
    # 1) IMAGE (Maximum upload size = 2mb)
    def clean_ppicture(self):
        ppicture = self.cleaned_data.get('ppicture')
        if ppicture.size > 2 * 1048476:
            raise forms.ValidationError('Denied ! Maximum allowed is 2mb.')
        return ppicture
    def clean_lpicture(self):
        lpicture = self.cleaned_data.get('lpicture')
        if lpicture.size > 2 * 1048476:
            raise forms.ValidationError('Denied ! Maximum allowed is 2mb.')
        return lpicture


class MultiImageForm(forms.ModelForm):
    image = forms.FileField(
        label="Foto moment",
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
        model = MultiImage
        fields = ['image']
        # widgets = {
        #     'image': ClearableFileInput(
        #         attrs={
        #             'multiple': True,
        #             'class': 'image',
        #             'style': 'font-size: 15px',
        #             'accept': 'image/png, image/jpeg'
        #        }),
        # }

    # SUPER FUNCTION
    def __init__(self, *args, **kwargs):
        super(MultiImageForm, self).__init__(*args, **kwargs)

        # ========== CONTROL PANEL (Optional method to control ========== !
        # 1. Input required
        self.fields['image'].required = False

        # 2. Help text
        # self.fields['image'].help_text = 'Note: Upload dengan memilih beberapa image secara langsung'

    # ========== MeTHOD ========== !
    # 1) IMAGE (Maximum upload size = 2mb)
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image.size > 2 * 1048476:
            raise forms.ValidationError('Denied ! Maximum allowed is 2mb.')
        return image

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
        labels = {
            'rekening': "Nama bank",
        }

        rekenings = Rekening.objects.all()
        DAFTAR_BANK = [ rekening.bank for rekening in rekenings]

        widgets = {
            'rekening': forms.Select(
                choices=DAFTAR_BANK,
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
        # 1. Select option
        self.fields["rekening"].choices = [('', 'Pilih bank'),] + list(self.fields["rekening"].choices)[1:]

class QuoteForm(forms.ModelForm):
    # INFORMASI QUOTE
    ayat = forms.CharField(
        label='Nama ayat/kutipan',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nama ayat/kutipan',
                'class': 'input',
                'style': 'font-size: 13px; text-transform: capitalize'
            }
        )
    )

    kutipan = forms.CharField(
        label='Kutipan', min_length=50, max_length=1000,
        required=True,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Kutipan',
                'class': 'textarea',
                'style': 'font-size: 13px',
            }
        )
    )

    class Meta:
        model = Quote
        fields = ['ayat', 'kutipan']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # ========== ADVANCE CONTROL PANEL (multiple <Inputs>) ========== !
        # 1. Input required
        require = ['ayat', 'kutipan',
        ]
        for field in require:
            self.fields[field].required = False

class ThemeProductForm(forms.ModelForm):
    class Meta:
        model = ThemeProduct
        fields = ['theme']
        labels = {
            'theme': "Tema",
        }
        widgets = {
            'theme': forms.Select(
                attrs={
                    'class': 'input',
                    'style': 'font-size: 13px',
                }
            ),
        }

    # SUPER FUNCTION
    def __init__(self, *args, **kwargs):
        super(ThemeProductForm, self).__init__(*args, **kwargs)

        # ========== CONTROL PANEL (Optional method to control ========== !
        # 1. Input required
        # self.fields['fitur'].required = False
        # self.fields['portofolio'].required = False

        # 2. Select option
        self.fields["theme"].choices = [('', 'Pilih tema'),] + list(self.fields["theme"].choices)[1:]


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
