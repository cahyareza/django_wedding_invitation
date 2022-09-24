# Generated by Django 3.2.15 on 2022-09-24 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portofolio', '0016_add_payment_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='bank',
        ),
        migrations.AddField(
            model_name='payment',
            name='rekening',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='portofolio.rekening'),
        ),
    ]
