# Generated by Django 3.2.15 on 2023-01-09 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portofolio', '0070_add_porto_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portofolio',
            name='lpicture',
            field=models.ImageField(blank=True, default='null', upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='ppicture',
            field=models.ImageField(blank=True, default='null', upload_to=''),
            preserve_default=False,
        ),
    ]
