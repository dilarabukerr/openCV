# PYTHON HATIRLATMA

# liste
"""
* Listeler, Python'un bileşik veri türlerinin çok yönlü olanıdır. 
* Bir liste, virgülle ayrılmış ve köşeli parantez ([]) içine alınmış öğeler içerir. 
* Listeler bir dereceye kadar C'deki dizilere benzer. 
* Aralarındaki bir fark, bir listeye ait tüm öğelerin farklı veri türünde olabilmesidir.
"""
liste = [1,2,3,4,5,6]
print(type(liste))

# listenin ilk elemanı
# python da index sıfırdan başlar
hafta = ["pazartesi","salı","çarşamba","perşembe","cuma","cumartesi","pazar"]
print(hafta[0])

# listenin son elemanı
print(hafta[-1])

# listenin eleman sayısı
print(len(hafta))

# listenin ikinci, üçüncü ve dördüncü elemanı
print(hafta[2:5]) # hafta[x,y]: x = dahil, y = dahil değil

sayı_listesi = [1,3,2,4,6,5]
sayı_listesi.append(7) # sona eleman ekler
print(sayı_listesi)

sayı_listesi = [1,3,2,4,6,5]
sayı_listesi.remove(4) # istenilen elemanı çıkarır
print(sayı_listesi)

sayı_listesi = [1,3,2,4,6,5]
sayı_listesi.reverse() # listeyi ters çevirir
print(sayı_listesi)

sayı_listesi = [1,3,2,4,6,5]
sayı_listesi.sort() # listeyi küçükten büyüğe sıralar
print(sayı_listesi)

# tuple
"""
* Python koleksiyonlarından olan Tuple sıralı ve değiştirilemez bir koleksiyon çeşididir. 
* ( ) parantezler kullanılarak yazılır. 
* Tuple salt okunur listeler olarak düşünülebilir.
"""
tuple_veritipi = (1,2,3,3,4,5,6)
print(tuple_veritipi[0]) # ilk eleman = sıfırıncı index

tuple_veritipi = (1,2,3,3,4,5,6)
print(tuple_veritipi[2:]) # 2. indexten sonraki elemanları yazdır

tuple_veritipi = (1,2,3,3,4,5,6)
print(tuple_veritipi.count(3)) # 3 sayısının kaç tane olduğunu hesaplar

tuple_xyz = (1, 2, 3)
x,y,z = tuple_xyz
print(x,y,z) 
#  deque
"""
Bilgisayar biliminde, çift uçlu kuyruk, kuyruğu genelleştiren, önden veya arkaya elemanların eklenebileceği veya önden çıkarılabileceği soyut bir veri türüdür.
"""
from collections import deque
dq = deque(maxlen = 3)
dq.append(1)
print(dq)
dq.append(2)
print(dq)
dq.append(3)
print(dq)
dq.append(4)
print(dq)

dq = deque(maxlen = 3)
dq.append(1)
print(dq)
dq.append(2)
print(dq)
dq.appendleft(3)
print(dq)

dq.clear()
print(dq)
# Dictionary
"""
* Python'un sözlükleri bir çeşit karma tablo türüdür. 
* Anahtar-değer çiftlerinden oluşurlar. 
* Sözlük anahtarı hemen hemen her Python türü olabilir, ancak genellikle sayılar veya dizelerdir. 
* Öte yandan değerler, herhangi bir rastgele Python nesnesi olabilir.
* Örneğin: {"Anahtar": değer}
"""
dictionary = {"İstanbul":34, "İzmir":35, "Konya":42}
print(dictionary)

print(dictionary['İstanbul'])   # istanbul anahtarının değeri

print(dictionary.keys())# tüm anahtarlar

print(dictionary.values()) # tüm değerler
# if - else
"""
* Koşullu ifadeler ve koşullu yapılar, programcı tarafından belirtilen bir boole koşulunun 
doğru veya yanlış olarak değerlendirilmesine bağlı olarak farklı hesaplamalar veya eylemler gerçekleştiren bir özelliktir.

"""
# büyük küçük karşılaştırması
sayi1 = 12.0
sayi2 = 20.0
if sayi1 < sayi2:
    print("sayi1 küçüktür sayi2")
