import re

from django import forms
from .models import *


def validate_data(text):
    return bool(re.search(r'[ !\d]', text))


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['last_name', 'first_name', 'patronymic', 'position', 'date_accept']
        widgets = {
            'date_accept': forms.widgets.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['patronymic'].required = False

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if re.search(r'[0-9\s\W]', last_name):
            raise forms.ValidationError('Фамилия не должна содержать цифры, пробелы или знаки препинания.')
        return last_name

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if re.search(r'[0-9\s\W]', first_name):
            raise forms.ValidationError('Имя не должно содержать цифры, пробелы или знаки препинания.')
        return first_name

    def clean_patronymic(self):
        patronymic = self.cleaned_data['patronymic']
        if patronymic and re.search(r'[0-9\s\W]', patronymic):
            raise forms.ValidationError('Отчество не должно содержать цифры, пробелы или знаки препинания.')


class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ['name']

    def clean_last_name(self):
        name = self.cleaned_data['name']
        if re.search(r'[0-9\s\W]', name):
            raise forms.ValidationError('Название должности не должна содержать цифры, пробелы или знаки препинания.')
        return name
