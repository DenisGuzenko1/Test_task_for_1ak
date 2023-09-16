from django import forms

from index.models import Users


class CreateUser(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['name', 'surname', 'patronymic']
