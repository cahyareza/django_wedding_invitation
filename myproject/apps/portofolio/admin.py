from django.contrib import admin
from .models import (Couple, Acara, Ourmoment, SpecialInvitation, Ucapan,
     Quotes, AddtoCalender, Goto, Hadir, Dompet, Portofolio, PhotoOurmoment,
     Rekening)

#Inline
class AcaraInline(admin.TabularInline):
    model = Acara

class CoupleInline(admin.TabularInline):
    model = Couple

class OurmomentInline(admin.TabularInline):
    model = Ourmoment

class SpecialInvitationInline(admin.TabularInline):
    model = SpecialInvitation

class UcapanInline(admin.TabularInline):
    model = Ucapan

class QuotesInline(admin.TabularInline):
    model = Quotes

class AddtoCalenderInline(admin.TabularInline):
    model = AddtoCalender

class GotoInline(admin.TabularInline):
    model = Goto

class HadirInline(admin.TabularInline):
    model = Hadir

class DompetInline(admin.TabularInline):
    model = Dompet

class PhotoOurmomentInline(admin.TabularInline):
    model = PhotoOurmoment

class RekeningInline(admin.TabularInline):
    model = Rekening

# Register your models here.
admin.site.register(Couple)
admin.site.register(Acara)
# admin.site.register(Ourmoment)
admin.site.register(SpecialInvitation)
admin.site.register(Ucapan)
admin.site.register(Quotes)
admin.site.register(AddtoCalender)
admin.site.register(Goto)
admin.site.register(Hadir)
# admin.site.register(Dompet)

@admin.register(Portofolio)
class PortofolioAdmin(admin.ModelAdmin):
    inlines = [AcaraInline, CoupleInline, OurmomentInline, SpecialInvitationInline,
               UcapanInline, QuotesInline, AddtoCalenderInline, GotoInline, HadirInline,
               DompetInline]

@admin.register(Ourmoment)
class OurmomentAdmin(admin.ModelAdmin):
    inlines = [PhotoOurmomentInline]

@admin.register(Dompet)
class DompetAdmin(admin.ModelAdmin):
    inlines = [RekeningInline]