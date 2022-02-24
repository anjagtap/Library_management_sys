from django import forms
from .models import data
from django.core import validators

class bookregisteration(forms.ModelForm):
    class Meta:
        model=data
        fields=['book_name','author_name','price']
        widgets={
            'book_name':forms.TextInput(attrs={'class':'form-control'}),
            'author_name':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.TextInput(attrs={'class':'form-control'}),
        }