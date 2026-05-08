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
        print(f"{self.items}")

    
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
item4 = Products("Strand of All Might's Hair", 500)
item5 = Products("Domain Expansion: Malevolent Shrine", 400)
item6 = Products("Dismantle", 150)
item7 = Products("Summon Rika", 700)
item8 = Products("Domain Expansion: Womb Profusion", 425)
item9 = Products("Domain Expansion: Chimera Shadow Garden", 350)
item10 = Products("Become a Cursed Spirit", 900)

def showAllItems():
    collectionOfItems = [item1.getItem(), item2.getItem(), item3.getItem(), item4.getItem(), item5.getItem(), item6.getItem(), item7.getItem(), item8.getItem(), item9.getItem(), item10.getItem()]


while True:
    choice = int(input("Please enter the number of your required service: "))

    if choice == 1:
        name = input("Please enter your name: ")
        startingBal = int(input("Please enter your starting balance as an integer: "))
        customer1 = Customer(name, startingBal)
        print("")
        print("Your account has been created successfully.")
        print("")
        showMenu()


    if choice == 2:
        print(customer1.getAccountBalance())
        print("")
        showMenu()

    if choice == 3:
        None

    if choice == 4:
        showAllItems()
        print("")
        showMenu()

    if choice == 5:
        showAllItems()
        chosenitem = input("Which item would you like to purchase?: ")

        if chosenitem == item1.getItem():
            if item1.getPrice <= customer1.getAccountBalance:
                paymentMethod = CreditCardPayment()
                paymentMethod.processPurchase(customer1, item1.getPrice)
                print(customer1.getPersonalDetails(), "has bought", item1.getItem(), "for", item1.getPrice())
                print("Current Balance:", customer1.getAccountBalance)
            else:
                print("Not enough balance to buy", item1.getItem())
    




            # or item2.getItem() or item3.getItem() or item4.getItem() or item5.getItem() or item6.getItem() or item7.getItem() or item8.getItem() or item9.getItem() or item10.getItem(): 
            

    if choice == 6: 
        None
        
    











    