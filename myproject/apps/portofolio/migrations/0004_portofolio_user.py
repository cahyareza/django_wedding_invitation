# Generated by Django 3.2.15 on 2022-08-27 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portofolio', '0003_auto_20220828_0343'),
    ]

    operations = [
        migrations.AddField(
            model_name='portofolio',
            name='user',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
    ]
