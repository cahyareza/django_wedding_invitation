from django.contrib import admin
from .models import (Portofolio, MultiImage, SpecialInvitation, Dompet, Quote,
     Rekening, Ucapan, Hadir, Fitur, Payment, Theme, ThemeProduct, Kabupaten, Story,
     Acara, Track, Kata, Dana)

# Inline
class PortoInline(admin.TabularInline):
    model = Portofolio

class AcaraInline(admin.TabularInline):
    model = Acara

class StoryInline(admin.TabularInline):
    model = Story

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

class ThemeProductInline(admin.TabularInline):
    model = ThemeProduct

class DanaInline(admin.TabularInline):
    model = Dana


@admin.register(Portofolio)
class PortofolioAdmin(admin.ModelAdmin):
    list_filter = ['tanggal_countdown']
    list_display = ['porto_name', 'pname', 'lname', 'tanggal_countdown', 'waktu_countdown', 'created']
    search_fields = ['porto_name', 'tanggal_countdown', 'created']
    inlines = [AcaraInline, MultiImageInline, SpecialInvitationInline, DompetInline, QuoteInline,
               UcapanInline, HadirInline, StoryInline, ThemeProductInline, DanaInline]
    list_per_page = 10

    # Fieldset
    fieldsets = [
        # INFORMASI UNDANGAN
        ('INFORMASI UNDANGAN', {'fields': ['porto_name', 'slug', 'user', 'porto_picture']}),
        # INFORMASI PASANGAN
        ('INFORMASI PASANGAN', {'fields': ['pname', 'pinsta_link', 'panak_ke', 'pnama_ayah', 'pnama_ibu',
         'ppicture', 'lname', 'linsta_link', 'lanak_ke', 'lnama_ayah', 'lnama_ibu', 'lpicture']}
         ),
        # INFORMASI COUNTDOWN
        ('INFORMASI COUNTDOWN', {"fields": ['tanggal_countdown', 'waktu_countdown', 'datetime_countdown', \
          'location_countdown', 'waktu_countdown_selesai']}
        ),
        # INFORMASI OUR MOMENT
        ('INFORMASI OUR MOMENT ', {"fields": ['video', 'livestream']}
        ),
        # INFORMASI CALENDER
        ('INFORMASI CALENDER', {"fields": ['name','description', 'startDate', 'location','startTime', 'endTime',
        'options', 'timeZone', 'trigger','iCalFileName']}
        ),
        # INFORMASI KATA
        ('INFORMASI KATA', {"fields": ['kata_special_invite', 'kata_live_streaming', 'kata_moment']}
         ),
        # INFORMASI MAP
        ('INFORMASI MAP', {"fields": ['link_iframe', 'lokasi', 'link_gmap']}
        ),
        # INFORMASI BACKGROUND
        ('INFORMASI BACKGROUND', {"fields": ['cover_background', 'open_background']}
         ),
        # INFORMASI TRACK
        ('INFORMASI TRACK', {"fields": ['track']}
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

@admin.register(Fitur)
class FiturAdmin(admin.ModelAdmin):
    pass

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass

@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    pass

@admin.register(ThemeProduct)
class ThemeProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Kabupaten)
class KabupatenAdmin(admin.ModelAdmin):
    pass

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Acara)
class AcaraAdmin(admin.ModelAdmin):
    pass

@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    inlines = [PortoInline]

@admin.register(Kata)
class KataAdmin(admin.ModelAdmin):
    pass

@admin.register(Dana)
class DanaAdmin(admin.ModelAdmin):
    pass