import datetime
from django import forms
from parking_reservation.models import SlotDetail
from django.forms import ModelForm, DateInput, TextInput, ValidationError

class SlotDetailForm(ModelForm):
    class Meta():
        model = SlotDetail
        fields = '__all__'

        widgets = {
            # The class here is a CSS class.
            'start_date' : DateInput(attrs={'type': 'date'}),
            'end_date'  : DateInput(attrs={'type': 'date'}),
        }

# Additional custom validator for start_date / finish_date fields
    def clean(self):
        data = self.cleaned_data
        start_date = data['start_date']
        end_date = data['end_date']

        if start_date > end_date:
            raise ValidationError('Wrong start and end dates.')

        if start_date < datetime.date.today():
            raise ValidationError('Start date in the past.')

        return data
