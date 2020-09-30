from django.db import models
from django.contrib import admin
from .models import Category, Tag, Berita

admin.site.register(Berita)
admin.site.register(Category)
admin.site.register(Tag)