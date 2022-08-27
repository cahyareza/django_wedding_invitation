from django.contrib import admin
from .models import (Couple, Acara, Ourmoment, SpecialInvitation, Ucapan,
     Quotes, AddtoCalender, Goto, Hadir, Dompet, Portofolio)

# Register your models here.
admin.site.register(Acara)
admin.site.register(Ourmoment)
admin.site.register(SpecialInvitation)
admin.site.register(Ucapan)
admin.site.register(Quotes)
admin.site.register(AddtoCalender)
admin.site.register(Goto)
admin.site.register(Hadir)
admin.site.register(Dompet)
admin.site.register(Portofolio)

@admin.register(Couple)
class CoupleAdmin(admin.ModelAdmin):
    pass
