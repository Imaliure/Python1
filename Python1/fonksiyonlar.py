# 1 =================================================================
# Hesap makinesi fonksiyonu
def hesap_makinesi(a, b):
    toplam = a + b  
    fark = a - b 
    carpim = a * b 
    if b != 0:  
        bolum = a / b  
    else:
        bolum = "Tanımsız (0'a bölme hatası)" 
    
    print(f"{a} + {b} = {toplam}")
    print(f"{a} - {b} = {fark}")
    print(f"{a} * {b} = {carpim}")
    print(f"{a} / {b} = {bolum}")

# Kullanıcıdan iki sayı al
sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

hesap_makinesi(sayi1, sayi2)

# 2 =================================================================
# Palindrom Kontrolü Fonksiyonu 
def palindrom(word):
    if word == word[::-1]: 
        print(f'{word} bir palindrom kelimedir.')
    else:
        print(f'{word} bir palindrom kelimesi değildir.')

word = input('Bir kelime giriniz: ')  
palindrom(word)  


# 3 =================================================================
# Yaş Hesaplama Fonksiyonu 
def kac_yil_kaldi(yas):
    if yas >= 100:  
        print('Zaten 100 yaşına ulaştınız.')
    else:
        print(f'{100 - yas} yıl sonra 100 yaşında olacaksınız.')  

yas = int(input('Yaşınızı girin: ')) 

