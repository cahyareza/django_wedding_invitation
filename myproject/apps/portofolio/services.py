from django.conf import settings

class AcaraFormSESSION():
    '''
    Akan membuat session dengan keys cart dan salah satu valuenya product_id
    "cart" ={
    "product_id": {
        'price': $9.99,
        'quantity': 1,
        'id': nike
        }
    }

    Kemudian pada session ini bisa menambahkan di session cart menggunakan prinsip2 dictionary data type
    '''

    def __init__(self, request):
        self.session = request.session
        # initialize session cart
        acaraform = self.session.get(settings.ACARAFORM_SESSION_ID)

        # jika tidak bukan cart
        if not acaraform:
            acaraform = self.session[settings.ACARAFORM_SESSION_ID] = {}

        self.acaraform = acaraform


    def add(self, id, form):
        form_id = str(id)

        if form_id not in self.acaraform:
            self.acaraform[form_id] = {'tempat_acara': form.cleaned_data.get('tempat_acara'),
                'nama_acara': form.cleaned_data.get('nama_acara'),
                'link_gmap_acara': form.cleaned_data.get('link_gmap_acara'),
                'tanggal_acara': form.cleaned_data.get('tanggal_acara'),
                'waktu_mulai_acara': form.cleaned_data.get('waktu_mulai_acara'),
                'waktu_selesai_acara': form.cleaned_data.get('waktu_selesai_acara'),
            }


        self.save()
        print(self.acaraform)

    def __iter__(self):
        acaraform = self.acaraform.copy()
        for item in acaraform.values():
            yield item

    def __str__(self):
        acaraform = self.acaraform.copy()
        return f"<acaraformObject {acaraform}>"

    def save(self):
        self.session.modified = True

    def clear(self):
        del self.session[settings.ACARAFORM_SESSION_ID]
        self.session.modified = True

class PasanganFormSESSION():
    '''
    Akan membuat session dengan keys cart dan salah satu valuenya product_id
    "cart" ={
    "product_id": {
        'price': $9.99,
        'quantity': 1,
        'id': nike
        }
    }

    Kemudian pada session ini bisa menambahkan di session cart menggunakan prinsip2 dictionary data type
    '''

    def __init__(self, request):
        self.session = request.session
        # initialize session cart
        pasanganform = self.session.get(settings.PASANGAN_SESSION_ID)

        # jika tidak bukan cart
        if not pasanganform:
            pasanganform = self.session[settings.PASANGAN_SESSION_ID] = {}

        self.pasanganform = pasanganform


    def add(self, id, form):
        form_id = str(id)

        if form_id not in self.pasanganform:
            self.pasanganform[form_id] = {'pname': form.cleaned_data.get('pname'),
            'pinsta_link': form.cleaned_data.get('pinsta_link'),
            'panak_ke': form.cleaned_data.get('panak_ke'),
            'pnama_ayah': form.cleaned_data.get('pnama_ayah'),
            'pnama_ibu': form.cleaned_data.get('pnama_ibu'),
            'ppicture': form.cleaned_data.get('ppicture'),
            'lname': form.cleaned_data.get('lname'),
            'linsta_link': form.cleaned_data.get('linsta_link'),
            'lanak_ke': form.cleaned_data.get('lanak_ke'),
            'lnama_ayah': form.cleaned_data.get('lnama_ayah'),
            'lnama_ibu': form.cleaned_data.get('lnama_ibu'),
            'lpicture': form.cleaned_data.get('lpicture'),
        }


        self.save()
        print(self.pasanganform)

    def __iter__(self):
        pasanganform = self.pasanganform.copy()
        for item in pasanganform.values():
            yield item

    def __call__(self):
        return self.pasanganform.values()

    def __str__(self):
        return f"<pasanganformObject {self.pasanganform}>"

    def save(self):
        self.session.modified = True

    def clear(self):
        del self.session[settings.PASANGAN_SESSION_ID]
        self.session.modified = True

class MultiImageFormSESSION():
    '''
    Akan membuat session dengan keys cart dan salah satu valuenya product_id
    "cart" ={
    "product_id": {
        'price': $9.99,
        'quantity': 1,
        'id': nike
        }
    }

    Kemudian pada session ini bisa menambahkan di session cart menggunakan prinsip2 dictionary data type
    '''

    def __init__(self, request):
        self.session = request.session
        # initialize session cart
        multiimageform = self.session.get(settings.MULTIIMAGE_SESSION_ID)

        # jika tidak bukan cart
        if not multiimageform:
            multiimageform = self.session[settings.MULTIIMAGE_SESSION_ID] = {}

        self.multiimageform = multiimageform


    def add(self, id, form):
        form_id = str(id)

        if form_id not in self.multiimageform:
            self.multiimageform[form_id] = {'image': form.cleaned_data.get('image')
            }

        self.save()
        print(self.multiimageform)

    def __iter__(self):
        multiimageform = self.multiimageform.copy()
        for item in multiimageform.values():
            yield item

    def __str__(self):
        multiimageform = self.multiimageform.copy()
        return f"<multiimageformObject {multiimageform}>"

    def save(self):
        self.session.modified = True

    def clear(self):
        del self.session[settings.MULTIIMAGE_SESSION_ID]
        self.session.modified = True

