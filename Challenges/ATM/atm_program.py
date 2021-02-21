import random
import datetime
from customer import Customer
# Instance the class from customer.py
atm = Customer(id) # id -> python built-in function to return an identity of an object

while True:
    pin = int(input('Enter Your PIN: '))
    
    # Verifikasi Pin
    tries_chance = 0
    while pin != atm.checkPin() and tries_chance < 3:
        pin = int(input('Wrong PIN, Enter Again: '))
        tries_chance += 1

        if tries_chance == 3:
            print('Error, please re-insert Your ATM card...')
            # Exit the program
            exit()
    
    # Menu ATM
    while True:
        print('\nWelcome to ATM')
        
        print('\n1 - Check Balance\t2 - Withdraw\t3 - Deposit\t4 - Change Pin\t5 - Exit')
        select_menu = int(input('\nChoose Menu: '))
        
        # Cek Saldo
        if select_menu == 1:
            print(f'Your Balance is: IDR {atm.checkBalance()}\n')
        # Ambil Uang
        elif select_menu == 2:
            nominal = int(input('Enter your withdraw nominal: '))
            verify_withdraw = input(f'It is correct nominal? (y/n) IDR {nominal}: ')
            if verify_withdraw == 'y':
                print(f'Initial Balance is IDR {atm.checkBalance()}')
                if atm.checkBalance() - nominal < 10000:
                    print('Sorry, Your Balance cant lower than IDR 10000')
                elif nominal < atm.checkBalance():
                    atm.withdrawBalance(nominal)
                    print('Transaction Success')
                    print(f'Current Balance is IDR {atm.checkBalance()}')
                else:
                    print('Sorry, Your Balance is not enough')
            else:
                break
        # Simpan Uang
        elif select_menu == 3:
            nominal = int(input('Enter your deposit nominal: '))
            verify_deposit = input(f'It is correct nominal? (y/n) IDR {nominal}: ')
            if verify_deposit == 'y':
                atm.depositBalance(nominal)
                print(f'Current Balance is IDR {atm.checkBalance()}')
            else:
                break
        # Ganti Pin
        elif select_menu == 4:
            current_pin = int(input('Enter Your current PIN: '))
            if current_pin != atm.checkPin():
                print('Wrong PIN!')
                break
            
            new_pin = int(input('Enter Your new PIN: '))
            verify_new_pin = int(input('Enter Your new PIN again: '))
            if verify_new_pin == new_pin:
                # Ubah PIN awal ke PIN baru
                atm.pin = new_pin
                print('Success')
            else:
                print('Failed, Your new PIN is not match')
        # Cetak Receipt dan exit
        elif select_menu == 5:
            print("\nReceipt is printed automatically when you leave.\nPlease keep this receipt as proof of your transaction.")
            print(f'\nNo. Record{" ": <7}: {random.randint(100000, 1000000)}')
            print(f'Date{" ": <13}: {datetime.datetime.now()}')
            print(f'Current Balance{" ": <2}: IDR {atm.checkBalance()}')
            print('Thank you for using ATM service')
            exit()
        # Menu tidak tersedia
        else:
            print('Sorry, that menu is not available')