elif sayi1 > sayi2:
    print("sayi1 büyüktür sayi2")
else: print("sayi1 eşittir sayi2")


liste = [1,2,3,4,5]
deger = 31
if deger in liste:
    print("{} degeri listenin icinde".format(deger))
else:
    print("{} degeri listenin icinde DEĞİL".format(deger))
    
    
dictionary = {"Türkiye":"Ankara", "İngiltere":"Londra", "İspanya":"Madrid"}
keys = dictionary.keys()
deger = "Türkiye"
if deger in keys:
    print("{} degeri sözlüğün içinde".format(deger))
else:
    print("{} degeri sözlüğün içinde DEĞİL".format(deger))
   
str1 = True 
str2 = False
if str1 or str2: # and
    print("basari")
else:
    print("non basari")

# Döngüler
"""
* Bir dizi üzerinde yineleme yapmak için for döngüsü kullanılır. Bu dizi bir liste, bir sözlük, veya bir metindir.
"""

# for
# range 1'den 11'e kadar değerleri i parametresine her iterasyonda yazar
for i in range(1,11):
    print(i)
    
liste = [1,4,5,6,8,3,3,4,67]
# for döngüsü ile toplama
count = 0
for c in liste:
    count = count + c
print(count)
 
tup1 = ((1,2,3),(3,4,5))
for x,y,z in tup1:
    print(x+y+z)
    
# while 
i = 0
while(i <4):
    print(i)
    i = i + 1    
    
# while ile toplama
iste = [1,4,5,6,8,3,3,4,67]

sinir = len(liste)   
her = 0
hesapla = 0
while(her < sinir):
    hesapla = hesapla + liste[her]
    her = her + 1 
hesapla

#  fonksiyonlar
"""
* Fonksiyonların görevi, karmaşık işlemleri bir araya toplayarak, bu işlemleri tek adımda yapmamızı sağlamaktır. 
* Fonksiyonlar çoğu zaman, yapmak istediğimiz işlemler için bir şablon vazifesi görür. 
* Fonksiyonları kullanarak, bir veya birkaç adımdan oluşan işlemleri tek bir isim altında toplayabiliriz. 

lambda function
"""

# user defined function

# def = definition
# daireAlan = fonksiyon ismi
# r = girdi parametresi
def daireAlan(r):
    """
        Dairenin alanını hesaplar
        Girdi = Daire Yarı Çapı
        Çıktı = Daire Alanı
    """
    pi = 3.14
    daire_alanı = pi*(r**2)
    return daire_alanı
alan = daireAlan(3)
print(alan)


def daireCevre(r, pi = 3.14):
    """
        Dairenin alanını hesaplar
        Girdi = Daire Yarı Çapı
        Çıktı = Daire Alanı
    """
    daire_cevre = 2*pi*r
    print(daire_cevre)
daireCevre(3)

katsayi = 5
def katsayiCarpimi():
    global katsayi
    print(katsayi*katsayi)
katsayiCarpimi()

def bos():
    pass

# built in functions: 
liste = [1,2,3,4]

print(len(liste))
print(str(liste))
liste2 = liste.copy()
print(liste2) 
print(max(liste))
print(min(liste))


"""
#### Lambda Fonksiyonu
İleri seviye bir fonksiyon çeşididir.
Lambda işlevi, küçük anonim bir işlevdir.
Bir lambda işlevi herhangi bir sayıda argüman alabilir, ancak yalnızca bir ifadeye sahip olabilir.
"""
# çarpma işlemi yapan normal fonksiyon
def carpma(x,y,z):
    return x*y*z
carpma(2,3,4)

# aynı işlemi lambda fonksiyon ile yapmak
fonksiyon_lambda = lambda x, y, z : x*y*z
fonksiyon_lambda(2,3,4)

