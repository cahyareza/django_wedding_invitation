from django import forms
import re
import datetime
from django.forms import ClearableFileInput
from .models import Portofolio, MultiImage, SpecialInvitation, Dompet, Quote, Rekening, ThemeProduct, \
    Story, Acara, Theme, Fitur, Dana
from myproject.apps.order.models import OrderItem, Order
from django.core.validators import RegexValidator
from django.contrib.admin import widgets
from django.forms import BaseFormSet
from django.core.exceptions import ValidationError
from django.conf import settings

from urllib.parse import urlparse
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

# def validate_url(value):
#     if not value:
#         return  # Required error is done the field
#     obj = urlparse(value)
#     print(obj)
#     if (not ('www.google') in obj.netloc) or (not ('goo.gl') in obj.netloc):
#         raise ValidationError('Only urls from google map is allowed !')

# def validate_iframe(value):
#     if not value:
#         return  # Required error is done the field
#     obj = urlparse(value)
#     if not obj.netloc in ('<iframe src="https:'):
#         raise ValidationError('Only embed a google map is allowed !')

# def validate_iframe_video(value):
#     if not value:
#         return  # Required error is done the field
#     obj = urlparse(value)
#     print(obj)
#     if not ('<iframe') in obj.path:
#         raise ValidationError('Only embed a video is allowed !')

# ============== PORTO INFO ===============!
class PortoInfoForm(forms.ModelForm):
    # INFORMASI UNDANGAN
    porto_name = forms.CharField(
        label='Nama undangan', min_length=3, max_length=400,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Misal: Undangan Pernikahan Cahya dan Mila',
                'class': 'input',
                'style': 'font-size: 13px;'
            }
        )
    )

    description = forms.CharField(
        label='Informasi/deskripsi undangan', min_length=50, max_length=1000,
        required=True,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Misal: Merupakan undangan pernikahan kami. Besar harapan untuk kehadiran bapak/ibu, dan atas perhatianya diucapkan terimakasih',
                'class': 'textarea',
                'style': 'font-size: 13px',
            }
        )
    )

    class Meta:
        model = Portofolio
        fields = ["porto_name", "description"]

    # SUPER FUNCTION
    def __init__(self, *args, **kwargs):
        super(PortoInfoForm, self).__init__(*args, **kwargs)

        # ========== CONTROL PANEL (Optional method to control ========== !
        # 1. Select option
        # self.fields["panak_ke"].choices = [('', 'Pilih anak ke-'), ] + list(self.fields["panak_ke"].choices)[1:]
        # self.fields["lanak_ke"].choices = [('', 'Pilih anak ke-'), ] + list(self.fields["lanak_ke"].choices)[1:]

        # 2. Help text
        self.fields['description'].help_text = 'Jika ingin menggunakan deskripsi bawaan cukup dengan mengosongi form'

        # 1. Input required
        self.fields['description'].required = False
# ============== PORTO INFO END ===============!



