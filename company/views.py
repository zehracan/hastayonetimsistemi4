from django.http import HttpResponse
from django.db import models
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import *

from .models import *

# Create your views here.

# employee

def index(request):
    return render(request, 'index.html', {})



class PersonelTablosu(ListView):
    model = Personel
    context_object_name = 'personeller'
    template_name = 'Personel/personel-bilgileri.html'


class PersonelOLusturma(CreateView):
    model = Personel
    fields = '__all__'
    success_url = reverse_lazy('personel')
    template_name = 'Personel/personel-form.html'


class PersonelGuncelleme(UpdateView):
    model = Personel
    fields = '__all__'
    success_url = reverse_lazy('personel')
    template_name = 'Personel/personel-form.html'


class PersonelSilme(DeleteView):
    model = Personel
    context_object_name = 'personel'
    success_url = reverse_lazy('personel')
    template_name = 'personel/personel-silme.html'



class HastalikBilgileri(ListView):
    model = Hastalik
    context_object_name = 'hastaliklar'
    template_name = 'Hastalik/hastalik-bilgileri.html'


class HastalikOlusturma(CreateView):
    model = Hastalik
    fields = '__all__'
    success_url = reverse_lazy('hastalik')
    template_name = 'Hastalik/hastalik-form.html'


class HastalikGuncelleme(UpdateView):
    model = Hastalik
    fields = '__all__'
    success_url = reverse_lazy('hastalik')
    template_name = 'Hastalik/hastalik-form.html'


class HastalikSilme(DeleteView):
    model = Hastalik
    context_object_name = 'hastalik'
    success_url = reverse_lazy('hastalik')
    template_name = 'Hastalik/hastalik-silme.html'




class CovidListesi(ListView):
    model = Covid
    context_object_name = 'covid_listesi'
    template_name = 'Covid/covid-listesi.html'


class CovidOlustur(CreateView):
    model = Covid
    fields = '__all__'
    success_url = reverse_lazy('covid')
    template_name = 'Covid/covid-bilgileri.html'


class CovidGuncelleme(UpdateView):
    model = Covid
    fields = '__all__'
    success_url = reverse_lazy('covid')
    template_name = 'Covid/covid-bilgileri.html'


class CovidSilme(DeleteView):
    model = Covid
    context_object_name = 'covid'
    success_url = reverse_lazy('covid')
    template_name = 'Covid/covid-silme.html'



class MesaiListesi(ListView):
    model = Mesai
    context_object_name = 'mesailer'
    template_name = 'Mesai/mesai.html'


class MesaiOlusturma(CreateView):
    model = Mesai
    fields = '__all__'
    success_url = reverse_lazy('mesai')
    template_name = 'Mesai/mesai-bilgileri.html'


class MesaiGuncelleme(UpdateView):
    model = Mesai
    fields = '__all__'
    success_url = reverse_lazy('mesai')
    template_name = 'Mesai/mesai-bilgileri.html'


class MesaiSilme(DeleteView):
    model = Mesai
    context_object_name = 'mesai'
    success_url = reverse_lazy('mesai')
    template_name = 'Mesai/mesai-silme.html'

class  ReceteListesi(ListView):
    model = Recete
    context_object_name = 'recete'
    template_name = 'Recete/recete-bilgileri.html'

class ReceteOlusturma(CreateView):
    model = Recete
    fields = '__all__'
    success_url = reverse_lazy('recete')
    template_name = ''



def egitim_covid(request):
    egitimler = EgitimCovid.objects.all()
    lisans_say = 0
    yukseklisans_say = 0
    doktora_say = 0
    lisans_t = 0
    yukseklisans_t = 0
    doktora_t = 0
    toplam = 0
    for i in egitimler:
        if i.egitim_seviyesi == "doktora":
            doktora_say += i.sayim
        if i.egitim_seviyesi == "yükseklisans":
            yukseklisans_say += i.sayim
        if i.egitim_seviyesi == "lisans":
            lisans_say += i.sayim
    toplam = lisans_say + yukseklisans_say + doktora_say
    if toplam != 0:

        doktora_t = (doktora_say * 100) / toplam
        yukseklisans_t = (yukseklisans_say * 100) / toplam
        lisans_t = (lisans_say * 100) / toplam

    context = {
        'doktora_t': doktora_t,
        'yukseklisans_t': yukseklisans_t,
        'lisans_t': lisans_t,
        'lisans_say': lisans_say,
        'yukseklisans_say': yukseklisans_say,
        'doktora_say': doktora_say,
        'toplam': toplam,
        'seviye': EgitimCovid.objects.all(),
        'covidsayim': Covid.objects.all()



    }
    return render(request, 'Egitim/egitim-covid-durumu.html',context)

def en_yaygin_hastaliklar(request):
    hastaliklar = EnYayginHastaliklar.objects.all()
    personeller = EnYayginHastalikPer.objects.all()

    context = {
        'secimler': hastaliklar,
        'personeller': personeller
    }

    return render(request, 'En/en_yaygin-hastaliklar.html', context)




def kan_grubu_covid_sklk(request):
    per_grup = KanGrubuCovidSklk.objects.all()
    context = {
        'pergruplari': per_grup
    }
    return render(request, "kan_grubu_covid_sklk.html",context)



