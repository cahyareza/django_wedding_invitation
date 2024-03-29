# Generated by Django 3.2.15 on 2022-09-24 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portofolio', '0017_add_payment_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theme',
            name='portofolio',
        ),
        migrations.CreateModel(
            name='FiturProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date and Time')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modification Date and Time')),
                ('fitur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='portofolio.fitur')),
                ('portofolio', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='portofolio.portofolio')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
