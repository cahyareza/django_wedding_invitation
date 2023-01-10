from PIL import Image
from django import forms
from django.core.files import File
from .models import Photo, Photo2

class PhotoForm(forms.ModelForm):
    x = forms.FloatField()
    y = forms.FloatField()
    width = forms.FloatField()
    height = forms.FloatField()

    class Meta:
        model = Photo
        fields = ('file', 'x', 'y', 'width', 'height', )

    # # SUPER FUNCTION
    # def __init__(self, *args, **kwargs):
    #     super(PhotoForm, self).__init__(*args, **kwargs)
    #
    #     # ========== CONTROL PANEL (Optional method to control ========== !
    #     # 1. Select option
    #     # self.fields["rekening"].choices = [('', 'Pilih bank'),] + list(self.fields["rekening"].choices)[1:]
    #
    #     # 2. Input required
    #     self.fields['file'].required = False
    #     self.fields['x'].required = False
    #     self.fields['y'].required = False
    #     self.fields['width'].required = False
    #     self.fields['height'].required = False

    def save(self):
        photo = super(PhotoForm, self).save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')

        image = Image.open(photo.file)
        cropped_image = image.crop((x, y, w+x, h+y))
        resized_image = cropped_image.resize((200, 200), Image.ANTIALIAS)
        resized_image.save(photo.file.path)

        return photo

class PhotoForm2(forms.ModelForm):
    x2 = forms.FloatField()
    y2 = forms.FloatField()
    width2 = forms.FloatField()
    height2 = forms.FloatField()

    class Meta:
        model = Photo2
        fields = ('file2', 'x2', 'y2', 'width2', 'height2', )

    # # SUPER FUNCTION
    # def __init__(self, *args, **kwargs):
    #     super(PhotoForm2, self).__init__(*args, **kwargs)
    #
    #     # ========== CONTROL PANEL (Optional method to control ========== !
    #     # 1. Select option
    #     # self.fields["rekening"].choices = [('', 'Pilih bank'),] + list(self.fields["rekening"].choices)[1:]
    #
    #     # 2. Input required
    #     self.fields['file2'].required = False
    #     self.fields['x'].required = False
    #     self.fields['y'].required = False
    #     self.fields['width'].required = False
    #     self.fields['height'].required = False

    def save(self):
        photo = super(PhotoForm2, self).save()

        x = self.cleaned_data.get('x2')
        y = self.cleaned_data.get('y2')
        w = self.cleaned_data.get('width2')
        h = self.cleaned_data.get('height2')

        image = Image.open(photo.file2)
        cropped_image = image.crop((x, y, w+x, h+y))
        resized_image = cropped_image.resize((200, 200), Image.ANTIALIAS)
        resized_image.save(photo.file2.path)

        return photo