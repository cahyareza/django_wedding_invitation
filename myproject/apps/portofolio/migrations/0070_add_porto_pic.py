# Generated by Django 3.2.15 on 2022-12-31 07:27

from django.db import migrations, models
import myproject.apps.portofolio.models


class Migration(migrations.Migration):

    dependencies = [
        ('portofolio', '0069_add_porto_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portofolio',
            name='porto_picture',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to=myproject.apps.portofolio.models.portofolio_picture_upload_to),
        ),
    ]
