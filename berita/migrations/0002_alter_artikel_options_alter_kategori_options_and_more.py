# Generated by Django 5.1.6 on 2025-03-15 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('berita', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artikel',
            options={'verbose_name_plural': '2. Artikel'},
        ),
        migrations.AlterModelOptions(
            name='kategori',
            options={'verbose_name_plural': '1. Kategori'},
        ),
        migrations.AlterField(
            model_name='artikel',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='artikel'),
        ),
    ]
