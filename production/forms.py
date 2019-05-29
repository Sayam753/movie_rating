from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    CHOICES = (('a','is_production_company'),
               ('b','is_actor'),
               ('c','is_director'),
               ('d','public_user'),)
    group = forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple())
    class Meta:
        model = User
        fields = ['username','group','email','password1','password2']
