# Generated by Django 3.2.15 on 2022-11-23 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portofolio', '0049_url_field_acara_gmap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portofolio',
            name='livestream',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
    ]