from django import forms
from django.forms import ModelForm

from .models import Berita, Category, Tag

class BeritaForm(ModelForm):
    class Meta:
        model = Berita
        fields = '__all__'
    
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'