# yield
"""
yield ne olduğunu anlamak için, generators  ne olduğunu anlamalısınız. 
Ve generators  anlamadan önce, yinelemeleri anlamalısınız.
"""
# yinelemeleri
# Bir liste oluşturduğunuzda, içindeki öğeleri tek tek okuyabilirsiniz. 
# Öğelerini tek tek okumak yineleme olarak adlandırılır:
mylist = [1, 2, 3] # mylist is an iterable.
for i in mylist:
    print(i)
"""
Bu yinelemeler kullanışlıdır çünkü onları istediğiniz kadar okuyabilirsiniz, 
ancak tüm değerleri bellekte saklarsınız ve çok fazla değeriniz olduğunda bu her zaman istediğiniz şey değildir.
"""
# 
"""
generators yineleyicilerdir, 
generators tüm değerleri bellekte saklamaz, değerleri anında üretirler:
"""
mygenerator = (x for x in range(1,4))
for i in mygenerator:
    print(i)
"""
[] yerine () kullanmanız dışında tamamen aynıdır. 
1'ı hesaplarlar, sonra unuturlar ve 2'i hesaplarlar ve  3'i hesaplarlar ve birer birer hesaplamayı bitirirler.
"""
 
"""
yield, işlevin bir generator döndürmesi dışında return gibi kullanılan bir anahtar sözcüktür.
"""   
def createGenerator():
    mylist = range(1,4)
    for i in mylist:
        yield i
mygenerator = createGenerator() # create a generator
print(mygenerator) # mygenerator is an object!
for i in mygenerator:
    print(i)
    
"""
Burada işe yaramaz bir örnek var 
ancak yalnızca bir kez okumanız gereken büyük bir veri kümesi döndüreceğiniz zaman kullanışlıdır.
örneğin image process de yapacağımız gibi
"""
# %% numpy 
"""
NumPy, Python programlama dili için bir kütüphane olup, büyük, çok boyutlu diziler ve matrisler için hesaplama kolaylığı sağlarken, bu dizilerde çalışmak için gerekli olan yüksek seviye ve karmaşık düzeyli matematiksel fonksiyonlarını içeren geniş bir koleksiyondur.
"""
import numpy as np

# 1*15 boyutunda bir array oluşturalım
dizi = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(dizi)

# array'in boyutuna bakalım
print(dizi.shape)

# 1*15'lik arrayi 3*5 lik bir matrise çevirelim
dizi2 = dizi.reshape(3,5)

print("Şekil: ",dizi2.shape)
print("Boyut: ", dizi2.ndim) # 2 boyutlu bir array

print("Veri Tipi: ",dizi2.dtype.name) # array içerisinde bulunan verinin tipi - tamsayı
print("Boy: ",dizi2.size) # arrayin boyu

# arrat'in tipi
print("type: ",type(dizi2))

# 2 boyutlu array oluşturalım
dizi2D = np.array([[1,2,3,4],[5,6,7,8],[9,8,7,5]])
print(dizi2D)

# sıfırlardan oluşan array oluşturalım
sifir_dizi = np.zeros((3,4))
print(sifir_dizi)

# birlerden oluşan array oluşturalım
bir_dizi = np.ones((3,4))
print(bir_dizi)

# boş bir array oluşturalım
bos_dizi = np.empty((2,3))
print(bos_dizi) # python da sıfır boş anlamına gelmektedir.
# aşağıda görüldüğü gibi sayılar sıfıra yakınsamaktadır

# arange(x,y, basamak): x'den başlar y'ye kadar (y dahil değil), basamak büyüklüğünde artarak
dizi_aralik = np.arange(10,50,5)
print(dizi_aralik)

# linspace(x, y,basamak) x ve y arasına (x ve y dahil) basamak kadar böl
dizi_bosluk = np.linspace(10,20,5)
print(dizi_bosluk)

float_array = np.float32([[1,2],[3,4]])
print(float_array)

# matematiksel işlemler için 2 tane dizi oluşturalım
a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b) # dizi toplaması
print(a-b) # dizi çıkarması
print(a**2) # dizinin kendisi ile çarpımı

# dizinin elemanlarını toplama
print(np.sum(a))

# dizinin en büyük değerini bulma
print(np.max(a))

# dizinin en küçük değerini bulma
print(np.min(a))

