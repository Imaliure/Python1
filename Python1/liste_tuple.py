# 1 =================================================================
# Kullanıcıdan 5 adet sayı alarak bir listeye ekleme ve analiz yapma

sayilar = [] 

for i in range(5): 
    sayi = float(input(f"{i+1}. sayıyı girin: "))  
    sayilar.append(sayi)  

toplam = sum(sayilar) 
ortalama = toplam / len(sayilar) 
en_buyuk = max(sayilar) 
en_kucuk = min(sayilar) 

print(f"Liste: {sayilar}")
print(f"Toplam: {toplam}")
print(f"Ortalama: {ortalama}")
print(f"En büyük sayı: {en_buyuk}")
print(f"En küçük sayı: {en_kucuk}")

# 2 =================================================================
# Kullanıcıdan kelimeler alarak listeye ekleyip ters sıralama

kelimeler = []  
adet = int(input("Kaç kelime girmek istiyorsunuz? "))

for i in range(adet): 
    kelime = input(f"{i+1}. kelimeyi girin: ")
    kelimeler.append(kelime)  

kelimeler.reverse()
print("Ters sıralanmış liste:", kelimeler)

# 3 =================================================================
# Bir liste içindeki tekrar eden elemanları kaldırma

liste = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7] 
benzersiz_liste = list(set(liste))

print("Tekrarsız liste:", benzersiz_liste)
