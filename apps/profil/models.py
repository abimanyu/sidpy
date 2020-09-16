from django.db import models
from django.contrib.auth.models import User
from martor.models import MartorField

class Kategori(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    class Meta:
        verbose_name_plural = 'Kategori'
    
    def __str__(self):
        return self.title

class Profil(models.Model):
    kategori = models.ForeignKey(Kategori, related_name='profil_all', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    isi = MartorField(blank=True, null=True)
    ordering = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Halaman'
        ordering = ('ordering',)

    def __str__(self):
        return self.title
