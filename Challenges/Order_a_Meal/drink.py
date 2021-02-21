# Import class MenuItem menggunakan 'from' 'import'
from menu_item import MenuItem

# Child Class
# Wariskan class MenuItem dan definisikan class Drink
# Diwariskan agar bisa memanggil method dari Parent Class
class Drink(MenuItem):
    # Definisikan method __init__ 
    def __init__(self, name, price, volume):

        # Menggunakan super() panggil __init__() dari Parent Class
        super().__init__(name, price)
        self.volume = volume
        
    # Definisikan method info (Jika nama Method sama maka akan Override Method di Parent Class)
    def info(self):
        #return self.name + ': $' + str(self.price) + ' (' + str(self.volume) + 'mL)'
        return f'{self.name}: ${self.price} ({self.volume} mL)'