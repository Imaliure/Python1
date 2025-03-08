# 1 =================================================================
# 1'den 100'e kadar olan sayıların yazdırılması
for i in range(101):
    print(i)

# 2 =================================================================
# 1'den 100'e kadar olan çift sayıların yazdırılması
for i in range(101): 
    if i % 2 == 0: 
        print(i)

# 3 =================================================================
# Kullanıcıdan bir sayı alıp faktöriyelini hesaplayan program
sayi = int(input('Bir sayı giriniz: ')) 
fact = 1  
for i in range(1, sayi + 1): 
    fact *= i  

print(f'{sayi} sayısının faktöriyeli: {fact}') 


# 4 =================================================================
# 1'den 100'e kadar olan asal sayıları bulan program

# Asal sayı kontrolü yapan fonksiyon
def asal_mi(n):
    if n < 2: 
        return False
    
    for i in range(2, int(n ** 0.5) + 1): 
        if n % i == 0: 
            return False
        
    return True 

# 1'den 100'e kadar olan asal sayıları ekrana yazdır
for i in range(1, 101):
    if asal_mi(i):  
        print(i)
