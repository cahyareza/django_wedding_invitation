# Generated by Django 3.2.15 on 2022-11-18 05:50

from django.db import migrations, models
import django_resized.forms
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('portofolio', '0036_pinsta_null_true'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dompet',
            name='nomor',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='dompet',
            name='pemilik',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='fitur',
            name='fitur',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('preset standard', 'preset standard'), ('quotes', 'quotes'), ('detail acara', 'detail acara'), ('profil pasangan', 'profil pasangan'), ('protokol kesehatan', 'protokol kesehatan'), ('navigasi lokasi', 'navigasi lokasi'), ('google calender', 'google calender'), ('unlimited custom jadwal acara', 'unlimited custom jadwal acara'), ('rsvp', 'rsvp'), ('amplop digital', 'amplop digital'), ('kirim ucapan', 'kirim ucapan'), ('gallery(max 10)', 'gallery(max 10)'), ('love stories', 'love stories'), ('buku tamu', 'buku tamu'), ('share eksklusif(max 50)', 'share eksklusif(max 50)'), ('background music(list only)', 'background music(list only)'), ('custom domain(additional)', 'custom domain(additional)'), ('preset platinum', 'preset platinum'), ('gallery(max 20)', 'gallery(max 20)'), ('live streaming', 'live streaming'), ('share eksklusif(unlimited)', 'share eksklusif(unlimited)'), ('background music(list dan custom)', 'background music(list dan custom)'), ('tersedia versi inggris', 'tersedia versi inggris'), ('semua jenis preset', 'semua jenis preset'), ('support prioritas', 'support prioritas'), ('masa aktif selamanya', 'masa aktif selamanya'), ('edit tanpa batas', 'edit tanpa batas')], max_length=488, null=True),
        ),
        migrations.AlterField(
            model_name='fitur',
            name='name',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='fitur',
            name='price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='fitur',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='hadir',
            name='hadir',
            field=models.CharField(choices=[('iya', 'iya'), ('tidak', 'tidak')], default='tidak', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='hadir',
            name='name',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='multiimage',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='payment',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='number',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='cover_background',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='datetime_resepsi',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='endTime',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='iCalFileName',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='lanak_ke',
            field=models.CharField(choices=[('Pertama', 'Pertama'), ('Kedua', 'Kedua'), ('Ketiga', 'Ketiga'), ('Keempat', 'Keempat'), ('Kelima', 'Kelima'), ('Keenam', 'Keenam'), ('Ketujuh', 'Ketujuh'), ('Kedelapan', 'Kedelapan'), ('Kesembilan', 'Kesembilan')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='link_gmap',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='link_gmap_akad',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='link_gmap_resepsi',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='link_gmap_unduhmantu',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='link_iframe',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='livestream',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='lnama_ayah',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='lnama_ibu',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='lname',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='location',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='lokasi',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='lpicture',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format='JPEG', keep_meta=True, null=True, quality=100, scale=1, size=[180, 180], upload_to='whatever'),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='name',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='options',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='panak_ke',
            field=models.CharField(choices=[('Pertama', 'Pertama'), ('Kedua', 'Kedua'), ('Ketiga', 'Ketiga'), ('Keempat', 'Keempat'), ('Kelima', 'Kelima'), ('Keenam', 'Keenam'), ('Ketujuh', 'Ketujuh'), ('Kedelapan', 'Kedelapan'), ('Kesembilan', 'Kesembilan')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='pnama_ayah',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='pnama_ibu',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='pname',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='ppicture',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format='JPEG', keep_meta=True, null=True, quality=100, scale=1, size=[180, 180], upload_to='whatever'),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='startDate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='startTime',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='tanggal_akad',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='tanggal_resepsi',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='tanggal_unduhmantu',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='tempat_akad',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='tempat_resepsi',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='tempat_unduhmantu',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='timeZone',
            field=models.CharField(choices=[('', 'Pilih zona waktu'), ('Asia/Jakarta', 'WIB'), ('Asia/Makassar', 'WITA'), ('Asia/Jayapura', 'WIT')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='trigger',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='video',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='waktu_akad',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='waktu_resepsi',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='waktu_selesai_akad',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='waktu_selesai_resepsi',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='waktu_selesai_unduhmantu',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='waktu_unduhmantu',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='ayat',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='kutipan',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='rekening',
            name='bank',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='rekening',
            name='kode',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='specialinvitation',
            name='name_invite',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='cerita',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='story',
            name='year',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='theme',
            name='cover_fitur',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='theme',
            name='line',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='theme',
            name='name',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='theme',
            name='open_fitur',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='theme',
            name='quote_fitur',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='theme',
            name='rundown_fitur',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='theme',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='theme',
            name='space',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='ucapan',
            name='alamat',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='ucapan',
            name='nama',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='ucapan',
            name='pesan',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
