print('Kodlamaio')  # Ekrana yazdırma işlemi

baslik = 'Tasit Kredisi'  # String (metinsel) değişken
print(baslik)

baslik = 'Ihtiyac Kredisi'  # Değişkenin değerini değiştirme
print(baslik)

# Sayısal veri tipleri
vade = 36  # Tam sayı (integer)
ekVade = 6
vade2 = '36'  # String (metin) veri tipi

# Ondalıklı sayı (float)
aylikOdeme = 200.50

# Boolean (True veya False)
yukselisteMi = True  

# Matematiksel operatörler
print(5 + 5)  # Toplama
print(vade + 12)
print(vade + ekVade)

print(5 - 5)  # Çıkarma
print(vade - 12)
print(vade - ekVade)

print(5 * 5)  # Çarpma
print(vade * 12)
print(vade * ekVade)

print(5 / 5)  # Bölme
print(vade / 12)
print(vade / ekVade)

# Yeni vade hesaplama
yeniVade = vade / 2
fiyat = 100  
indirimliFiyat = fiyat - 20  # İndirim uygulanmış fiyat

print(yeniVade)
print(indirimliFiyat)

# Modülüs (%) operatörü (bölümden kalanı bulur)
print(10 % 2)  
print(vade % 3)
print(vade % ekVade)

# Mantıksal operatörler (Karşılaştırma)
print(1 == 1)  # Eşit mi?
print(1 == 2)

print(1 > 2)  # Büyük mü?
print(3 > 1)

print(1 < 2)  # Küçük mü?
print(1 < 1)

print(1 != 1)  # Eşit değil mi?
print(1 != 2)

# Mantıksal bağlaçlar (or, and)
print(1 > 2 or 5 > 2)  # En az biri doğruysa True döner
print(1 > 2 and 5 > 2)  # Her ikisi de doğru olmalı
print(1 > 2 or 5 > 2 and 3 > 2)  # Öncelik 'and' operatöründedir

# Karar yapıları (if-else)
sayi1 = 10
sayi2 = 15

if sayi1 > sayi2:
    print(f'{sayi1}, {sayi2} den büyüktür')
else:
    print(f'{sayi2}, {sayi1} den büyüktür')
