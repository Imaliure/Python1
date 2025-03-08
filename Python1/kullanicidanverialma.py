# Kullanıcıdan veri alma
ad=input('Lutfen adinizi giriniz:')
yas=input('Lutfen yasinizi giriniz:')
dogum_yili=input('Lutfen dogum yilinizi giriniz:')

# Sonucu ekrana yazdırma
print(f'Merhaba {ad}! {yas} yaşındasın ve {dogum_yili} yılında doğmuşsun.')


# Kullanıcıdan iki sayı alma
sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

# İşlemleri gerçekleştirme
toplam = sayi1 + sayi2
fark = sayi1 - sayi2
carpim = sayi1 * sayi2
bolum = sayi1 / sayi2 if sayi2 != 0 else "Tanımsız"  # Sıfıra bölme kontrolü

# Sonuçları ekrana yazdırma
print(f"Toplam: {toplam}")
print(f"Fark: {fark}")
print(f"Çarpım: {carpim}")
print(f"Bölüm: {bolum}")