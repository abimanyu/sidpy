from django.db import models
from django.contrib import admin
from martor.widgets import AdminMartorWidget

from .models import Kategori, Profil

admin.site.register(Kategori)

class ProfilAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }
admin.site.register(Profil)