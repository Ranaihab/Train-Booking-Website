from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterationForm(forms.Form):
    username = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'class':'cunstomForm'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'cunstomForm'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'cunstomForm'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'cunstomForm'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'cunstomForm'}))
    confirmPass = forms.CharField(widget=forms.PasswordInput(attrs={'class':'cunstomForm'}))
    isAdmin = forms.BooleanField(widget=forms.RadioSelect(attrs={'class':'cunstomForm'}))