# dizinin ortalaması
print(np.mean(a))

# dizinin median
print(np.median(a))
# rastgele sayı üretme [0,1] arasında Sürekli üniform dağılım - 3*3 matris
rastgele_dizi = np.random.random((3,3))
print(rastgele_dizi)

dizi = np.array([1,2,3,4,5,6,7])
# dizinin 1. elamanı yani sıfırıncı index de bulunan elemanı
print(dizi[0])

# dizinin ilk 4 elemanı
print(dizi[0:4])

# dizinin tersi
print(dizi[::-1])

# matrislerde indeksleri ve dilimleri incelemek için 2 boyutlu bir matris oluşturalım
dizi2D = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(dizi2D)

# dizini 1. satır ve 1. sutunda bulunan elemanı, unutmayın saymaya sıfır ile başlıyoruz.
print(dizi2D[1,1])

# dizinin 1. sütununun tüm satıları
print(dizi2D[:,1])

# dizinin 1. satırının 1.2.3. elemanı
print(dizi2D[1,1:4])

# dizinin son satırının yani 2. satırın tüm sütunları
print(dizi2D[-1,:])

# dizinin son sütunun tüm satıları
print(dizi2D[:,-1])

dizi2D = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(dizi2D)

# vektör haline getirme
vektor = dizi2D.ravel()
print(vektor)

maksimum_sayinin_indeksi = vektor.argmax()
print(maksimum_sayinin_indeksi)
print(vektor.reshape(3,3))

# pandas 
"""
* Pandas, veri işlemesi ve analizi için Python programlama dilinde yazılmış olan bir yazılım kütüphanesidir. 
Bu kütüphane temel olarak zaman etiketli serileri ve sayısal tabloları işlemek için bir veri yapısı oluşturur ve 
bu şekilde çeşitli işlemler bu veri yapısı üzerinde gerçekleştirilebilir.
* Pandas sayesinde hızlı, güçlü, esnek vbir şekilde veri analizi ve işleme yapılabilir.
* Pandas sayesinde .csv ve .txt dosyalarını kolayca okuyabiliriz.
* Veri biliminde, veri içersinde bulunan eksik verileri bulmada, çıkarmtada Pandas kütüphanesi işimizi kolaylaştırır.
"""
# Pandas kütüphanesini içe aktaralım
import pandas as pd

# pandas veri çerçevesi oluşturmak için önce dözlük oluşturmak gerekli
dictionary = {"isim": ["ali","veli","kenan","murat","ayse","hilal"],
              "yas" : [15,16,17,33,45,66],
              "maas": [100,150,240,350,110,220]} 
veri = pd.DataFrame(dictionary)
print(veri)
# verinin ilk 5 satırına bakmak için
print(veri.head()) # veri ile ilgili ilk izlenimi elde etmek için
print(veri.columns) # verinin sütunları
print(veri.info())
print(veri.describe())
# yas sütununu alalım
print(veri["yas"])
# veriye yeni bir sütun ekleyelim
veri["sehir"] = ["Ankara","İstanbul","Konya","İzmir","Bursa","Antalya"]
print(veri)
# verinin yas sütununu başka bir yöntem ile alalım
print(veri.loc[:,"yas"])
# yas sütunu ve ilk 3 satırı al. 3. satır dahil
print(veri.loc[:3,"yas"])
# ilk 3 satırı ve yas'tan şehre kadar olan sütunları al
print(veri.loc[:3,"yas":"sehir"])
# ilk 3 satırı ve yas ve isim sütunlarını al
print(veri.loc[:3,["isim","yas"]])
# satırları tersten yazdır
print(veri.loc[::-1,:])
# yas sütununu iloc ile yazdır. yas sütun listeside 1. indekeste
print(veri.iloc[:,1])
# ilk 3 satırı ve yas ve isim sütunlarını al iloc ile
print(veri.iloc[:3,[0,1]])

# filtreleme
dictionary = {"isim": ["ali","veli","kenan","murat","ayse","hilal"],
              "yas" : [15,16,17,33,45,66],
              "sehir": ["İzmir","Ankara","Konya","Ankara","Ankara","Antalya"]} 
