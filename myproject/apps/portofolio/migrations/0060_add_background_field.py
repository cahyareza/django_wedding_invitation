# Generated by Django 3.2.15 on 2022-12-20 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portofolio', '0059_add_ornament_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='background_1',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='theme',
            name='background_2',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='theme',
            name='background_3',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='theme',
            name='background_4',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
