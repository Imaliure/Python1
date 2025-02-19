class Human:
    # Yapıcı metod (instance oluşturulduğunda çalışır)
    def __init__(self, name):
        self.name = name
        print('human instance üretildi.')

    # Nesne çağrıldığında dönecek string değeri
    def __str__(self):
        return f'STR fonksiyonu değeri {self.name}'
    
    # Konuşma fonksiyonu
    def talk(self, sentence):
        print(f'{self.name}: {sentence}')
    
    # Yürüme fonksiyonu
    def walk(self):
        print(f'{self.name} is walking..')


# Nesne oluşturma
human1 = Human('Ali')

# Fonksiyonları çağırma
human1.talk("Merhaba")
human1.walk()

# Yeni nesne oluşturma
human2 = Human('Cem')
human2.talk('Selam')
human2.walk()

# Nesneyi ekrana yazdırma (__str__ metodu çalışır)
print(human1)
