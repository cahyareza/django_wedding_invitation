# Generated by Django 3.2.15 on 2022-11-28 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portofolio', '0051_change_foreign_key_blank_null'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='ayat',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]