# Generated by Django 3.2.15 on 2022-10-07 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portofolio', '0021_add_datetime_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portofolio',
            name='datetime_resepsi',
            field=models.CharField(max_length=250),
        ),
    ]