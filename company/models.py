from functools import update_wrapper
from django.db import models



e_seviyesi = (('Lisans', 'Lisans'),
             ('yükseklisans', 'yükseklisans'),
              ('doktora', 'doktora'))

bg = (('A+', 'A+'), ('A-', 'A-'), ('AB+', 'AB+'),
      ('AB-', 'AB-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'))

haftanin_gunleri = (
    ('Pazartesi', 'Pazartesi'),
    ('Salı', 'Salı'),
    ('Çarşamba', 'Çarşamba'),
    ('Perşembe', 'Perşembe'),
    ('Cuma', 'Cuma'),
    ('Cumartesi', 'Cumartesi'),
    ('Pazar', 'Pazar')
)

a_t = (
    ('Biontech', 'Biontech'),
    ('Sinovac', 'Sinovac')
)



class Personel(models.Model):
    tc                      = models.CharField(max_length=11, primary_key=True, null=False)
    ad                      = models.CharField(max_length=30, null=False)
    soyad                   = models.CharField(max_length=30, null=False)
    kan_grubu               = models.CharField(max_length=3, null=False, choices=bg)
    sehir                   = models.CharField(max_length=30, null=False)
    posizyon                = models.CharField(max_length=30, null=False, blank=True)
    maas                    = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    hobbiler                = models.TextField(null=True)
    egitim_seviyesi         = models.CharField(max_length=30, null=False, choices=e_seviyesi)

    def __str__(self):
        return self.ad + " " + self.soyad

class Covid(models.Model):
    covid_id                = models.AutoField(primary_key=True)
    personel                = models.ForeignKey(Personel, on_delete=models.CASCADE, null=False)
    p_tarih                 = models.DateField(auto_now=False, auto_now_add=False, null=False)
    n_tarih                 = models.DateField(auto_now=False, auto_now_add=False, null=False)
    asili_mi                = models.BooleanField(null=False, default=False)
    asi_tipi                = models.CharField(max_length=30, choices=a_t, null=True, blank=True)
    doz                     = models.IntegerField(null=True, blank=True)
    temasli                 = models.ManyToManyField("TemasliKisi", blank=True)
    kronik                  = models.ManyToManyField("KronikHastalik", blank=True)
    c_semp                  = models.ManyToManyField("Semptomlar", blank=True)

    def __str__(self):
        return '(' + str(self.p_tarih) + ')'

class Semptomlar(models.Model):
    semptom_isim            = models.CharField(max_length=60, primary_key=True, null=False)

    def __str__(self):
        return self.semptom_isim


class TemasliKisi(models.Model):
    id                      = models.AutoField(primary_key=True)
    pers                    = models.ForeignKey(Personel, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.pers)


class KronikHastalik(models.Model):
    kronik_isim             = models.CharField(max_length=60, primary_key=True, null=False)
    def __str__(self):
        return self.kronik_isim




class ilac(models.Model):
    ilac_id                = models.AutoField(primary_key=True)
    isim                   = models.CharField(max_length=30, null=False)
    def __str__(self):
        return 'ID  ' + str(self.ilac_id) + ' ----- ' + self.isim

class Recete(models.Model):
    recete_id          = models.AutoField(primary_key=True)
    ilac_id            =models.ManyToManyField("ilac")

    def __str__(self):
        return str(self.recete_id)



class Hastalik(models.Model):
    h_id                   = models.CharField(max_length=5, primary_key=True)
    h_isim                 = models.CharField(max_length=30, null=False)
    teshis_tarih           = models.DateField(auto_now=False, auto_now_add=False, null=False)
    per                    = models.ForeignKey(Personel, on_delete=models.CASCADE)
    h_semp                 = models.ManyToManyField(Semptomlar, blank=True)
    recete                 = models.ForeignKey(Recete, on_delete=models.CASCADE)

    def __str__(self):
        return self.h_isim

