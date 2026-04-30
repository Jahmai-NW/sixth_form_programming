class BankAccount():
    def __init__(self, theAccountHolder, initialBalance=0):
        self.accountholder = theAccountHolder
        self.balance = initialBalance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(amount, "has been deposited.")
            print("New Balance:", self.balance)
            return True
        else:
            return False
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print("Withdrew", amount)
            print("New Balance:", self.balance)

    def check_balance(self):
        print("Account Holder:", self.accountholder)
        print("Current Balance:", self.balance)

    


class Bank():
    def __init__(self):
        # self.accounts = []
        self.bankTotal = 100000

    def subtract(self, amount):
        self.bankTotal -= amount
        return self.bankTotal
    
    # def createAccount(self, theAccountHolder, ):





def option1():
    enterName = input("Please enter your full name: ")
    Account = BankAccount(enterName, 0)
    print("Your account has been created.")
    
    
def option4():
    enterName = input("Please enter your full name: ")
    if Account.







# ###########################TESTING##############################
while True:
    print('''
    ----------------------------------------------------------------------------
                                Menu
    Please choose an option below by entering the number accordingly.
    1. Create a new account
    2. Deposit
    3. Withdraw
    4. Check Current Balance
    5. Exit
    ----------------------------------------------------------------------------''')

    choice = int(input("Enter Number Here: "))

    if choice == 1:
        option1()

    elif choice == 2:
        option2()

    elif choice == 3:
        option3()

    elif choice == 4:
        option4()

    elif choice == 5:
        exit()
    
    elif choice < 1:
        print("Invalid option")
         

    



# my_account = BankAccount("Alice", 100)
# my_account.check_balance()
# bank1 = Bank()

# my_account.withdraw(50)
# print(bank1.subtract(50))