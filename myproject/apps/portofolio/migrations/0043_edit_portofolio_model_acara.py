# Generated by Django 3.2.15 on 2022-11-19 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portofolio', '0042_edit_portofolio_model_acara'),
    ]

    operations = [
        migrations.AddField(
            model_name='portofolio',
            name='location_countdown',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='portofolio',
            name='waktu_countdown_selesai',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
