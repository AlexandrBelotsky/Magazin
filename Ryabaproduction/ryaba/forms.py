from django import forms
from .models import *



class Zakaz2(forms.ModelForm):
    class Meta:
        model = Zakaz
        fields = ['name', 'email', 'city', 'tel', 'choice', 'opisanie', 'count']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)




