# Import class MenuItem menggunakan 'from' 'import'
from menu_item import MenuItem

# Child Class
# Wariskan class MenuItem dan definisikan class Food
# Diwariskan agar bisa memanggil method dari Parent Class
class Food(MenuItem):
    # Definisikan method __init__ 
    def __init__(self, name, price, calorie_count):

        # Menggunakan super() panggil __init__() dari Parent Class
        super().__init__(name, price)
        self.calorie_count = calorie_count
        
    # Definisikan method info (Jika nama Method sama maka akan Override Method di Parent Class)
    def info(self):
        #return self.name + ': $' + str(self.price) + ' (' + str(self.calorie_count) + 'kkal)'
        return f'{self.name}: ${self.price} ({self.calorie_count} kkal)'
    
    # Definisikan method calorie_info 
    def calorie_info(self):
        print(f'kkal: {self.calorie_count}')