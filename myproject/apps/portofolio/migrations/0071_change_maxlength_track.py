# Generated by Django 3.2.15 on 2023-01-21 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portofolio', '0070_add_porto_pic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='theme',
            options={'ordering': ['-created']},
        ),
        migrations.AlterField(
            model_name='track',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
