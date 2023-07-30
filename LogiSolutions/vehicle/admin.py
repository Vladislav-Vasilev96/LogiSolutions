from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from LogiSolutions.vehicle.models import Vehicle


class VehicleAdmin(admin.ModelAdmin):
    list_display = ['license_plate', 'current_location', 'is_approved', 'approve_button']
    list_filter = ['is_approved']
    actions = ['approve_vehicle', 'reject_vehicle']

    def approve_button(self, obj):
        if not obj.is_approved:
            return format_html('<a class="button" href="{}">Approve</a>', reverse('approve vehicle', args=[obj.pk]))
        return ""

    approve_button.short_description = "Approve Button"

    def approve_vehicle(self, request, queryset):
        queryset.update(is_approved=True)

    def reject_vehicle(self, request, queryset):
        queryset.update(is_approved=False)

    approve_vehicle.short_description = 'Approve selected vehicle posts'
    reject_vehicle.short_description = 'Reject selected vehicle posts'

admin.site.register(Vehicle, VehicleAdmin)

