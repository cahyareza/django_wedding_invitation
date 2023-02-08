# Generated by Django 3.2.15 on 2023-02-08 12:36

from django.db import migrations, models
import myproject.apps.portofolio.models


class Migration(migrations.Migration):

    dependencies = [
        ('portofolio', '0073_change_size_photo_in_pasangan_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='dompet',
            name='bar_code',
            field=models.FileField(blank=True, max_length=500, null=True, upload_to=myproject.apps.portofolio.models.dompet_upload_to),
        ),
        migrations.AddField(
            model_name='portofolio',
            name='alamat_rumah',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
