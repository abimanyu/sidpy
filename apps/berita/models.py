from django.db import models
from django.contrib.auth.models import User
from martor.models import MartorField

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Kategori'
        ordering = ('ordering',)
    
    def __str__(self):
        return self.title

class Berita(models.Model):
    category = models.ForeignKey(Category, related_name='all_berita', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    isi = MartorField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Berita'
        ordering = ('-date_added',)

    def __str__(self):
        return self.title
