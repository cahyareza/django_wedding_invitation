# Generated by Django 3.2.15 on 2022-09-09 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portofolio', '0003_add_dompet_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dompet',
            name='nomor',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='dompet',
            name='pemilik',
            field=models.CharField(max_length=50),
        ),
    ]