from django.contrib.auth.models import User
from django import forms

class UserForm(forms.Form):
    username = forms.CharField(label='Login', max_length=50)
