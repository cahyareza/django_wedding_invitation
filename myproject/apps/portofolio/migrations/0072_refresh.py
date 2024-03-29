# Generated by Django 3.2.15 on 2023-02-02 06:27

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('portofolio', '0071_change_maxlength_track'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fitur',
            name='fitur',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('desain standard', 'desain standard'), ('quotes', 'quotes'), ('detail acara', 'detail acara'), ('profil pasangan', 'profil pasangan'), ('protokol kesehatan', 'protokol kesehatan'), ('navigasi lokasi', 'navigasi lokasi'), ('google calender', 'google calender'), ('unlimited custom jadwal acara', 'unlimited custom jadwal acara'), ('rsvp', 'rsvp'), ('amplop digital', 'amplop digital'), ('kirim ucapan', 'kirim ucapan'), ('gallery(max 10)', 'gallery(max 10)'), ('love stories', 'love stories'), ('buku tamu', 'buku tamu'), ('share eksklusif(max 50)', 'share eksklusif(max 50)'), ('background music(list only)', 'background music(list only)'), ('custom domain(additional)', 'custom domain(additional)'), ('desain platinum', 'desain platinum'), ('gallery(max 20)', 'gallery(max 20)'), ('live streaming', 'live streaming'), ('share eksklusif(unlimited)', 'share eksklusif(unlimited)'), ('background music(list dan custom)', 'background music(list dan custom)'), ('tersedia versi inggris', 'tersedia versi inggris'), ('semua jenis desain', 'semua jenis desain'), ('support prioritas', 'support prioritas'), ('masa aktif selamanya', 'masa aktif selamanya'), ('edit tanpa batas', 'edit tanpa batas')], max_length=488, null=True),
        ),
    ]
