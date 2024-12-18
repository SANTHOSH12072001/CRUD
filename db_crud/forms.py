from django import forms
from .models import RegisterForm
from django.forms import fields
class MyRegisterForm(forms.ModelForm):
    name=forms.CharField(label='Name', max_length=100)
    age=forms.IntegerField(label='Age')
    email=forms.CharField(label='Email', max_length=100)
    address=forms.CharField(label='Address', max_length=150)
    contact=forms.CharField(label='Contact', max_length=100)
    class Meta:
        model = RegisterForm
        fields=["name","age","email","address","contact"]