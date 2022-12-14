# Generated by Django 3.2.15 on 2022-12-12 20:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_change_place_field_to_foreign'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='bukti_upgrade',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(70)]),
        ),
        migrations.AddField(
            model_name='order',
            name='paid_upgrade',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='order',
            name='status_upgrade',
            field=models.CharField(choices=[('menunggu pembayaran', 'menunggu pembayaran'), ('menunggu konfirmasi', 'menunggu konfirmasi'), ('terkonfirmasi', 'terkonfirmasi')], default='menunggu pembayaran', max_length=20),
        ),
        migrations.AddField(
            model_name='order',
            name='upgrade_status',
            field=models.BooleanField(default=False),
        ),
    ]