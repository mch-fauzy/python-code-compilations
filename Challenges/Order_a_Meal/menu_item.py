# Parent Class
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # Method Instance
    def info(self):
        #return self.name + ': $' + str(self.price)
        return f'{self.name}: ${self.price}'

    # Method Instance
    def get_total_price(self, count):
        total_price = self.price * count
        
        # Jika count lebih besar dari atau sama dengan 3, kalikan dengan 0.9
        if count >= 3:
            total_price *= 0.9
        
        # Bulatkan total_price ke float terdekat
        return round(total_price)