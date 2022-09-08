from django.contrib import admin
from .models import (Portofolio, MultiImage, SpecialInvitation)

# Inline
class MultiImageInline(admin.TabularInline):
    model = MultiImage

class SpecialInvitationInline(admin.TabularInline):
    model = SpecialInvitation

# Register your models here.
# admin.site.register(Couple)


@admin.register(Portofolio)
class PortofolioAdmin(admin.ModelAdmin):
    inlines = [MultiImageInline, SpecialInvitationInline]


@admin.register(MultiImage)
class MultiImageAdmin(admin.ModelAdmin):
    pass

@admin.register(SpecialInvitation)
class SpecialInvitationAdmin(admin.ModelAdmin):
    pass

# @admin.register(Dompet)
# class DompetAdmin(admin.ModelAdmin):
#     inlines = [RekeningInline]