from django import forms

from LogiSolutions.guest_service.models import GuestServiceFormSubmission


class QuestionForm(forms.ModelForm):
    class Meta:
        model = GuestServiceFormSubmission
        fields = [ 'email', 'phone','question']
