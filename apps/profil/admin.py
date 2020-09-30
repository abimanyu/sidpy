from django.db import models
from django.contrib import admin
from .models import Category, Pages

admin.site.register(Category)
admin.site.register(Pages)