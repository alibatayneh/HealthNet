from django import forms
from models import User,Patient

class UserForm(forms.ModelForm):
    class Meta:
        model = Patient.user