# ============== PASANGAN ===============!
class PasanganForm(forms.ModelForm):
    # INFORMASI PASANGAN
    # PEREMPUAN
    pname = forms.CharField(
        label='Nama', min_length=3, max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nama lengkap',
                'class': 'input',
                'style': 'font-size: 13px; text-transform: capitalize'
            }
        )
    )

    pinsta_link = Lowercase(
        label='Username instagram',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Misal: cahya_rez',
                'class': 'input',
                'style': 'font-size: 13px;'
            }
        )
    )

    pnama_ayah = forms.CharField(
        label='Nama ayah', min_length=3, max_length=50,
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
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nama ibu',
                'class': 'input',
                'style': 'font-size: 13px; text-transform: capitalize'
            }
        )
    )

    # Photo (Upload photo)
    # ppicture = forms.FileField(
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


    # LAKI - LAKI
    lname = forms.CharField(
        label='Nama lengkap', min_length=3, max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nama',
                'class': 'input',
                'style': 'font-size: 13px; text-transform: capitalize'
            }
        )
    )

    linsta_link = Lowercase(
        label='Username instagram',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Misal: cahya_rez',
                'class': 'input',
                'style': 'font-size: 13px;'
            }
        )
    )

    lnama_ayah = forms.CharField(
        label='Nama ayah', min_length=3, max_length=50,
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
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nama ibu',
                'class': 'input',
                'style': 'font-size: 13px; text-transform: capitalize'
            }
        )
    )

    # Photo (Upload photo)
    # lpicture = forms.FileField(
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
        fields = ['pname', 'pinsta_link', 'panak_ke', 'pnama_ayah', 'pnama_ibu',
            'lname', 'linsta_link', 'lanak_ke', 'lnama_ayah', 'lnama_ibu']
        labels = {
            'panak_ke': "Anak Perempuan ke-",
            'lanak_ke': "Anak Laki-laki ke-",
        }

        # OUTSIDE WIDGET
        widgets = {
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
        super(PasanganForm, self).__init__(*args, **kwargs)

        # ========== CONTROL PANEL (Optional method to control ========== !
        # 1. Select option
        # self.fields["panak_ke"].choices = [('', 'Pilih anak ke-'), ] + list(self.fields["panak_ke"].choices)[1:]
        # self.fields["lanak_ke"].choices = [('', 'Pilih anak ke-'), ] + list(self.fields["lanak_ke"].choices)[1:]

        # 2. Help text
        self.fields['pinsta_link'].help_text = 'Jika instagram tidak ingin ditampilkan cukup dengan mengosongi form'
        self.fields['linsta_link'].help_text = 'Jika instagram tidak ingin ditampilkan cukup dengan mengosongi form'
        # self.fields['ppicture'].help_text = 'Pastikan ukuran image yang diupload 180 x 180px'
        # self.fields['lpicture'].help_text = 'Pastikan ukuran image yang diupload 180 x 180px'

        # 1. Input required
        self.fields['panak_ke'].required = True
        self.fields['lanak_ke'].required = True

        # self.fields['ppicture'].required = False
        # self.fields['lpicture'].required = False

    # ========== MeTHOD ========== !
    # 1) IMAGE (Maximum upload size = 2mb)
    def clean_ppicture(self):
        ppicture = self.cleaned_data.get('ppicture')
        if ppicture:
            if ppicture.size > 2 * 1048476:
                raise forms.ValidationError('Denied ! Maximum allowed is 2mb.')
            return ppicture
    def clean_lpicture(self):
        lpicture = self.cleaned_data.get('lpicture')
        if lpicture:
            if lpicture.size > 2 * 1048476:
                raise forms.ValidationError('Denied ! Maximum allowed is 2mb.')
            return lpicture
# ============== PASANGAN INFO END ===============!


# ============== PASANGAN PICTURE ===============!
class PasanganPictureForm(forms.ModelForm):
    # INFORMASI PASANGAN
    # PEREMPUAN
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

    x = forms.FloatField()
    y = forms.FloatField()
    width = forms.FloatField()
    height = forms.FloatField()

    x2 = forms.FloatField()
    y2 = forms.FloatField()
    width2 = forms.FloatField()
    height2 = forms.FloatField()

    class Meta:
        model = Portofolio
        fields = ['ppicture', 'lpicture', 'x', 'y', 'width', 'height', 'x2', 'y2', 'width2', 'height2']

    # SUPER FUNCTION
    def __init__(self, *args, **kwargs):
        super(PasanganPictureForm, self).__init__(*args, **kwargs)

        # ========== CONTROL PANEL (Optional method to control ========== !
        # 1. Select option
        # self.fields["panak_ke"].choices = [('', 'Pilih anak ke-'), ] + list(self.fields["panak_ke"].choices)[1:]
        # self.fields["lanak_ke"].choices = [('', 'Pilih anak ke-'), ] + list(self.fields["lanak_ke"].choices)[1:]

        # 2. Help text
        self.fields['ppicture'].help_text = 'Pastikan ukuran image yang diupload 180 x 180px'
        self.fields['lpicture'].help_text = 'Pastikan ukuran image yang diupload 180 x 180px'

        # 1. Input required
        self.fields['ppicture'].required = False
        self.fields['lpicture'].required = False
        self.fields['x'].required = False
        self.fields['y'].required = False
        self.fields['width'].required = False
        self.fields['height'].required = False
        self.fields['x2'].required = False
        self.fields['y2'].required = False
        self.fields['width2'].required = False
        self.fields['height2'].required = False

    # ========== MeTHOD ========== !
    # 1) IMAGE (Maximum upload size = 2mb)
    def clean_ppicture(self):
        ppicture = self.cleaned_data.get('ppicture')
        if ppicture:
            if ppicture.size > 2 * 1048476:
                raise forms.ValidationError('Denied ! Maximum allowed is 2mb.')
            return ppicture
    def clean_lpicture(self):
        lpicture = self.cleaned_data.get('lpicture')
        if lpicture:
            if lpicture.size > 2 * 1048476:
                raise forms.ValidationError('Denied ! Maximum allowed is 2mb.')
            return lpicture

    # def save(self):
    #     photo = super(PasanganPictureForm, self).save()
    #
    #     x = self.cleaned_data.get('x')
    #     y = self.cleaned_data.get('y')
    #     w = self.cleaned_data.get('width')
    #     h = self.cleaned_data.get('height')
    #
    #     x2 = self.cleaned_data.get('x2')
    #     y2 = self.cleaned_data.get('y2')
    #     w2 = self.cleaned_data.get('width2')
    #     h2 = self.cleaned_data.get('height2')
    #
    #     image1 = Image.open(photo.ppicture)
    #     cropped_image1 = image1.crop((x, y, w+x, h+y))
    #     resized_image1 = cropped_image1.resize((180, 180), Image.ANTIALIAS)
    #
    #     image2 = Image.open(photo.lpicture)
    #     cropped_image2 = image2.crop((x2, y2, w2+x2, h2+y2))
    #     resized_image2 = cropped_image2.resize((180, 180), Image.ANTIALIAS)
    #
    #     resized_image1.save(photo.ppicture.path)
    #     resized_image2.save(photo.lpicture.path)
    #
    #     return photo
# ============== PASANGAN PICTURE INFO END ===============!



# ============== ACARA ===============!
class AcaraForm(forms.ModelForm):
    tempat_acara = forms.CharField(
        label='Tempat acara', min_length=3, max_length=500,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Tempat acara',
                'class': 'input',
                'style': 'font-size: 13px; text-transform: capitalize; margin-bottom: 7px;'
            }
        )
    )

    nama_acara = forms.CharField(
        label='Nama acara',
        validators=[RegexValidator(r'^[a-zA-ZA-y\s]*$',
        message="Only letters is allowed !")],
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Misal: Akad/Resepsi/Unduh mantu',
                'class': 'input',
                'style': 'font-size: 13px; text-transform: capitalize; margin-bottom: 7px;'
            }
        )
    )

    link_gmap_acara = forms.URLField(
        label='Link google map acara',
        # validators=[validate_url],
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Link ke google maps',
                'class': 'textarea',
                'style': 'font-size: 13px; margin-bottom: 12px;',
            }
        )
    )

    class Meta:
        model = Acara
        fields = ['nama_acara', 'tanggal_acara', 'waktu_mulai_acara', 'waktu_selesai_acara', 'tempat_acara', 'link_gmap_acara']
        widgets = {
            # Tanggal akad
            'tanggal_acara': forms.DateInput(
                format='%d-%m-%Y',
                attrs={
                    'placeholder': 'dd-mm-yyyy',
                    'style': 'font-size: 13px; cursor: pointer; margin-bottom: 7px;',
                    # 'type': 'date',
                    'class': 'input',
                    # 'onkeydown': 'return false',  # Block typing inside field
                    # 'min': '2022-01-01',
                    # 'max': '2030-01-01',
                    'data-mask': '00-00-0000'
                },
            ),
            # Waktu akad
            'waktu_mulai_acara': forms.TimeInput(
                attrs={
                    'placeholder': 'Misal: 09:00',
                    'style': 'font-size: 13px; cursor: pointer; margin-bottom: 7px;',
                    'class': 'input',
                    'data-mask': '00:00'
                }
            ),
            # Waktu selesai akad
            'waktu_selesai_acara': forms.TimeInput(
                attrs={
                    'placeholder': 'Misal: 11:00',
                    'style': 'font-size: 13px; cursor: pointer; margin-bottom: 7px;',
                    'class': 'input',
                    'data-mask': '00:00'
                }
            ),
        }

    # SUPER FUNCTION
    def __init__(self, *args, **kwargs):
        super(AcaraForm, self).__init__(*args, **kwargs)

        # 1. Input required
        self.fields['tanggal_acara'].required = True
        self.fields['waktu_selesai_acara'].required = False

        # 2. Help text
        self.fields['waktu_selesai_acara'].help_text = 'Jika waktu selesai acara ingin ditampilkan "s/d selesai" cukup dengan mengosongi form'
        self.fields['link_gmap_acara'].help_text = 'Jika tidak ingin menampilkan link google maps acara cukup dengan mengosongi form'

