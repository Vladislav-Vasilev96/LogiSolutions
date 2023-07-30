from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from LogiSolutions.cargo.models import Cargo

class CargoAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'is_approved', 'approve_button']
    list_filter = ['is_approved']
    actions = ['approve_cargo', 'reject_cargo']

    def approve_button(self, obj):
        if not obj.is_approved:
            return format_html('<a class="button" href="{}">Approve</a>', reverse('approve cargo', args=[obj.pk]))
        return ""

    approve_button.short_description = "Approve Button"

    def approve_cargo(self, request, queryset):
        queryset.update(is_approved=True)

    def reject_cargo(self, request, queryset):
        queryset.update(is_approved=False)

    approve_cargo.short_description = 'Approve selected cargo posts'
    reject_cargo.short_description = 'Reject selected cargo posts'

admin.site.register(Cargo, CargoAdmin)

