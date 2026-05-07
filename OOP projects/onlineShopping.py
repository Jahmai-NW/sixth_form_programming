class Customer():
    def __init__(self, thePersonalDetails, theAccountBalance):
        self.personalDetails = thePersonalDetails
        self.accountBalance = theAccountBalance

    def getPersonalDetails(self):
        print(f"Here is your ID: {self.personalDetails}")

    def getAccountBalance(self):
        print(f"Here is your Bal: {self.accountBalance}")

####

class Products():
    def __init__(self, theItems, thePrices):
        self.items = theItems
        self.prices = thePrices

    def getPrice(self):
        print(f"This item costs {self.prices}")

    def getItem(self):
        print(f"This is a {self.items}")

    






####











class Purchases(Customer, Products): #Child Class
    def __init__(self, thePersonalDetails, theAccountBalance, theItems, thePrices):
        super().__init__(thePersonalDetails, theAccountBalance)
        super().__init__(theItems, thePrices)

    def finalPurchase(self):    
        getPersonalDetails()
        getItem()


    def finalInformation(self):
        requiredQuantity()
        newBalance = self.accountBalance - totalPrice
        print(f"Your new balance is now {newBalance}")

    def requiredQuantity(self, quantity):
        quantity = int(input(f"How many {self.items}s would you like to purchase?: "))
        totalPrice = quantity * self.prices
        return totalPrice



    