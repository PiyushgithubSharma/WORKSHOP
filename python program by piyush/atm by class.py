class Atm:
    def __init__(self):
        print(id(self))
        self.pin = ''
        self.balance=0
        self.menu()
    def get_balance(self):
        return self.balance
    def set_balance(self,new_value):
        if type(new_value)==int:
            self.balance = new_value
        else:
            print('beta mann ja')
    def menu(self):
        user_input=input('''
        hi how can i help you
        1. press 1 for creat pin
        2. press 2 for change pin
        3. press 3 for check balance
        4. press 4 for withdraw
        5, press anything else to exit''')
        if user_input=='1':
            self.create_pin()
        elif user_input=='2':
            self.change_pin()
        elif user_input == '3':
            self.check_balance()
        elif user_input == '4':
            self.withdraw_balance()
        else:
            exit()
    def create_pin(self):
        user_pin = input('enter the pin')
        self.pin = user_pin
        user_balance = int(input('enter the balance'))
        self.balance = user_balance
        print('pin creat sucessfull')
    def change_pin(self):
        old_pin = self.pin
        if old_pin == self.pin:
            new_pin = input('enter your pin')
            self.pin = new_pin
            print('pin change sucessful')
        else:
            print('chla ja chor')
    def check_balance(self):
        user_pin = input('enteer the pin')
        if user_pin == self.pin:
            print('your balance is',self.balance)
        else:
            print('chor hai to chor')
    def withdraw_balance(self):
        user_pin = input('enter the pin :')
        if user_pin == self.pin:
            amount = int(input('enter the amount'))
            if amount<=self.balance:
                self.balance = self.balance-amount
                print('withdraw succesful balance is',self.balance)
            else:
                print('hello Mr garib')
        else:
            print('sale chor')
obj = Atm()