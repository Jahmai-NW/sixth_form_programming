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
    def __init__(self, theAccounts):
        self.accounts = theAccounts
    
    # def createAccount(self, theAccountHolder, ):

























###########################TESTING##############################
while True:
    print('''
                                Menu:
    Please choose an option below by entering the number accordingly.
    1. Check Current Balance
    2. Deposit
    3. Withdraw
    4. Create a new account
    5. Exit''')



my_account = BankAccount("Alice", 100)
my_account.check_balance()