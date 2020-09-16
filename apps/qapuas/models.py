from django.db import models

class site_conf(models.Model):
    conf = models.SlugField(max_length=255)
    conf_val = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=255)
    desc = models.TextField(blank=True, null=True)
    is_load = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Web Config'

    def __str__(self):
        return self.title
