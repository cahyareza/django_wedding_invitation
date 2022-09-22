from django.contrib import admin
from .models import (Portofolio, MultiImage, SpecialInvitation, Dompet, Quote,
     Rekening, Ucapan, Hadir)

# Inline
class MultiImageInline(admin.TabularInline):
    model = MultiImage

class DompetInline(admin.TabularInline):
    model = Dompet

class SpecialInvitationInline(admin.TabularInline):
    model = SpecialInvitation

class DompetInline(admin.TabularInline):
    model = Dompet

class QuoteInline(admin.TabularInline):
    model = Quote

class RekeningInline(admin.TabularInline):
    model = Rekening

class UcapanInline(admin.TabularInline):
    model = Ucapan

class HadirInline(admin.TabularInline):
    model = Hadir

# Register your models here.
# admin.site.register(Couple)


@admin.register(Portofolio)
class PortofolioAdmin(admin.ModelAdmin):
    inlines = [MultiImageInline, SpecialInvitationInline, DompetInline, QuoteInline,
               UcapanInline, HadirInline]
    list_per_page = 10

    # Fieldset
    fieldsets = [
        # INFORMASI UNDANGAN
        ('INFORMASI UNDANGAN', {'fields': ['porto_name', 'slug', 'user']}),
        # INFORMASI PASANGAN
        ('INFORMASI PASANGAN', {'fields': ['pname', 'pinsta_link', 'panak_ke', 'pnama_ayah', 'pnama_ibu',
         'ppicture', 'lname', 'linsta_link', 'lanak_ke', 'lnama_ayah', 'lnama_ibu', 'lpicture']}
         ),
        # INFORMASI ACARA
        ('INFORMASI ACARA', {"fields": ['tanggal_akad','waktu_akad', 'waktu_selesai_akad',
        'tempat_akad', 'link_gmap_akad', 'tanggal_resepsi','waktu_resepsi', 'waktu_selesai_resepsi',
        'tempat_resepsi', 'link_gmap_resepsi', 'tanggal_unduhmantu','waktu_unduhmantu',
        'waktu_selesai_unduhmantu', 'tempat_unduhmantu','link_gmap_unduhmantu']}
        ),
        # INFORMASI OUR MOMENT
        ('INFORMASI OUR MOMENT ', {"fields": ['video', 'livestream']}
        ),
        # INFORMASI CALENDER
        ('INFORMASI CALENDER', {"fields": ['name','description', 'startDate', 'location','startTime', 'endTime',
        'options', 'timeZone', 'trigger','iCalFileName']}
        ),
        # INFORMASI MAP
        ('INFORMASI MAP', {"fields": ['link_iframe', 'lokasi', 'link_gmap']}
        ),
    ]


@admin.register(MultiImage)
class MultiImageAdmin(admin.ModelAdmin):
    pass

@admin.register(SpecialInvitation)
class SpecialInvitationAdmin(admin.ModelAdmin):
    pass

@admin.register(Dompet)
class DompetAdmin(admin.ModelAdmin):
    pass

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    pass

@admin.register(Rekening)
class RekeningAdmin(admin.ModelAdmin):
    inlines = [DompetInline]

@admin.register(Ucapan)
class UcapanAdmin(admin.ModelAdmin):
    pass

@admin.register(Hadir)
class HadirAdmin(admin.ModelAdmin):
    pass