# ============== ACARA END ===============!



# ============== QUOTE ===============!
class QuoteForm(forms.ModelForm):
    pembuka = forms.CharField(
        label='Kalimat Pembuka',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Kalimat',
                'class': 'input',
                'style': 'font-size: 13px; text-transform: capitalize'
            }
        )
    )

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
        fields = ['pembuka', 'ayat', 'kutipan']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # ========== ADVANCE CONTROL PANEL (multiple <Inputs>) ========== !
        # 1. Input required
        require = ['pembuka', 'ayat', 'kutipan']

        for field in require:
            self.fields[field].required = False

        # 2. Help text
        self.fields['pembuka'].help_text = 'Jika tidak ingin ada kalimat pembuka cukup dengan mengosongi form'
        self.fields['ayat'].help_text = 'Jika ingin menggunakan kalimat bawaan cukup dengan mengosongi form'
        self.fields['kutipan'].help_text = 'Jika ingin menggunakan kalimat bawaan cukup dengan mengosongi form'

# ============== QUOTE END ===============!



# ============== MOMENT ===============!
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
        self.fields['image'].help_text = 'Pastikan ukuran file image kurang dari 2MB'

    # ========== MeTHOD ========== !
    # 1) IMAGE (Maximum upload size = 2mb)
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > 2 * 1048476:
                raise forms.ValidationError('Denied ! Maximum allowed is 2mb.')
            return image

