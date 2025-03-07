# Dosya adı
dosya_adi = "veriler.txt"

# Kullanıcıdan bir metin alıp dosyaya yazma
metin = input("Bir metin girin: ")
with open(dosya_adi, "w", encoding="utf-8") as dosya:
    dosya.write(metin + "\n")

# Dosyanın içeriğini okuma ve ekrana yazdırma
with open(dosya_adi, "r", encoding="utf-8") as dosya:
    print("\nDosyanın içeriği:")
    print(dosya.read())

# Kullanıcıdan 5 farklı satır alıp dosyaya ekleme
print("\nŞimdi 5 satırlık veri gireceksiniz:")
with open(dosya_adi, "a", encoding="utf-8") as dosya:
    for i in range(5):
        satir = input(f"{i+1}. satırı girin: ")
        dosya.write(satir + "\n")

# Dosyayı satır satır okuma ve ekrana yazdırma
print("\nDosyadaki tüm satırlar:")
with open(dosya_adi, "r", encoding="utf-8") as dosya:
    for satir in dosya:
        print(satir.strip())  # Satır sonundaki boşlukları temizler
