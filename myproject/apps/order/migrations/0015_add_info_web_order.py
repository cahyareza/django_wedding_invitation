# Generated by Django 3.2.15 on 2023-01-05 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0014_auto_20221229_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='info_web',
            field=models.CharField(choices=[('teman', 'Teman'), ('vendor', 'Vendor'), ('influencer', 'Influencer'), ('instagram', 'Instagram'), ('facebook', 'Facebook'), ('tiktok', 'TikTok'), ('twitter', 'Twitter'), ('google', 'Google'), ('iklan', 'Iklan'), ('lainnya', 'Lainnya')], default='lainnya', max_length=20),
        ),
    ]