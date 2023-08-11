from django import forms

from LogiSolutions.cargo.models import Cargo


class DateInput(forms.DateInput):
    input_type = 'date'

    def __int__(self, **kwargs):
        kwargs['format'] = "%d-%m-%Y"
        super().__init__(**kwargs)


class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ['name', 'location', 'destination', 'total_km', 'cargo_type', 'contact_number', 'weight',
                  'cargo_image', 'departure_date', 'arrival_date', 'description']
        exclude = ('owner', 'is_approved','created_at')
        labels = {
            'name': 'Name of item',
            'destination': 'Final Destination',
            'total_km': 'Total Kilometers',

        }

        widgets = {
            'departure_date': DateInput,
            'arrival_date': DateInput,
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Item type'
                }
            ),

            'location': forms.TextInput(
                attrs={
                    'placeholder': 'Town, Country',
                }
            ),
            'total_km': forms.TextInput(
                attrs={
                    'placeholder': 'Kilometers',
                }
            ),
            'destination': forms.TextInput(
                attrs={
                    'placeholder': 'Final Destination'
                }
            ),
            'cargo_type': forms.TextInput(
                attrs={
                    'placeholder': 'Package type'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Add Additional Information Here..'
                }
            ),

        }