class PortoInfo2Form(forms.ModelForm):
    video = forms.CharField(
        label='Link video',
        required=True,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Misalkan : <iframe width="560" height="315" src="https://www.youtube.com/embed/MmjXcF0bmbw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
                'class': 'textarea',
                'style': 'font-size: 13px',
            }
        )
    )
    livestream = forms.URLField(
        label='Link livestream',
        required=True,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Misalkan : https://zoom.us/j/5551112222',
                'class': 'textarea',
                'style': 'font-size: 13px',
            }
        )
    )

    kata_live_streaming = forms.CharField(
        label='Kalimat live streaming', min_length=30, max_length=1000,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Tuliskan kalimat live streaming',
                'class': 'textarea',
                'style': 'font-size: 13px',
            }
        )
    )

    kata_moment = forms.CharField(
        label='Kalimat moment', min_length=30, max_length=1000,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Tuliskan kalimat moment',
                'class': 'textarea',
                'style': 'font-size: 13px',
            }
        )
    )
    class Meta:
        model = Portofolio
        fields = ["video", "livestream", "kata_live_streaming", "kata_moment"]

    # SUPER FUNCTION
    def __init__(self, *args, **kwargs):
        super(PortoInfo2Form, self).__init__(*args, **kwargs)

        # 1. Input required
        self.fields['video'].required = False
        self.fields['livestream'].required = False
        self.fields['kata_live_streaming'].required = False
        self.fields['kata_moment'].required = False

        # 2. Help text
        self.fields['kata_live_streaming'].help_text = 'Jika ingin menggunakan kalimat bawaan cukup dengan mengosongi form'
        self.fields['kata_moment'].help_text = 'Jika ingin menggunakan kalimat bawaan cukup dengan mengosongi form'
        self.fields['video'].help_text = 'Cukup mengosongi form jika tidak ada video'
        self.fields['livestream'].help_text = 'Cukup mengosongi form jika tidak ada livestream'


