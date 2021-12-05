from django import forms
from django.forms import ModelForm
from .models import UserProfile

class AuthForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'profile_img',
            ]