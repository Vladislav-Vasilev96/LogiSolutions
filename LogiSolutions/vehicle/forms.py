from django import forms

from LogiSolutions.vehicle.models import Vehicle


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'
        exclude = ('owner',)
