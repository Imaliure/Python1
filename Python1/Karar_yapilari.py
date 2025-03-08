# 1 =======================================================================
try:
    # Kullanıcıdan bir sayı girmesini iste
    sayi = int(input("Bir sayı girin: "))

    # Sayının tek mi çift mi olduğunu kontrol et
    if sayi % 2 == 0:
        print(f"{sayi} çift bir sayıdır.")
    else:
        print(f"{sayi} tek bir sayıdır.")
except:
    print('Lütfen geçerli bir tam sayı girin.')


# 2 ===========================================================================
# Kullanıcıdan notu al
notu = int(input("Notunuzu girin: "))

# Harf notunu hesapla
if 90 <= notu <= 100:
    harf_notu = "A"
elif 80 <= notu <= 89:
    harf_notu = "B"
elif 70 <= notu <= 79:
    harf_notu = "C"
elif 60 <= notu <= 69:
    harf_notu = "D"
elif 0 <= notu <= 59:
    harf_notu = "F"
else:
    harf_notu = "Geçersiz not! Lütfen 0-100 arasında bir değer girin."

# Sonucu ekrana yazdır
print(f"Harf Notunuz: {harf_notu}")


# 3 ================================================================
try:
    # Kullanıcıdan yaş bilgisi al
    yas = int(input("Lütfen yaşınızı girin: "))

    # Negatif yaş kontrolü
    if yas < 0:
        print("Hata: Yaş negatif olamaz! Lütfen geçerli bir yaş girin.")
    else:
        # Yaş grubunu belirle
        if 0 <= yas <= 12:
            yas_grubu = "Çocuk"
        elif 13 <= yas <= 19:
            yas_grubu = "Genç"
        elif 20 <= yas <= 59:
            yas_grubu = "Yetişkin"
        else:
            yas_grubu = "Yaşlı"

        # Sonucu ekrana yazdır
        print(f"Yaş grubunuz: {yas_grubu}")

except:
    print("Lütfen geçerli bir tam sayı girin.")

