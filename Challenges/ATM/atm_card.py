# ATM default
class ATMcard():
    def __init__(self, default_pin, default_balance):
        self.default_pin = default_pin
        self.default_balance = default_balance

    def check_initial_pin(self):
        return self.default_pin
    
    def check_initial_balance(self):
        return self.default_balance