# Generated by Django 3.2.15 on 2023-01-05 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0015_add_info_web_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='info_web',
            field=models.CharField(blank=True, choices=[('teman', 'Teman'), ('vendor', 'Vendor'), ('influencer', 'Influencer'), ('instagram', 'Instagram'), ('facebook', 'Facebook'), ('tiktok', 'TikTok'), ('twitter', 'Twitter'), ('google', 'Google'), ('iklan', 'Iklan'), ('lainnya', 'Lainnya')], max_length=20, null=True),
        ),
    ]
