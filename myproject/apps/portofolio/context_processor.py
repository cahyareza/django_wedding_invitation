from .models import Fitur

def listProduct(request):
    objects_fitur = Fitur.objects.all()

    return {'fiturs': objects_fitur}