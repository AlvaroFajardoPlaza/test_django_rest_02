"""
Tenemos las Built.in clases de Django para crear usuarios, pero no las vamos a emplear."""
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User # Modelo de Django incorporado... pero yo tengo el mio

from django import forms
from .models import User

class NewUserForm(forms.ModelForm):

    class Meta:

        model = User
        fields = ['username', 'email', 'password']


class LoginForm(forms.ModelForm):

    class Meta:

        model = User
        fields = ['email', 'password']