class StoryFormSESSION():
    '''
    Akan membuat session dengan keys cart dan salah satu valuenya product_id
    "cart" ={
    "product_id": {
        'price': $9.99,
        'quantity': 1,
        'id': nike
        }
    }

    Kemudian pada session ini bisa menambahkan di session cart menggunakan prinsip2 dictionary data type
    '''

    def __init__(self, request):
        self.session = request.session
        # initialize session cart
        storyform = self.session.get(settings.STORY_SESSION_ID)

        # jika tidak bukan cart
        if not storyform:
            storyform = self.session[settings.STORY_SESSION_ID] = {}

        self.storyform = storyform


    def add(self, id, form):
        form_id = str(id)

        if form_id not in self.storyform:
            self.storyform[form_id] = {'image': form.cleaned_data.get('image'),
               'cerita': form.cleaned_data.get('cerita'),
               'year': form.cleaned_data.get('year'),
            }

        self.save()
        print(self.storyform)

    def __iter__(self):
        storyform = self.storyform.copy()
        for item in storyform.values():
            yield item

    def __str__(self):
        storyform = self.storyform.copy()
        return f"<storyformObject {storyform}>"

    def save(self):
        self.session.modified = True

    def clear(self):
        del self.session[settings.STORY_SESSION_ID]
        self.session.modified = True


class DompetFormSESSION():
    '''
    Akan membuat session dengan keys cart dan salah satu valuenya product_id
    "cart" ={
    "product_id": {
        'price': $9.99,
        'quantity': 1,
        'id': nike
        }
    }

    Kemudian pada session ini bisa menambahkan di session cart menggunakan prinsip2 dictionary data type
    '''

    def __init__(self, request):
        self.session = request.session
        # initialize session cart
        dompetform = self.session.get(settings.DOMPET_SESSION_ID)

        # jika tidak bukan cart
        if not dompetform:
            dompetform = self.session[settings.DOMPET_SESSION_ID] = {}

        self.dompetform = dompetform


    def add(self, id, form):
        form_id = str(id)

        if form_id not in self.dompetform:
            self.dompetform[form_id] = {'nomor': form.cleaned_data.get('nomor'),
                'pemilik': form.cleaned_data.get('pemilik'),
                'rekening': form.cleaned_data.get('rekening')
            }

        self.save()
        print(self.dompetform)

    def __iter__(self):
        dompetform = self.dompetform.copy()
        for item in dompetform.values():
            yield item

    def __str__(self):
        dompetform = self.dompetform.copy()
        return f"<dompetformObject {dompetform}>"

    def save(self):
        self.session.modified = True

    def clear(self):
        del self.session[settings.DOMPET_SESSION_ID]
        self.session.modified = True

class SpecialinviteFormSESSION():
    '''
    Akan membuat session dengan keys cart dan salah satu valuenya product_id
    "cart" ={
    "product_id": {
        'price': $9.99,
        'quantity': 1,
        'id': nike
        }
    }

    Kemudian pada session ini bisa menambahkan di session cart menggunakan prinsip2 dictionary data type
    '''

    def __init__(self, request):
        self.session = request.session
        # initialize session cart
        specialinviteform = self.session.get(settings.SPECIALINVITE_SESSION_ID)

        # jika tidak bukan cart
        if not specialinviteform:
            specialinviteform = self.session[settings.SPECIALINVITE_SESSION_ID] = {}

        self.specialinviteform = specialinviteform


    def add(self, id, form):
        form_id = str(id)

        if form_id not in self.specialinviteform:
            self.specialinviteform[form_id] = {'name_invite': form.cleaned_data.get('name_invite'),
            }

        self.save()
        print(self.specialinviteform)

    def __iter__(self):
        specialinviteform = self.specialinviteform.copy()
        for item in specialinviteform.values():
            yield item

    def __str__(self):
        specialinviteform = self.specialinviteform.copy()
        return f"<specialinviteformObject {specialinviteform}>"

    def save(self):
        self.session.modified = True

    def clear(self):
        del self.session[settings.SPECIALINVITE_SESSION_ID]
        self.session.modified = True


