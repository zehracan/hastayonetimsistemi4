Gereklilikler:
psycopg2 ve crispy_forms paketlerini algılamazsa manuel olarak indiriniz.(uyumluluğa dikkat ediniz)
django 3.0.0 aşağısı sürümlerde paketlerin çalışmasında sorun olabilir. Django sürümünü yükseltin ya da ilgili paketleri manuel olarak indirin.
python-3.8 +

Projeyi kendi veritabanınız ile ilişkilendirmek için postgresql kısmında kendi port ve host numaranızı verebilirsiniz.

Bu proje aşağıdaki maddeleri yerine getirebilir:
- Çalışanlara ilişkin olarak, tabloda yer alan tüm özelliklerine ilişkin sorgulamalar gerçekleştirebilecek yetenekte olması. Yeni bir çalışan ekleyebilme, var olanı silebilme ve güncelleyebilme.
- Her elemanla ilgili yeni bir hastalık ve reçete bilgisi girilebilir, güncellenebilir gerekirse silinebilir..
- Her elemanla ilgili COVID bilgisi girilebilir, güncellenebilir gerekirse silinebilir..
- Her elemanla ilgili çalışma saati bilgisi girilebilir, güncellenebilir gerekirse silinebilir..
- Eğitim durumu ile COVID geçirme arasındaki istatistiki bilgi çıkarılabilir.
- Elemanlar arasında görülen en yaygın üç hastalık türü rapor edilebilmeli ve hastalığa sahip olan elemanların listesi çıkarılabilir.
- Belirli şehirde doğan elemanlar arasında en sık görülen ilk üç hastalık rapor edilebilir.
- En yaygın kullanılan ilk üç ilacı kullanan elemanların COVID geçirme durumu rapor edilebilir.
- Belirli bir ilacı kullanan çalışanların COVID geçirme durumu rapor edilebilir.
- Biontech aşısı olan ve belirli bir hastalığı önceden geçirmiş olan çalışanlardan COVID’e yakalananlar listelenebilir.
- Aşı vurulma durumuna göre COVID hastalığına yakalanma oranı rapor edilebilir.
- Belirli bir kronik hastalığa göre, çalışanların COVID testinin negatife dönmesi için geçen süre rapor edilebilir.
- Kan grubuna göre COVID’e yakalanma sıklığı rapor edilebilir.
- Toplam çalışma süresi ile COVID’e yakalanma arasındaki istatistiki bilgi sunulabilir.
- COVID’e yakalananlar arasında görülen en sık karşılaşılan ilk 3 belirti listelenebilir.
- En fazla temasta bulunmuş ilk 3 çalışan listelenebilir.
- Biontech ve sinovac aşılarının etkinliği, COVID geçirme süresi göz önüne alınarak kıyaslanabilir.
- Haftasona çalışan kişiler arasında COVID gözükme miktarı analiz edilebilir.
- En sık hasta olan ilk 10 kişinin son bir ay içerisinde COVID’e yakalanma durumları listelenebilir.
- Aşı vurulmayanlar arasında, en uzun süre COVID geçiren kişinin, son 1 yılda geçirmiş olduğu hastalıklar ve verilen reçeteler listelenebilir.
Siteye ait bazı sayfaların görüntüsü şöyledir:
ANASAYFA:
![ANASAYFAA](https://user-images.githubusercontent.com/61902608/167526067-66a5a0cc-5481-4486-9f71-c2de39e590d3.png)




ADMİN(reçete verme, reçeteye ilaç ekleme gibi özel işlemler admin panelinde yapılır.)
![admin1](https://user-images.githubusercontent.com/61902608/167526471-84cf4d5d-6613-49ec-9655-aae6170e206e.png)
![admin2](https://user-images.githubusercontent.com/61902608/167526489-fe89df9f-e99e-4b68-b385-4ad72f0e6833.png)



PERSONELE AİT İŞLEMLER:
![personel](https://user-images.githubusercontent.com/61902608/167525599-7cc9dbda-c301-4aa8-920a-4254abf4a731.png)

HASTALIK KAYDI:
![hastalık](https://user-images.githubusercontent.com/61902608/167525669-4e111d43-a08c-40b8-bffa-ce875172723b.png)


Covid-19 ve AŞI KAYDI:
![COVİD](https://user-images.githubusercontent.com/61902608/167525770-ebcd1e9d-d9a3-4b1b-84ba-eccda6c6898a.png)

EĞİTİM DÜZEYİ- COVİD GÖRÜLME İLİŞKİSİ
![image](https://user-images.githubusercontent.com/61902608/167525834-c06c1c6a-f3f1-4f6a-8201-fada5bcb244d.png)

ŞİRKETTEKİ COVİD HASTALARI ARASINDA EN SIK GÖRÜLEN BELİRTİLER:
![SEMPTOM](https://user-images.githubusercontent.com/61902608/167525929-0152a9e0-5107-496f-afec-cb28c90ebdd6.png)


![image](https://user-images.githubusercontent.com/61902608/167527713-70cf5acd-1d6f-4d85-b2af-72888c9ed1ec.png)



