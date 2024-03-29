# Generated by Django 3.2.15 on 2022-11-05 17:52

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('portofolio', '0030_add_pic_resize'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portofolio',
            name='lpicture_resize',
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='lpicture',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format='JPEG', keep_meta=True, quality=100, scale=0.5, size=[180, 180], upload_to='whatever'),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='ppicture',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format='JPEG', keep_meta=True, quality=100, scale=0.5, size=[180, 180], upload_to='whatever'),
        ),
    ]
