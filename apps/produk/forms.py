from django import forms
from django.forms import ModelForm

from .models import Item, Category

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'