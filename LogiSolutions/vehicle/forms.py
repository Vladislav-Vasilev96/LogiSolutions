from django import forms

from LogiSolutions.vehicle.models import Vehicle


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'
        exclude = ('owner', 'is_approved')
        widgets = {
            'license_plate': forms.TextInput(
                attrs={
                    'placeholder': 'CB0430PM..'
                }
            ),
            'current_location': forms.TextInput(
                attrs={
                    'placeholder': 'Town, Country..'
                }
            ),
            'description': forms.Textarea(
                attrs={'placeholder': 'Add Additional Information Here..'}
            ),
        }
