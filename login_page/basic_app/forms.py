from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import UserProfileInfo


class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username", "password", "email")


class UserProfileInfoForm(ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ("portfolio_site", "profile_pic")
