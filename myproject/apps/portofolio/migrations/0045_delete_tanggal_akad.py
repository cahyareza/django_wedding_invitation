# Generated by Django 3.2.15 on 2022-11-19 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portofolio', '0044_add_tanggal_akad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portofolio',
            name='tanggal_akad',
        ),
    ]
