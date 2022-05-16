from django import urls
from django.urls import path
from .views import *
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    # path("", baslik, name="baslik"),
    path("", index, name="baslik"),

    path('personel/', PersonelTablosu.as_view(), name="personel"),
    path("personel-olustur/", PersonelOLusturma.as_view(), name="personel-olustur"),
    path("personel-guncelleme/<str:pk>/", PersonelGuncelleme.as_view(), name="personel-guncelleme"),
    path("personel-silme/<str:pk>/", PersonelSilme.as_view(), name="personel-silme"),



    path("hastalik", HastalikBilgileri.as_view(), name="hastalik"),
    path("hastalik-olusturma", HastalikOlusturma.as_view(), name="hastalik-olusturma"),
    path("hastalik-guncelleme/<str:pk>/", HastalikGuncelleme.as_view(), name="hastalik-guncelleme"),
    path("hastalik-silme/<str:pk>/", HastalikSilme.as_view(), name="hastalik-silme"),

    path("recete", ReceteListesi.as_view(), name="recete"),
    path("recete-olustur/", ReceteOlusturma.as_view(), name="recete-olustur"),

    path("covid", CovidListesi.as_view(), name="covid"),
    path("covid-olustur", CovidOlustur.as_view(), name="covid-olustur"),
    path("covid-guncelleme/<int:pk>/", CovidGuncelleme.as_view(), name="covid-guncelleme"),
    path("covid-silme/<int:pk>/", CovidSilme.as_view(), name="covid-silme"),

    path("mesai", MesaiListesi.as_view(), name="mesai"),
    path("mesai-olusturma", MesaiOlusturma.as_view(), name="mesai-olusturma"),
    path("mesai-guncelleme/<int:pk>/", MesaiGuncelleme.as_view(), name="mesai-guncelleme"),
    path("mesai-silme/<int:pk>/", MesaiSilme.as_view(), name="mesai-silme"),

    path('egitim-covid-durumu/', egitim_covid, name="egitim-covid-durumu"),

    path('en_yaygin_hastaliklar/', en_yaygin_hastaliklar, name="en_yaygin_hastaliklar"),
    path('en_yaygin_ilaclar/', en_yaygin_ilaclar, name="en_yaygin_ilaclar"),
    path("en_yaygin_covid_semptomlari/", en_yaygin_covid_semptomlari, name="en_yaygin_covid_semptomlari"),
    path("en_temasli_insanlar/", en_temasli_insanlar, name="en_temasli_insanlar"),
    path("men_sk_hasta_per_covid/", en_sk_hasta_per_covid, name="en_sk_hasta_per_covid"),

    path('sehir_yaygin_hastaliklar/',belirli_sehir_hastalik, name="sehir_yaygin_hastaliklar"),
    path("kan_grubu_covid_sklk/", kan_grubu_covid_sklk, name="kan_grubu_covid_sklk"),
    path("covid_per_mesai_saat_durumu/", covid_per_mesai_saat_durumu, name="covid_per_mesai_saat_durumu"),

    path("haftasonu_personel_covid_durumu/", haftasonu_personel_covid_durumu, name="haftasonu_personel_covid_durumu"),


    path("asiliasisiz/", asiliasisiz, name="asiliasisiz"),
    path("asisiz-personel-bir-yıl-covid/", asisiz_personel_hastalik, name="asisiz-personel-bir-yıl-covid"),






    path("biontech-vs-sinovac/", biontech_sinovac_oran, name="biontech-vs-sinovac"),



    path("biontech-belirli-hastalik-covid/", biontech_belirli_hastalik_covid, name="biontech-belirli-hastalik-covid"),


    path("kullaniciGiris/", kullaniciGiris, name="kullaniciGiris"),
    path("kullaniciCikis/", kullaniciCikis, name="kullaniciCikis"),
    path("belirli-bir-ilaci-kullananlar/", belirli_bir_ilaci_kullananlar, name="belirli-bir-ilaci-kullananlar"),
    path("belirli-kronik-hastalik-covid-suresi/", belirli_kronik_hastalik_covid_suresi, name="belirli-kronik-hastalik-covid-suresi"),


]

