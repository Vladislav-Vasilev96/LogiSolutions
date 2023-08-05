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
                    'placeholder': 'CB0430PM..',
                    'class': 'form-group centered-placeholder',
                }
            ),
            'current_location': forms.TextInput(
                attrs={
                    'placeholder': 'Town, Country..',
                    'class': 'form-group centered-placeholder',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Add Additional Information Here..',
                    'class': 'form-group centered-placeholder',
                }
            ),

        }



