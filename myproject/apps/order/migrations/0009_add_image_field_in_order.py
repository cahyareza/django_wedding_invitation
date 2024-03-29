# Generated by Django 3.2.15 on 2022-09-26 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_related_name_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='bukti',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('menunggu pembayaran', 'menunggu pembayaran'), ('menunggu konfirmasi', 'menunggu konfirmasi'), ('terkonfirmasi', 'terkonfirmasi')], default='menunggu pembayaran', max_length=20),
        ),
    ]
