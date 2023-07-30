from django.contrib import admin

from LogiSolutions.guest_service.models import GuestServiceFormSubmission


@admin.register(GuestServiceFormSubmission)
class GuestServiceFormSubmissionAdmin(admin.ModelAdmin):
    pass