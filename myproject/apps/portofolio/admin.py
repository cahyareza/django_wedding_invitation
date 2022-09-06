from django.contrib import admin
from .models import (Portofolio, MultiImage)

# Inline
class MultiImageInline(admin.TabularInline):
    model = MultiImage



# Register your models here.
# admin.site.register(Couple)


@admin.register(Portofolio)
class PortofolioAdmin(admin.ModelAdmin):
    inlines = [MultiImageInline]


@admin.register(MultiImage)
class MultiImageAdmin(admin.ModelAdmin):
    pass

# @admin.register(Dompet)
# class DompetAdmin(admin.ModelAdmin):
#     inlines = [RekeningInline]