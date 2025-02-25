def asal_mi(sayi):
    if sayi < 2:
        return f"{sayi} bir asal sayı değildir."
    
    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            return f"{sayi} bir asal sayı değildir."
    
    return f"{sayi} bir asal sayıdır."

print(asal_mi(7))   # Çıktı: 7 bir asal sayıdır.
print(asal_mi(10))  # Çıktı: 10 bir asal sayı değildir.
print(asal_mi(193)) # Çıktı: 193 bir asal sayıdır.
