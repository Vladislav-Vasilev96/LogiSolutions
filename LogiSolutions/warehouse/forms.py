from django import forms

from LogiSolutions.warehouse.models import Warehouse


class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = '__all__'
        exclude = ('owner',)