class Mesai(models.Model):
    gun                     = models.CharField(max_length=32, null=False, choices=haftanin_gunleri)
    mesai_baslangic          = models.TimeField(auto_now=False, auto_now_add=False, null=False)
    mesai_bitis             = models.TimeField(auto_now=False, auto_now_add=False, null=False)
    per                     = models.ForeignKey(Personel, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return str(self.per) + ' ' + self.gun




class EgitimCovid(models.Model):
    egitim_seviyesi = models.CharField(max_length=30, null=False, choices=e_seviyesi, primary_key=True)
    sayim = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'egitim_covid'

    def __str__(self):
        return self.egitim_seviyesi


class EnYayginHastaliklar(models.Model):
    h_isim = models.CharField(max_length=30, primary_key=True, null=False)
    d_count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'en_yaygin_hastaliklar'

    def __str__(self):
        return self.h_isim + '(' + str(self.d_count) + ')'

class EnYayginHastalikPer(models.Model):
    tc = models.CharField(primary_key=True, max_length=11, null=False)
    ad = models.CharField(max_length=30)
    soyad = models.CharField(max_length=30)
    h_isim = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'en_yaygin_hastaliklar_per'

    def __str__(self):
        return self.tc + '(' + str(self.h_isim)+')'


class KanGrubuCovidSklk(models.Model):
    kan_grubu = models.CharField(primary_key=True, max_length=3)
    toplamsayi = models.DecimalField(max_digits=3, decimal_places=2)

    class Meta:
        managed = False
        db_table = "kan_grubu_covid_sklk"

    def __str__(self):
        return self.kan_grubu + " - " + str(self.toplamsayi)

class CovidPerMesaiSaatDurumu(models.Model):
    haftalik_saat = models.DecimalField(max_digits=5, decimal_places=2, primary_key=True)
    per_sayisi = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = "covid_per_mesai_saat_durumu"

    def __str__(self):
        return str(self.haftalik_saat) + " - " + str(self.per_sayisi)


class EnYayginCovidSemptomlari(models.Model):
    semptom = models.CharField(max_length=30, primary_key=True)
    semptom_say = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = "en_yaygin_covid_semptomlari"

    def __str__(self):
        return str(self.semptom) + " - " + str(self.semptom_say)


class EnTemasliInsanlar(models.Model):
    tc = models.CharField(max_length=11, primary_key=True)
    ad = models.CharField(max_length=30)
    soyad = models.CharField(max_length=30)
    temas_say = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = "temaslikisiler"

    def __str__(self):
        return str(self.tc) + " - " + self.ad + " " + self.soyad + "(" + str(self.temas_say) + ")"

class BiontechCovidliPer(models.Model):
    toplam_sure = models.DecimalField(max_digits=6, decimal_places=2, primary_key=True)
    per_sayisi = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = "biontech_covidli_per"

    def __str__(self):
        return str(self.toplam_sure) + "(" + str(self.per_sayisi) + ")"


class SinovacCovidliPer(models.Model):
    toplam_sure = models.DecimalField(max_digits=6, decimal_places=2, primary_key=True)
    per_sayisi = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = "sinovac_covidli_per"




class HaftasonuPersonel(models.Model):
    tc = models.CharField(max_length=11, primary_key=True)
    ad = models.CharField(max_length=30)
    soyad = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = "haftasonu_per"


class HaftasonuPersonelCovid(models.Model):
    tc = models.CharField(max_length=11, primary_key=True)
    ad = models.CharField(max_length=30)
    soyad = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = "haftasonu_per_covid"


class EnSkHastaPersonel(models.Model):
    per_id = models.CharField(max_length=11, primary_key=True)
    hastalik_sayim = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = "en_sk_hasta_per"


class EnSkHastaPersonelCovid(models.Model):
    tc = models.CharField(max_length=11, primary_key=True)
    ad = models.CharField(max_length=30)
    soyad = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = "en_sk_hasta_per_covid"


class AsisizPersonel(models.Model):
    tc = models.CharField(max_length=11, primary_key=True)
    ad = models.CharField(max_length=30)
    soyad = models.CharField(max_length=30)
    covid_t = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        managed = False
        db_table = "asisiz_personel"


class AsisizPersonelHastalikReceteBilgisi(models.Model):
    h_isim = models.CharField(max_length=30)
    recete_id = models.CharField(max_length=5, primary_key=True)

    class Meta:
        managed = False
        db_table = "asisiz_personel_hastalik"


class EnYayginIlaclar(models.Model):
    ilac_isim = models.CharField(max_length=32, primary_key=True)
    ilac_sayim = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = "en_yaygin_ilaclar"


class EnYayginIlacKullananlar(models.Model):
    tc = models.CharField(max_length=11, primary_key=True)
    ad = models.CharField(max_length=32)
    soyad = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = "en_yaygin_ilac_kullananlar"


class BelirliBirIlacKullananlar(models.Model):
    tc = models.CharField(max_length=11, primary_key=True)
    ad = models.CharField(max_length=30)
    soyad = models.CharField(max_length=30)
    ilac = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = "belirli_bir_ilaci_kullananlar"

class BelirliBirILaciKullananlarCovid(models.Model):
    tc = models.CharField(max_length=11, primary_key=True)
    ad = models.CharField(max_length=30)
    soyad = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = "belirli_bir_ilaci_kullananlar_covid"


class BiontechBelirliHastalikCovid(models.Model):
    tc = models.CharField(max_length=11, primary_key=True)
    ad = models.CharField(max_length=30)
    soyad = models.CharField(max_length=30)
    h_isim = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'biontech_belirli_hastalik_covid'



class BelirliKronikHastalikCovidSuresi(models.Model):
    kronik_hastalik = models.CharField(max_length=60)
    gun_sayisi = models.DecimalField(max_digits=12, decimal_places=0, primary_key=True)
    hasta_sayisi = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'belirli_kronik_hastalik_covid_suresi'

class BelirliSehirHastalik(models.Model):
    ad = models.CharField(max_length=60, primary_key=True)
    soyad = models.CharField(max_length=30)
    sehir = models.CharField(max_length=60)
    h_isim = models.CharField(max_length=60)
    class Meta:
        managed = False
        db_table = 'belirli_sehir_hastalik'