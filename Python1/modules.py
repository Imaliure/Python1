import matematik as m  # matematik modülünü içe aktar
import random  # Rastgele sayı üretmek için modül
from day3 import Human  # day3 dosyasındaki Human sınıfını içe aktar

# Toplama fonksiyonunu çağır
print(m.toplama(10, 20))

# 0 ile 100 arasında rastgele bir sayı üret
print(random.randint(0, 100))

# Human sınıfından nesne oluştur
human1 = Human('Ali')
