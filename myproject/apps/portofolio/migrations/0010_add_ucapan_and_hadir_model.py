# Generated by Django 3.2.15 on 2022-09-10 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portofolio', '0009_add_rekening_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ucapan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date and Time')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modification Date and Time')),
                ('nama', models.CharField(max_length=40)),
                ('alamat', models.CharField(max_length=40)),
                ('pesan', models.CharField(max_length=60)),
                ('portofolio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='portofolio.portofolio')),
            ],
            options={
                'verbose_name_plural': 'Ucapan',
            },
        ),
        migrations.CreateModel(
            name='Hadir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date and Time')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modification Date and Time')),
                ('name', models.CharField(max_length=40)),
                ('hadir', models.CharField(choices=[('iya', 'iya'), ('tidak', 'tidak')], default='tidak', max_length=20)),
                ('portofolio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='portofolio.portofolio')),
            ],
            options={
                'verbose_name_plural': 'Hadir',
            },
        ),
    ]