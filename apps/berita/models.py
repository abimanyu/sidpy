from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Kategori'
        ordering = ('ordering',)
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug == None:
            slug = slugify(self.title)

            has_slug = Category.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.title) + '-' + str(count)
                has_slug = Category.objects.filter(slug=slug).exists()
            self.slug =slug

        super().save(*args, **kwargs)

# ___________________________________

class Tag(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug == None:
            slug = slugify(self.title)
            has_slug = Tag.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.title) + '-' + str(count)
                has_slug = Tag.objects.filter(slug=slug).exists()
            self.slug =slug

        super().save(*args, **kwargs)
# ___________________________________

class Berita(models.Model):
    category = models.ForeignKey(Category, related_name='all_berita', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    thumbnail = models.ImageField(upload_to='thumb', null=True, blank=True)
    
    isi = RichTextUploadingField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    STATUS = (
        ('Publish', 'Publish'),
        ('Draft', 'Draft'),
        ('InActive', 'InActive')
    )
    status = models.CharField(max_length=20, default='Publish', blank=True, choices=STATUS)

    featured = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, default=1)
    slug = models.SlugField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Berita'
        ordering = ('-date_added',)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.slug == None:
            slug = slugify(self.title)

            has_slug = Berita.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.title) + '-' + str(count)
                has_slug = Berita.objects.filter(slug=slug).exists()
            self.slug =slug

        super().save(*args, **kwargs)
