from django.contrib import admin
from .models import (Portofolio)

#Inline
# class AcaraInline(admin.TabularInline):
#     model = Acara
#
# class CoupleInline(admin.TabularInline):
#     model = Couple


# Register your models here.
# admin.site.register(Couple)
# admin.site.register(Acara)
# admin.site.register(Ourmoment)
# admin.site.register(SpecialInvitation)
# admin.site.register(Ucapan)
# admin.site.register(Quotes)
# admin.site.register(AddtoCalender)
# admin.site.register(Goto)
# admin.site.register(Hadir)
# admin.site.register(Dompet)

@admin.register(Portofolio)
class PortofolioAdmin(admin.ModelAdmin):
    pass

#
# @admin.register(Ourmoment)
# class OurmomentAdmin(admin.ModelAdmin):
#     inlines = [PhotoOurmomentInline]
#
# @admin.register(Dompet)
# class DompetAdmin(admin.ModelAdmin):
#     inlines = [RekeningInline]