# Generated by Django 3.2.15 on 2022-11-09 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portofolio', '0033_add_cover_backg'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='cover_fitur',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='theme',
            name='quote_fitur',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
