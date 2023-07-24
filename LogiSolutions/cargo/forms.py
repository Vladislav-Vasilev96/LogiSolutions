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
        fields = '__all__'
        exclude = ('owner',)
        widgets = {
            'departure_date': DateInput,
            'arrival_date': DateInput
        }
