from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name...'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name...'}),
            'username': forms.TextInput(attrs={'placeholder': 'Username...'}),
            'email': forms.TextInput(attrs={'placeholder': 'E-mail...'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Password...'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Password(again)...'}),
        }