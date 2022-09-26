# Generated by Django 3.2.15 on 2022-09-25 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portofolio', '0018_add_fiturproduct_model'),
        ('order', '0003_add_orderitem_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='nama_rekening',
            field=models.CharField(default='Tomo', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portofolio.payment'),
        ),
    ]
