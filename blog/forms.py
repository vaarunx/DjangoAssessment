from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.forms import fields, DateInput, widgets
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from .models import Profile




class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1' , 'password2']


class UserUpdateForm(forms.ModelForm): 
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username' , 'email' ]         


class ProfileUpdateForm(forms.ModelForm):
    phone_number = PhoneNumberField(
        widget = PhoneNumberPrefixWidget(initial = 'IN')  
    )

    class Meta:
        model = Profile
        fields = ['phone_number' , 'birthdate']    
        widgets = {
            'birthdate': DateInput(attrs={'type': 'date'}),
        }    