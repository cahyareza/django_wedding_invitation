# Generated by Django 3.2.15 on 2022-09-05 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portofolio', '0001_create_new_porto_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portofolio',
            name='lanak_ke',
            field=models.CharField(default=1, max_length=3),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='panak_ke',
            field=models.CharField(default=1, max_length=3),
        ),
    ]