# Generated by Django 3.2.15 on 2022-11-23 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portofolio', '0047_change_related_name_themeproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portofolio',
            name='link_gmap',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
    ]