# ============== MOMENT END ===============!



# ============== STORY ===============!
class StoryForm(forms.ModelForm):
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
    cerita = forms.CharField(
        label='Cerita', min_length=5, max_length=1000,
        required=True,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Cerita',
                'class': 'textarea',
                'style': 'font-size: 13px',
            }
        )
    )
    year = forms.CharField(
        label='Tahun', min_length=4, max_length=5,
        validators=[RegexValidator(r'^[0-9]*$',
        message="Only numbers is allowed !")],
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Tahun',
                'class': 'input',
                'style': 'font-size: 13px;'
            }
        )
    )
    class Meta:
        model = Story
        fields = ['year', 'cerita', 'image']
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
        super(StoryForm, self).__init__(*args, **kwargs)

        # ========== CONTROL PANEL (Optional method to control ========== !
        # 1. Input required
        self.fields['year'].required = False
        self.fields['cerita'].required = False
        self.fields['image'].required = True

        # 2. Help text
        self.fields['year'].help_text = 'Cukup mengosongi form jika tidak ada story'
        self.fields['cerita'].help_text = 'Cukup mengosongi form jika tidak ada story'
        self.fields['image'].help_text = 'Cukup mengosongi form jika tidak ada story'

    # ========== MeTHOD ========== !
    # 1) IMAGE (Maximum upload size = 2mb)
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > 2 * 1048476:
                raise forms.ValidationError('Denied ! Maximum allowed is 2mb.')
            return image

# ============== STORY END ===============!



# ============== NAVIGASI ===============!
class NavigasiForm(forms.ModelForm):
    link_iframe = forms.CharField(
        label='Link embed map tempat acara di google map', min_length=20, max_length=1000,
        required=True,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Misal : <div class="mapouter"><div class="gmap_canvas"><iframe ......',
                'class': 'textarea',
                'style': 'font-size: 13px',
            }
        )
    )
    link_gmap = forms.URLField(
        label='Link tempat acara di google maps', min_length=20, max_length=1000,
        # validators=[validate_url],
        required=True,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Misal : https://goo.gl/maps/C6bdeQVQPvYqr1mw8',
                'class': 'textarea',
                'style': 'font-size: 13px',
            }
        )
    )
    class Meta:
        model = Portofolio
        fields = ["link_iframe", "link_gmap"]

# ============== NAVIGASI END ===============!





# ============== DOMPET ===============!
class PortoAlamatDompet(forms.ModelForm):
    alamat_rumah = forms.CharField(
        label='Alamat pengiriman bingkisan', min_length=30, max_length=1000,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Alamat',
                'class': 'textarea',
                'style': 'font-size: 13px',
            }
        )
    )
    class Meta:
        model = Portofolio
        fields = ["alamat_rumah"]

    # SUPER FUNCTION
    def __init__(self, *args, **kwargs):
        super(PortoAlamatDompet, self).__init__(*args, **kwargs)
        # 1. Input required
        self.fields['alamat_rumah'].required = False

        # 2. Help text
        self.fields['alamat_rumah'].help_text = 'Jika tidak ingin menampilkan alamat cukup dengan mengosongi form'