def en_yaygin_ilaclar(request):
    context = {
        "en_yaygin_ilaclar": EnYayginIlaclar.objects.all(),
        "en_yaygin_ilac_kullananlar": EnYayginIlacKullananlar.objects.all()
    }
    return render(request, 'En/en_yaygin_ilaclar.html', context)

def asiliasisiz(request):
    asili_sayac = 0
    asisiz_sayac = 0
    toplam = 0
    covid_personel = Covid.objects.all()
    for personel in covid_personel:
        if(personel.asili_mi == True):
            asili_sayac += 1

        else:
            asisiz_sayac += 1
    toplam = asili_sayac + asisiz_sayac
    asili_per = asili_sayac/toplam
    asisiz_per = asisiz_sayac/toplam

    context = {
        "aşılı_sayaç": asili_sayac,
        "aşısız_sayaç": asisiz_sayac,
        "aşılı_per": asili_per,
        "aşısız_per": asisiz_per,
        "toplam": toplam
    }
    return render(request, "asili-vs-asisiz.html",context)


def covid_per_mesai_saat_durumu(request):
    per_grup = CovidPerMesaiSaatDurumu.objects.all()
    context = {
        'pergrups': per_grup
    }
    return render(request,'Mesai/covid-mesai-saat-durumu.html',context)

def en_yaygin_covid_semptomlari(request):
    semptomlar = EnYayginCovidSemptomlari.objects.all()
    context = {
        'semptomlar': semptomlar
    }
    return render(request,"En/en-yaygin-covid-semptomlari.html",context)

def en_temasli_insanlar(request):
    context = {
        'personeller': EnTemasliInsanlar.objects.all()
    }
    return render(request, "En/en-temasli-insanlar.html", context)


def biontech_sinovac_oran(request):
    biontech = BiontechCovidliPer.objects.get()
    sinovac = SinovacCovidliPer.objects.get()
    biontech_ortalama = biontech.toplam_sure/biontech.per_sayisi
    sinovac_ortalama = sinovac.toplam_sure/sinovac.per_sayisi
    context = {

        "biontech": biontech,
        "sinovac": sinovac,
        "biontech_ortalama": biontech_ortalama,
        "sinovac_ortalama":sinovac_ortalama

    }
    return render(request, 'biontech-vs-sinovac-covid-per.html', context)


def haftasonu_personel_covid_durumu(request):
    personeller = HaftasonuPersonel.objects.all()
    covidlipersonel = HaftasonuPersonelCovid.objects.all()

    context = {
        'personeller': personeller,
        'covidlipersonel': covidlipersonel
    }

    return render(request, "Mesai/haftasonu_personel_covid_durumu.html",context)


def en_sk_hasta_per_covid(request):
    personeller = EnSkHastaPersonel.objects.all()
    covidli_personel = EnSkHastaPersonelCovid.objects.all()

    context = {
        'personeller': personeller,
        'covidli_personeller': covidli_personel
    }

    return render(request,"En/en-sk-hastalanan-personel-covid.html", context, )


def asisiz_personel_hastalik(request):
    personel = AsisizPersonel.objects.all()
    hasta_personel = AsisizPersonelHastalikReceteBilgisi.objects.all()

    context = {
        'personeller': personel,
        'hastapersoneller': hasta_personel,
        'covidpersonel': Covid.objects.all()
    }

    return render(request, "asisiz-covid-bir-sene.html", context)




def biontech_belirli_hastalik_covid(request):
    personeller = BiontechBelirliHastalikCovid.objects.all()

    context = {
        'personeller': personeller,
    }

    return render(request, 'Belirli/biontech-belirli-hastalik.html', context)


def belirli_kronik_hastalik_covid_suresi(request):
    sure = BelirliKronikHastalikCovidSuresi.objects.get()
    ort_sure = sure.gun_sayisi/sure.hasta_sayisi
    context = {
        'sure': sure,
        'ort_sure':ort_sure
    }
    return render(request, 'Belirli/belirli_kronik_hastalik_covid_suresi.html', context)


def belirli_bir_ilaci_kullananlar(request):
    ilackullananlar = BelirliBirIlacKullananlar.objects.all()
    ilackullanancovidliler = BelirliBirILaciKullananlarCovid.objects.all()

    context = {
        'ilackullananlar': ilackullananlar,
        'ilackullanancovidliler': ilackullanancovidliler
    }
    return render(request, 'Belirli/belirli_bir_ilaci_kullananlar.html', context)


def belirli_sehir_hastalik(request):
    personeller = BelirliSehirHastalik.objects.all()

    context = {
        'personeller': personeller,
    }

    return render(request, 'Belirli/şehir-yaygın-hastalıklar.html', context)



def kullaniciGiris(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("baslik")
        else:
            return render(request, "KullaniciGirisi/kullanicigirisi.html", {
                "error": "bu kullani adi veya sifresi bulunmamaktadir"
            })
    else:
        return render(request, "KullaniciGirisi/kullanicigirisi.html")


def kullaniciCikis(request):
    logout(request)
    return redirect("baslik")