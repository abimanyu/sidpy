from django.db import models
from django.contrib import admin
from martor.widgets import AdminMartorWidget
from .models import Category, Berita

admin.site.register(Category)

class BeritaAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }
admin.site.register(Berita, BeritaAdmin)