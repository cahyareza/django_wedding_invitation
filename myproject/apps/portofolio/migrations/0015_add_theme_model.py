# Generated by Django 3.2.15 on 2022-09-23 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portofolio', '0014_add_fitur_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fitur',
            name='slug',
            field=models.SlugField(blank=True, max_length=255),
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date and Time')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modification Date and Time')),
                ('name', models.CharField(max_length=40)),
                ('slug', models.SlugField(blank=True, max_length=255)),
                ('fitur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='portofolio.fitur')),
                ('portofolio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='portofolio.portofolio')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
