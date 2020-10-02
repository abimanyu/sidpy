from django import forms
from django.forms import ModelForm

from .models import Pages

class PagesForm(ModelForm):
    class Meta:
        model = Pages
        fields = '__all__'