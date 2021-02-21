from food import Food
from drink import Drink

# Instance Makanan
food1 = Food('Roti Lapis', 5, 330)
food2 = Food('Kue Coklat', 4, 450)
food3 = Food('Kue Sus', 2, 180)

# Simpan Instance Makanan ke dalam List
foods = [food1, food2, food3]

# Instance Minuman
drink1 = Drink('Kopi', 3, 180)
drink2 = Drink('Jus Jeruk', 2, 350)
drink3 = Drink('Espresso', 3, 30)

# Simpan Instance Minuman ke dalam List
drinks = [drink1, drink2, drink3]

# Menu Makanan
print('Makanan:')
index = 0
for food in foods:
    print(str(index) + '. ' + food.info())
    index += 1

#Menu Minuman
print('\nMinuman:')
index = 0
for drink in drinks:
    print(str(index) + '. ' + drink.info())
    index += 1

print('--------------------\n')

food_order = int(input('Masukkan nomor makanan: '))
selected_food = foods[food_order]

drink_order = int(input('Masukkan nomor minuman: '))
selected_drink = drinks[drink_order]

# Ambil input dari console dan tetapkan ke variable count_food dan count_drink
count_food = int(input('Mau berapa paket makanan? (Diskon 10% untuk 3 atau lebih): '))
count_drink = int(input('Mau berapa paket minuman? (Diskon 10% untuk 3 atau lebih): '))

# Panggil method get_total_price dari selected_food dan selected_drink
# get_total_price() merupakan method instance dari Parent Class MenuItem
result = selected_food.get_total_price(count_food) + selected_drink.get_total_price(count_drink)

# Cetak Total Harga
print(f'\nTotal harga adalah ${result}')