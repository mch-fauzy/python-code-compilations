from atm_card import ATMcard

# Data Customer
class Customer():
    def __init__(self, atmID, cust_pin = 1234, cust_bal = 10000):
        self.atmID = atmID
        self.pin = cust_pin
        self.balance = cust_bal
    
    def checkID(self):
        return self.atmID

    def checkPin(self):
        return self.pin
    
    def checkBalance(self):
        return self.balance

    def withdrawBalance(self, nominal):
        self.balance -= nominal
    
    def depositBalance(self, nominal):
        self.balance += nominal

default_atm = ATMcard(1234, 10000)
atm = Customer('Vermillion')
print(f'Hello {atm.checkID()}')
