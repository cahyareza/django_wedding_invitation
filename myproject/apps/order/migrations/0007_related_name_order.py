# Generated by Django 3.2.15 on 2022-09-26 04:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portofolio', '0018_add_fiturproduct_model'),
        ('order', '0006_change_field_paid_in_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('menunggu pembayaran', 'menunggu pembayaran'), ('dibayar', 'dibayar'), ('menunggu konfirmasi', 'menunggu konfirmasi'), ('terkonfirmasi', 'terkonfirmasi')], default='menunggu pembayaran', max_length=20),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='portofolio.fitur'),
        ),
    ]
