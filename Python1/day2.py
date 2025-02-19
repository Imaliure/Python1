faiz = 1.59  # Ondalıklı sayı (float)
vade = 36  # Tam sayı (int)
krediAdi = 'Ihtiyac Kredisi'  # Metin (string)

print(vade + 12)  # Toplama işlemi

# Veri tiplerini kontrol etme
print(type(faiz))  
print(type(vade))  
print(type(krediAdi))  

print(int(vade) + 12)  # String'i integer'a çevirme
print(str(faiz))  # Float'ı string'e çevirme

# Kullanıcıdan giriş alma
vade = input('Lütfen istediğiniz vade sayısını giriniz:')  
print(int(vade) + 12)  

# String interpolation
print(f'Seçtiğiniz vade sonucu ortaya çıkan vade: {vade}')  

# Liste tanımlama
krediler = ['İhtiyaç Kredisi', 'Taşıt Kredisi', 'Konut Kredisi']  
print(krediler[1])  # Belirtilen index'teki elemanı yazdırma
print(len(krediler))  # Listenin uzunluğu

dizi = ['İhtiyaç Kredisi', 10, 5.2, True]  # Farklı veri tiplerini içeren liste
print(dizi)

krediler.append('Özel Kredi')  # Listeye eleman ekleme
krediler.pop()  # Son elemanı silme
krediler.remove('Taşıt Kredisi')  # Belirtilen elemanı silme
krediler.extend(['Y Kredisi', 'Z Kredisi'])  # Listeye birden fazla eleman ekleme
print(krediler)

# Döngüler
for i in range(10):  # 0'dan 9'a kadar döngü
    print(i)

for i in range(5, 10):  # 5 ile 9 arasında döngü
    print(i)

for i in range(0, 51, 10):  # 0'dan 50'ye kadar 10'ar artan döngü
    print(i)

for kredi in krediler:  # Liste elemanlarını yazdırma
    print(kredi)

for i in range(len(krediler)):  # Listeyi index ile dolaşma
    print(krediler[i])

i = 0
while i < 10:  # While döngüsü ile 10 kez 'x' yazdırma
    print('x')
    i += 1

while True:  # Sonsuz döngü (break ile durduruluyor)
    print('X')
    break

# While döngüsü ve break kullanımı
i = 0
while i < len(krediler):
    print(krediler[i])
    i += 1
    if krediler[i] == 'Konut Kredisi':
        break

# Fonksiyonlar
def hesapla():  
    print(100 - 20)  # Sabit hesaplama

hesapla()  

def calculateWithParams(fiyat, indirim):  
    print(fiyat - indirim)  # Parametre ile hesaplama

calculateWithParams(100, 30)  

def sayHello(name):  
    print(f'Merhaba {name}')  # Parametre alan fonksiyon

sayHello('Ali')  

def calculateAndReturn(price, discount):  
    return price - discount  # Geriye değer döndüren fonksiyon

yeniFiyat = calculateAndReturn(200, 50)  
print(yeniFiyat)  # Yeni fiyatı yazdırma