veri = pd.DataFrame(dictionary)
print(veri)

# ilk olarak yasa göre bir filtre oluşturalım. yas > 22
filtre1 = veri.yas > 22
filtrelenmis_veri = veri[filtre1]
print(filtrelenmis_veri)

# list comprehension
# ortalama yasi bulalım
ortalama_yas = veri.yas.mean()
# np.mean(veri.yas) yöntemini de kullanabilirdik
print(ortalama_yas)

veri["YAS_GRUBU"] = ["kucuk" if ortalama_yas > i else "buyuk" for i in veri.yas]
print(veri)
# birleştirme
sozluk1 = {"isim": ["ali","veli","kenan"],
              "yas" : [15,16,17],
              "sehir": ["İzmir","Ankara","Konya"]} 
veri1 = pd.DataFrame(sozluk1)

# veri seti 2 oluşturalım
sozluk2 = {"isim": ["murat","ayse","hilal"],
              "yas" : [33,45,66],
              "sehir": ["Ankara","Ankara","Antalya"]} 
veri2 = pd.DataFrame(sozluk2)

# dikey birleştirme axis = 0 ise dikey
veri_dikey = pd.concat([veri1,veri2],axis=0)

# yatay birleştirme axis = 1 ise dikey
veri_yatay = pd.concat([veri1,veri2],axis=1)

#  matplotlib ile görselleştirme 
"""
Veri görselleştirme, bilgi ve verilerin grafiksel temsilidir. 
* Grafikler, grafikler ve haritalar gibi görsel öğeleri kullanarak veri görselleştirme araçları, 
verilerdeki eğilimleri, aykırı değerleri ve kalıpları görmek ve anlamak için erişilebilir bir yol sağlar.
"""

import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4]
y = [4,3,2,1]
plt.figure() # figür oluştur - dış çerçeve
plt.plot(x, y, color = "red", alpha = 0.7, label = "line" ) # alpha = saydamlık
plt.scatter(x, y, color = "blue", alpha = 0.7, label = "scatter") # alpha = saydamlık
plt.title('Matplotlib')
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.xticks([0,1,2,3,4,5])
plt.show()


fig, axes = plt.subplots(2, 1, figsize=(9, 7))
fig.subplots_adjust(hspace = 0.5)

x = [1,2,3,4,5,6,7,8,9,10]
y = [10,9,8,7,6,5,4,3,2,1]

axes[0].scatter(x,y)
axes[0].set_title("sub figure 1")
axes[0].set_ylabel("sub figure x")
axes[0].set_xlabel("sub figure y")

axes[1].scatter(y,x)
axes[1].set_title("sub figure 2")
axes[1].set_ylabel("sub figure x")
axes[1].set_xlabel("sub figure y")

plt.figure()
img = np.random.random((50,50))
plt.imshow(img, cmap = "gray")
plt.axis("off")
plt.show()

# operating system (OS) module python
import os # OS module in python provides functions for interacting with the operating system

print(os.name) # Windows ise nt - linux ise posix dönecektir.

currentDir = os.getcwd()
print(currentDir) # Bu method bizlere o an içinde bulunduğumuz klasörü döndürür.

folder_name = "new_folder"
os.mkdir(folder_name)

new_folder_name = "new_folder2"
os.rename(folder_name,new_folder_name)

os.chdir(currentDir + "\\" + new_folder_name) # farklı bir klasör içerisine geçebilirsiniz.
print(os.getcwd()) 

os.chdir(currentDir)
print(os.listdir()) #  hangi klasördeyseniz onun içerisindeki dosya ve klasörleri döndürür.

files = os.listdir()
for f in files:
    if f.endswith(".py"):
        print(f)

os.rmdir(new_folder_name) # İçi boş olan bir klasörü silmek için kullanılır, az önce oluşturduğumuz yeniKlasor isimli dizini silelim.

# Verdiğiniz bir klasörün altındaki dizinleri ve dosyaları görebileceğiniz bir method.
for i in os.walk(currentDir):
    print(i)

os.path.exists("python_hatırlatma.py")











