from django.contrib import admin
from .models import Order, OrderItem
from django.utils.html import format_html

class OrderItemInline(admin.TabularInline):
    model = OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_filter = ['status']
    list_display = ['user', 'phone', 'paid', 'payment', 'nama_rekening',
                    'bukti', 'status_color', 'upgrade_status', 'paid_upgrade', 'status_upgrade_color', 'bukti_upgrade']
    search_fields = ['user', 'nama_rekening', 'place', 'status']
    list_per_page = 10
    inlines = [OrderItemInline]

    # function to color the text
    def status_color(self, obj):
        if obj.status == 'terkonfirmasi':
            color = '#28a745'
        elif obj.status == 'menunggu konfirmasi':
            color = '#fea95e'
        else:
            color = 'red'
        return format_html('<strong><p style="color: {}">{}</p></strong>'.format(color, obj.status))
    status_color.allow_tags = True

    # function to color the text
    def status_upgrade_color(self, obj):
        if obj.upgrade_status == True :
            if obj.status_upgrade == 'terkonfirmasi':
                color = '#28a745'
            elif obj.status_upgrade == 'menunggu konfirmasi':
                color = '#fea95e'
            else:
                color = 'red'
            return format_html('<strong><p style="color: {}">{}</p></strong>'.format(color, obj.status_upgrade))
    status_upgrade_color.allow_tags = True

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass