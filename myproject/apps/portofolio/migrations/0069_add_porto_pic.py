# Generated by Django 3.2.15 on 2022-12-31 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portofolio', '0068_change_max_length_to_filefield_and_imagefield'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='portofolio',
            options={'ordering': ['-created'], 'verbose_name_plural': 'APortofolio'},
        ),
        migrations.AddField(
            model_name='portofolio',
            name='porto_picture',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
