class Customer():
    def __init__(self, thePersonalDetails, theAccountBalance):
        self.personalDetails = thePersonalDetails
        self.__accountBalance = theAccountBalance

    def getPersonalDetails(self):
        print(f"Here is your ID: {self.personalDetails}")

    def getAccountBalance(self):
        print(f"Here is your current balance: {self.__accountBalance}")

    def updateBalance(self, amount):
        if self.__accountBalance + amount < 0:
            print("Insufficient funds.")
        else:
            self.__accountBalance += amount

####

class Products():
    def __init__(self, theItems, thePrices):
        self.items = theItems
        self.prices = thePrices

    def getPrice(self):
        print(f"This item costs {self.prices}")

    def getItem(self):
        print(f"This is a {self.items}")

    
def showMenu():
    print('''                                           MENU
    --------------------------------------------------------------------------------------------------------
                                    1. Create an account
                                    2. Check balance
                                    3. Update balance
                                    4. View available items
                                    5. Make a purchase
                                    6. Exit the store
    ''')




from abc import ABC, abstractmethod

class Purchase(ABC):
    @abstractmethod
    def processPurchase(self, customer, amount):
        pass

class CreditCardPayment(Purchase):
    def processPurchase(self, customer, amount):
        print(f"Processing credit card payment of £{amount} for {customer.personalDetails}")
        customer.updateBalance(-amount)






#######################################################################
showMenu()
item1 = Products("Inverted Spear of Heaven", 100)
item2 = Products("Hollow Purple", 200)
item3 = Products("Domain Expansion: Infinite Void", 450)


while True:
    choice = int(input("Please enter the number of your required service: "))

    if choice == 1:
        name = input("Please enter your name: ")
        startingBal = int(input("Please enter your starting balance as an integer: "))
        customer = Customer(name, startingBal)
        print("")
        print("Your account has been created successfully.")
        print("")
        showMenu()


    if choice == 2:
        print(customer.getAccountBalance())
        print("")
        showMenu()

    if choice == 3:
        None

    if choice == 4:
        None

    if choice == 5:
        None

    if choice == 6: 
        None
        
    











    