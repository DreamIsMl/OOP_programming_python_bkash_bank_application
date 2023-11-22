class Bkash:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.run_menu()

    def run_menu(self):
        while True:
            self.menu()
            user_input = input("Do you want to continue? (y/n): ").lower()
            if user_input != 'y':
                print('Goodbye!')
                break

    def menu(self):
        user_input = input('''
                           Hello! How would you like to proceed?
                           1. Enter 1 to create pin
                           2. Enter 2 for Cash In
                           3. Enter 3 for Cash Out
                           4. Enter 4 for check Balance
                           5. Enter 5 for exit
''')

        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.deposit()
        elif user_input == '3':
            self.cash_out()
        elif user_input == '4':
            self.check_balance()
        elif user_input == '5':
            print('Exiting...')


    def create_pin(self):
        self.pin = int(input('Enter pin to set'))
        print('Pin set Successfully')

    def deposit(self):
        temp = int(input("Enter Your Pin"))
        if temp == self.pin:
            amount = int(input('Enter amount that you want to deposit'))
            self.balance += amount
            print('Deposit Successfully')
        else:
            print("Wrong Pin number")

    def cash_out(self):
        temp = int(input("Enter Your Pin"))
        if temp == self.pin:
            amount = int(input("Enter amount to Cash out"))
            if amount <= self.balance:
                self.balance -= amount
                print("Cash out successfully")
            else:
                print("Insufficient funds")
        else:
            print("Wrong Pin number")

    def check_balance(self):
        temp = int(input("Enter Your Pin"))
        if temp == self.pin:
            print('Your balance is', self.balance)
        else:
            print('Wrong Pin Number')

# Example usage
bkash_account = Bkash()