class DompetForm(forms.ModelForm):
    bar_code = forms.FileField(
        label="Foto barcode",
        widget=forms.ClearableFileInput(
            attrs={
                'placeholder': 'Select a picture',
                'class': 'image',
                'style': 'font-size: 15px',
                'accept': 'image/png, image/jpeg'
            }
        )
    )
    nomor = forms.CharField(
        label='Nomor rekening',
        validators=[RegexValidator(r'^[0-9]*$',
        message="Only numbers is allowed !")],
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
        validators=[RegexValidator(r'^[a-zA-ZA-y\s]*$',
        message="Only letters is allowed !")],
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
        fields = ['pemilik', 'rekening', 'bar_code', 'nomor']
        labels = {
            'rekening': "Nama bank",
        }

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
        # 1. Select option
        # self.fields["rekening"].choices = [('', 'Pilih bank'),] + list(self.fields["rekening"].choices)[1:]

        # 2. Input required
        self.fields['rekening'].required = True
        self.fields['bar_code'].required = False

        # 3. help_text
        self.fields['nomor'].help_text = 'Cukup mengosongi form jika tidak ada dompet'
        self.fields['pemilik'].help_text = 'Cukup mengosongi form jika tidak ada dompet'
        self.fields['rekening'].help_text = 'Cukup mengosongi form jika tidak ada dompet'
        self.fields['bar_code'].help_text = 'Cukup mengosongi form jika tidak ada barcode'
# ============== DOMPET END ===============!





# ============== SPECIAL INVIT ===============!
class SpecialInvitationForm(forms.ModelForm):
    name_invite = forms.CharField(
        label='Nama tamu', min_length=3, max_length=50,
        validators=[RegexValidator(r'^[a-zA-ZA-y\s]*$',
        message="Only letters is allowed !")],
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nama undangan',
                'class': 'input',
                'style': 'font-size: 13px; text-transform: capitalize; margin-bottom: 7px;'
            }
        )
    )
    class Meta:
        model = SpecialInvitation
        fields = ['name_invite']


    # SUPER FUNCTION
    def __init__(self, *args, **kwargs):
        super(SpecialInvitationForm, self).__init__(*args, **kwargs)

        # ========== CONTROL PANEL (Optional method to control ========== !
        # 1. Input required
        self.fields['name_invite'].required = True

        # 2. help_text
        self.fields['name_invite'].help_text = 'Cukup mengosongi form jika tidak ada tamu khusus'

class PortoInfo3Form(forms.ModelForm):
    kata_special_invite = forms.CharField(
        label='Kalimat invitation', min_length=30, max_length=1000,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Tuliskan kalimat invitation',
                'class': 'textarea',
                'style': 'font-size: 13px',
            }
        )
    )
    class Meta:
        model = Portofolio
        fields = ["kata_special_invite"]

    # SUPER FUNCTION
    def __init__(self, *args, **kwargs):
        super(PortoInfo3Form, self).__init__(*args, **kwargs)
        # 1. Input required
        self.fields['kata_special_invite'].required = False

        # 2. Help text
        self.fields['kata_special_invite'].help_text = 'Jika ingin menggunakan kalimat bawaan cukup dengan mengosongi form'

# ============== SPECIAL INVIT END ===============!



from django.utils.safestring import mark_safe

class CustomChoiceField(forms.ModelChoiceField):

    def label_from_instance(self, obj):
        if obj.theme_picture:
            image = obj.theme_picture.url
            title = obj.name
            preview = obj.preview_url

            label = '<div class="card-image px-3 py-1">' \
                    '<figure class ="image is-3by5">' \
                    '<img src="%s" />' \
                    '</figure>' \
                    '</div>' \
                    '<p class="subtitle">%s</p>'\
                    '<a href="%s" class="button is-danger mb-3" target="_blank">Preview</a>'% (image, title, preview)

            return mark_safe(label)

