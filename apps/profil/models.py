from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    class Meta:
        verbose_name_plural = 'Kategori'
    
    def __str__(self):
        return self.title

class Pages(models.Model):
    category = models.ForeignKey(Category, related_name='pages', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    STATUS = (
        ('Publish', 'Publish'),
        ('Draft', 'Draft'),
        ('InActive', 'InActive')
    )
    status = models.CharField(max_length=20, default='Publish', blank=True, choices=STATUS)

    isi = RichTextUploadingField(blank=True, null=True)
    ordering = models.IntegerField(default=0)
    slug = models.SlugField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Halaman'
        ordering = ('ordering',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug == None:
            slug = slugify(self.title)

            has_slug = Pages.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.title) + '-' + str(count)
                has_slug = Pages.objects.filter(slug=slug).exists()
            self.slug =slug

        super().save(*args, **kwargs)