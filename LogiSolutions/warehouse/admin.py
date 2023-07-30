from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from LogiSolutions.warehouse.models import Warehouse


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'square_meters_capacity', 'is_approved', 'approve_button']
    list_filter = ['is_approved']
    actions = ['approve_warehouse', 'reject_warehouse']

    def approve_button(self, obj):
        if not obj.is_approved:
            return format_html('<a class="button" href="{}">Approve</a>', reverse('approve warehouse', args=[obj.pk]))
        return ""

    approve_button.short_description = "Approve Button"

    def approve_warehouse(self, request, queryset):
        queryset.update(is_approved=True)

    def reject_warehouse(self, request, queryset):
        queryset.update(is_approved=False)

    approve_warehouse.short_description = 'Approve selected warehouse posts'
    reject_warehouse.short_description = 'Reject selected warehouse posts'


admin.site.register(Warehouse, WarehouseAdmin)