# ============== THEME ===============!
class ThemeProductForm(forms.ModelForm):
    # theme = forms.ModelChoiceField(queryset=Theme.objects.all(), to_field_name='slug', widget=forms.CheckboxSelectMultiple, required=False)
    # order = Order.objects.filter(user=user).first()
    # orderitem = OrderItem.objects.get(order=order)
    # theme_filter = Theme.objects.filter(fitur=orderitem.product)
    class Meta:
        model = ThemeProduct
        fields = ['theme']
        labels = {
            'theme': "Tema",
        }
        # widgets = {
        #     'theme': forms.RadioSelect()
        # }

    # SUPER FUNCTION
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(ThemeProductForm, self).__init__(*args, **kwargs)
        if str(OrderItem.objects.get(order=Order.objects.filter(user=user).first()).product) == "SILVER":
            self.fields['theme'].queryset = Theme.objects.filter(fitur=OrderItem.objects.get(order=Order.objects.filter(user=user).first()).product)
        elif str(OrderItem.objects.get(order=Order.objects.filter(user=user).first()).product) == "PLATINUM":
            self.fields['theme'].queryset = Theme.objects.all().exclude(fitur=3)
        else:
            self.fields['theme'].queryset = Theme.objects.all()
        # ========== CONTROL PANEL (Optional method to control ========== !
        # 1. Input required
        self.fields['theme'].required = True

        # 2. Select option
        # self.fields["theme"].choices = list(self.fields["theme"].choices)[1:]

        self.fields["theme"].widget.template_name = "portofolio/widgets/theme.html"

    theme = CustomChoiceField(queryset=None, widget=forms.RadioSelect,)
    # def clean_my_field(self):
    #     if self.cleaned_data['theme']:
    #         if len(self.cleaned_data['theme']) != 1:
    #             raise forms.ValidationError('Just select 1.')
    #         return self.cleaned_data['theme']
# ============== THEME END ===============!




# ============== COVER ===============!
# class CustomClearableFileInput(ClearableFileInput):
#     template_name = "django/forms/widgets/custom_clearable_file_input.html"

