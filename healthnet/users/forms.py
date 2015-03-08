
from django import forms
from django.contrib.auth.models import User
from users.models import Patient


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('address', 'doctor')
