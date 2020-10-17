from django.db import models
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

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='all_item', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    thumbnail = models.ImageField(upload_to='thumb', null=True, blank=True)

    isi = RichTextUploadingField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    STATUS = (
        ('Publish', 'Publish'),
        ('Draft', 'Draft'),
        ('InActive', 'InActive')
    )
    status = models.CharField(max_length=20, default='Publish', blank=True, choices=STATUS)

    featured = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Produk'
        ordering = ('-created_at',)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.slug == None:
            slug = slugify(self.title)

            has_slug = Produk.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.title) + '-' + str(count)
                has_slug = Produk.objects.filter(slug=slug).exists()
            self.slug =slug

        super().save(*args, **kwargs)