class PortoInfo4Form(forms.ModelForm):
    open_background = forms.FileField(
        label="Foto open background",
        widget=forms.ClearableFileInput(
            attrs={
                'placeholder': 'Select a picture',
                'class': 'image',
                'style': 'font-size: 15px',
                'accept': 'image/png, image/jpeg'
            }
        )
    )
    cover_background = forms.FileField(
        label="Foto cover background",
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
        fields = ["cover_background", "open_background"]

    # SUPER FUNCTION
    def __init__(self, *args, **kwargs):
        super(PortoInfo4Form, self).__init__(*args, **kwargs)

        # ========== CONTROL PANEL (Optional method to control ========== !
        # 1. Input required
        self.fields['cover_background'].required = False
        self.fields['open_background'].required = False

        # 2. Help text
        self.fields['cover_background'].help_text = 'Jika tidak ingin menggunakan foto sebagai background cukup kosongi form'
        self.fields['open_background'].help_text = 'Jika tidak ingin menggunakan foto sebagai background cukup kosongi form'

# ============== COVER END ===============!




# ============== CALENDER ===============!
class CalenderForm(forms.ModelForm):
    location_countdown = forms.CharField(
        label='Alamat acara', min_length=10, max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Alamat acara',
                'class': 'input',
                'style': 'font-size: 13px',
            }
        )
    )
    class Meta:
        model = Portofolio
        fields = ["location_countdown", "tanggal_countdown", "waktu_countdown", "waktu_countdown_selesai",\
                  "timeZone"]
        labels = {
            'tanggal_countdown': "Tanggal acara",
            'waktu_countdown': "Waktu acara",
            'waktu_countdown_selesai': "Waktu selesai acara",

        }

        # OUTSIDE WIDGET
        widgets = {
            # Timezone
            'timeZone': forms.Select(
                attrs={
                    'class': 'input',
                    'style': 'font-size: 13px',
                }
            ),
            # Tanggal countdown
            'tanggal_countdown': forms.DateInput(
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
            # Waktu countdown
            'waktu_countdown': forms.TimeInput(
                attrs={
                    'placeholder': 'Misal: 09:00',
                    'style': 'font-size: 13px; cursor: pointer;',
                    'class': 'input',
                    'data-mask': '00:00'
                }
            ),
            # Waktu countdown
            'waktu_countdown_selesai': forms.TimeInput(
                attrs={
                    'placeholder': 'Misal: 09:00',
                    'style': 'font-size: 13px; cursor: pointer;',
                    'class': 'input',
                    'data-mask': '00:00'
                }
            ),
        }

    # SUPER FUNCTION
    def __init__(self, *args, **kwargs):
        super(CalenderForm, self).__init__(*args, **kwargs)

        # ========== CONTROL PANEL (Optional method to control ========== !
        # 1. Input required
        self.fields['location_countdown'].required = True
        self.fields['tanggal_countdown'].required = True
        self.fields['waktu_countdown'].required = True
        self.fields['waktu_countdown_selesai'].required = True
        self.fields['timeZone'].required = True

    # ========== MeTHOD ========== !
    def clean_tanggal_countdown(self):
        tanggal_countdown = self.cleaned_data['tanggal_countdown']
        if tanggal_countdown:
            if tanggal_countdown < datetime.date.today():
                raise forms.ValidationError('Tanggal acara usang!')
            return tanggal_countdown

# ============== CALENDER END ===============!



# ============== TRACK ===============!
class PortoInfo5Form(forms.ModelForm):
    class Meta:
        model = Portofolio
        fields = ["track"]
        widgets = {
            # Timezone
            'track': forms.Select(
                attrs={
                    'class': 'input',
                    'style': 'font-size: 13px',
                }
            ),
        }

    # SUPER FUNCTION
    def __init__(self, *args, **kwargs):
        super(PortoInfo5Form, self).__init__(*args, **kwargs)

        # ========== CONTROL PANEL (Optional method to control ========== !
        # 1. Input required
        self.fields['track'].required = True

        # 2. Help text
        # self.fields['cover_background'].help_text = 'Jika tidak ingin menggunakan foto sebagai background cukup kosongi form'
# ============== TRACK END ===============!

# # ============== DANA ===============!
# class CustomChoiceFieldDiTransfer(forms.ModelChoiceField):
#     pass
#
# class DanaForm(forms.ModelForm):
#     nama = forms.CharField(
#         label='Nama', min_length=3, max_length=50,
#         validators=[RegexValidator(r'^[a-zA-ZA-y\s]*$',
#         message="Only letters is allowed !")],
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Nama',
#                 'class': 'input',
#                 'style': 'font-size: 13px; text-transform: capitalize; margin-bottom: 7px;'
#             }
#         )
#     )
#     ditransfer_ke = forms.CharField(
#         label='Ditransfer ke-',
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Ditransfer ke-',
#                 'class': 'input',
#                 'style': 'font-size: 13px margin-bottom: 7px;'
#             }
#         )
#     )
#     jumlah = forms.CharField(
#         label='Jumlah', min_length=3, max_length=50,
#         validators=[RegexValidator(r'^[0-9]*$',
#         message="Only numbers is allowed !")],
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Jumlah',
#                 'class': 'input',
#                 'style': 'font-size: 13px; margin-bottom: 7px;'
#             }
#         )
#     )
#     pesan = forms.CharField(
#         label='Pesan', max_length=100,
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Pesan',
#                 'class': 'input',
#                 'style': 'font-size: 13px; text-transform: capitalize; margin-bottom: 7px;'
#             }
#         )
#     )
#     class Meta:
#         model = Dana
#         fields = ["nama", "jumlah", "pesan", "ditransfer_ke"]
#
#
#         # widgets = {
#         #     'ditransfer_ke': forms.Select(
#         #         attrs={
#         #             'class': 'input',
#         #             'style': 'font-size: 13px',
#         #         }
#         #     ),
#         # }
#
#     # SUPER FUNCTION
#     # def __init__(self, *args, **kwargs):
#     #     user = kwargs.pop('user')
#     #     super(DanaForm, self).__init__(*args, **kwargs)
#     #     self.fields['ditransfer_ke'].queryset = Dompet.objects.filter(portofolio=Portofolio.objects.get(user=user))
#
#     # ditransfer_ke = forms.ModelChoiceField(queryset=None, widget=forms.Select,)
# # ============== DANA ===============!


# ================== FORMSET =================== !
class BaseRegisterFormSet(BaseFormSet):
    def clean(self):
        super().clean()
        """Checks that no two articles have the same title."""
        if any(self.errors):
            # Don't bother validating the formset unless each form is valid on its own
            return
        for form in self.forms:
            if self.can_delete and self._should_delete_form(form):
                continue
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.queryset = SpecialInvitation.objects.filter(pk=id)
# ================== FORMSET END =================== !
