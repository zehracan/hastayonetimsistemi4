# Generated by Django 4.0 on 2022-01-01 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ilac',
            fields=[
                ('ilac_id', models.AutoField(primary_key=True, serialize=False)),
                ('isim', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='KronikHastalik',
            fields=[
                ('kronik_isim', models.CharField(max_length=60, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Personel',
            fields=[
                ('tc', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('ad', models.CharField(max_length=30)),
                ('soyad', models.CharField(max_length=30)),
                ('kan_grubu', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-')], max_length=3)),
                ('sehir', models.CharField(max_length=30)),
                ('posizyon', models.CharField(blank=True, max_length=30, null=True)),
                ('maas', models.DecimalField(decimal_places=2, max_digits=12)),
                ('hobbiler', models.TextField(null=True)),
                ('egitim_seviyesi', models.CharField(choices=[('lisans', 'lisans'), ('yükseklisans', 'yükseklisans'), ('doktora', 'doktora')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Semptomlar',
            fields=[
                ('semptom_isim', models.CharField(max_length=60, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='TemasliKisiler',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pers', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Recete',
            fields=[
                ('recete_id', models.AutoField(primary_key=True, serialize=False)),
                ('ilac_id', models.ManyToManyField(to='company.ilac')),
            ],
        ),
        migrations.CreateModel(
            name='Mesai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gun', models.CharField(choices=[('Pazartesi', 'Pazartesi'), ('Salı', 'Salı'), ('Çarşamba', 'Çarşamba'), ('Perşembe', 'Perşembe'), ('Cuma', 'Cuma'), ('Cumartesi', 'Cumartesi'), ('Pazar', 'Pazar')], max_length=32)),
                ('mesai_baslangic', models.TimeField()),
                ('mesai_bitis', models.TimeField()),
                ('per', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.personel')),
            ],
        ),
        migrations.CreateModel(
            name='Hastalik',
            fields=[
                ('h_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('h_isim', models.CharField(max_length=30)),
                ('teshis_tarih', models.DateField()),
                ('h_semp', models.ManyToManyField(blank=True, to='company.Semptomlar')),
                ('per', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.personel')),
                ('recete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.recete')),
            ],
        ),
        migrations.CreateModel(
            name='Covid',
            fields=[
                ('covid_id', models.AutoField(primary_key=True, serialize=False)),
                ('p_tarih', models.DateField()),
                ('n_tarih', models.DateField()),
                ('asili_mi', models.BooleanField(default=False)),
                ('asi_tipi', models.CharField(blank=True, choices=[('Biontech', 'Biontech'), ('Sinovac', 'Sinovac')], max_length=30, null=True)),
                ('doz', models.IntegerField(blank=True, null=True)),
                ('c_semp', models.ManyToManyField(blank=True, to='company.Semptomlar')),
                ('kronik', models.ManyToManyField(blank=True, to='company.KronikHastalik')),
                ('personel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.personel')),
                ('temasli', models.ManyToManyField(blank=True, to='company.TemasliKisiler')),
            ],
        ),
    ]
