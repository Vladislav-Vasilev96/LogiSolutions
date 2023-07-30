from django import forms

from LogiSolutions.warehouse.models import Warehouse


class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = '__all__'
        exclude = ('owner','is_approved')

        labels = {
            'square_meters_capacity': 'Area capacity'
        }

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Add name of the warehouse'
                }
            ),
            'Location': forms.TextInput(
                attrs={
                    'placeholder': 'Add location of the warehouse'
                }
            ),
            'square_meters_capacity': forms.TextInput(
                attrs={
                    'placeholder': 'm2'
                }
            ),
            'location': forms.TextInput(
                attrs={
                    'placeholder': 'Location of the warehouse'
                }
            )

        }
