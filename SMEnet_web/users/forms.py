from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    Company_name = forms.CharField()
    Location = forms.CharField()
    Sector = forms.CharField()


    class Meta:
        model = User
        fields = ['username', 'Company_name', 'Location', 'Sector', 'email', 'password1', 'password2']
