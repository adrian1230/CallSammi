from django import forms
from string import punctuation
from understand.models import Result
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
import numpy as np
import random
from Sammie import settings
from understand.models import categories

class TextSummary(forms.ModelForm):
	source = forms.CharField(widget=forms.TextInput(attrs={'class': 'input is-rounded','placeholder':'url or magazine name, etc.'}),required=False)
	original_text = forms.CharField(widget=forms.Textarea(attrs={'rows':7,'cols':10, 'class':'textarea'}))
	category = forms.CharField(widget=forms.Select(choices=categories,attrs={'class': 'select'}))
	user = forms.CharField(widget=forms.TextInput(attrs={'class': 'input','placeholder':'your exact user name'}))

	class Meta:
		model = Result
		fields = [
		  'source',
		  'original_text',
		  'category',
		  'user'
		]

class Register(UserCreationForm): # Using
    username = forms.CharField(max_length=30, required=True,widget=forms.TextInput(attrs={'class':'input'}))
    password1 = forms.CharField(label="password",max_length=40, required=True,widget=forms.TextInput(attrs={'class':'input'}))
    password2 = forms.CharField(label="confirm password",max_length=40, required=True,widget=forms.TextInput(attrs={'class':'input'})) 

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for f in ['password1', 'password2']:
            self.fields[f].help_text = None

    class Meta:
        model = User
        fields = [
            'username', 
            'password1', 
            'password2', 
            ]

    def save(self, commit=True):
        user = super (Register, self ).save(commit=False)
        user.is_staff = False
        user.is_superuser = False

        if commit :
            user.save()

        return user