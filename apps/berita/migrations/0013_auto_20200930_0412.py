# Generated by Django 3.1.1 on 2020-09-29 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('berita', '0012_auto_20200930_0235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='berita',
            name='slug',
            field=models.SlugField(max_length=255, null=True),
        ),
    ]
