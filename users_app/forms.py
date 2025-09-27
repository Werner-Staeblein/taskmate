from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Erforderlich. Geben Sie eine gültige E-Mail-Adresse ein.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']