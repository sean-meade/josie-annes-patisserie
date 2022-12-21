from django import forms
from .models import AfternoonTea


class AfternoonTeaForm(forms.ModelForm):
    class Meta:
        model = AfternoonTea
        fields = ('full_name', 'email', 'phone_number',
                  'date', 'time', 'notes', 'no_of_people',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'date': 'Date',
            'time': 'Time',
            'notes': 'Notes',
            'no_of_people': 'No. of People',
        }
        for field in self.fields:
            if field == 'date' or field == 'time':
                pass
            else:
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
