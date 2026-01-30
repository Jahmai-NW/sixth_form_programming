class Player():
    def __init__(self, thePlayerID):
        self.playerID = thePlayerID
        self.position = 0
        self.money = 2000
        self.skipTurn = False
        self.rollsThisTurn = 0
    
    def getPosition(self):
        return self.position
    
    def setPosition(self, position):
        self.position = position

    def getMoney(self):
        return self.money
    
    def setMoney(self, amount):
        self.money = amount


class Animal():
    def __init__(self, theName, theCost, 
                 theL0, theL1, theL2, theL3, 
                 theImageLink, theSetSquare, theOwned):
        self.name = theName
        self.cost = theCost
        self.L0 = theL0
        self.L1 = theL1
        self.L2 = theL2
        self.L3 = theL3
        self.imageLink = theImageLink
        self.setSquare = theSetSquare
        self.owned = theOwned
        self.currentLevel = 0

    def getCost(self):
        return self.cost

    def getCurrentLevel(self):
        return self.currentLevel
    
    def setOwned(self, player):
        self.owned = player

    def getOwned(self):
        return self.owned
    
    def getName(self):
        return self.name
    
    def upgrade(self): 
        if self.currentLevel < 3: 
            self.currentLevel += 1
        else:
            print(self.name, "is already at max level.")

    def getAmountToCharge(self):
        levels = [self.L0, self.L1, self.L2, self.L3]
        return levels[self.currentLevel]

    
class Card():
    # private textToDisplay String
    # private amount Integer

    # constructor
    def __init__(self, theTextToDisplay, theAmount):
        self.textToDisplay = theTextToDisplay
        self.amount = theAmount

    def getTextToDisplay(self):
        return self.textToDisplay
    
    def getAmount(self):
        return self.amount
    
##########
##########
##########

import random

board = [None]*26 
board[0] = Animal("START", 0, 0, 0, 0, 0, "start.bmp", 0, "free")
board[1] = Animal("mouse", 600, 5, 25, 50, 100, "mouse.bmp", 1, "free")
board[2] = Animal("rabbit", 800, 8, 40, 80, 160, "rabbit.bmp", 2, "free")
board[3] = Animal("hedgehog", 900, 9, 45, 90, 180, "hedgehog.bmp", 3, "free")
board[4] = Animal("fox", 1200, 12, 60, 120, 240, "fox.bmp", 4, "free")
board[5] = Animal("badger", 1400, 14, 70, 140, 280, "badger.bmp", 5, "free")
board[6] = Animal("squirrel", 1000, 10, 50, 100, 500, "squirrel.bmp", 6, "free")
board[7] = Animal("owl", 1600, 16, 80, 160, 320, "owl.bmp", 7, "free")
board[8] = Animal("deer", 1800, 18, 90, 180, 360, "deer.bmp", 8, "free")
board[9] = Animal("boar", 2000, 20, 100, 200, 400, "boar.bmp", 9, "free")
board[10] = Animal("wolf", 2200, 22, 110, 220, 440, "wolf.bmp", 10, "free")
board[11] = Animal("lynx", 2400, 24, 120, 240, 480, "lynx.bmp", 11, "free")
board[12] = Animal("bear", 2600, 26, 130, 260, 520, "bear.bmp", 12, "free")
board[13] = Animal("SPECIAL", 0, 0, 0, 0, 0, "special.bmp", 13, "free")
board[14] = Animal("penguin", 1800, 18, 90, 180, 360, "penguin.bmp", 14, "free")
board[15] = Animal("seal", 2000, 20, 100, 200, 400, "seal.bmp", 15, "free")
board[16] = Animal("dolphin", 2400, 24, 120, 240, 480, "dolphin.bmp", 16, "free")
board[17] = Animal("shark", 2800, 28, 140, 280, 560, "shark.bmp", 17, "free")
board[18] = Animal("tiger", 3000, 30, 150, 300, 600, "tiger.bmp", 18, "free")
board[19] = Animal("elephant", 3500, 35, 175, 350, 700, "elephant.bmp", 19, "free")
board[20] = Animal("zebra", 2800, 28, 140, 280, 560, "zebra.bmp", 20, "free")
board[21] = Animal("giraffe", 3000, 30, 150, 300, 600, "giraffe.bmp", 21, "free")
board[22] = Animal("rhino", 3200, 32, 160, 320, 640, "rhino.bmp", 22, "free")
board[23] = Animal("hippo", 3400, 34, 170, 340, 680, "hippo.bmp", 23, "free")
board[24] = Animal("lion", 3600, 36, 180, 360, 720, "lion.bmp", 24, "free")
board[25] = Animal("gorilla", 3800, 38, 190, 380, 760, "gorilla.bmp", 25, "free")

###

deck = [
    Card("WIN: You have won the zoo lottery", 1000000),
    Card("FINE: You are double parked while visiting the zoo", -200),
    Card("WIN: Your panda enclosure is a huge success", 500),
    Card("FINE: You must pay for emergency vet treatment", -400),
    Card("WIN: A famous wildlife photographer features your zoo", 300),
    Card("FINE: You forgot to lock the reptile house", -250),
    Card("WIN: School trip bookings increase profits", 350),
    Card("FINE: You must repair damaged fencing", -300),
    Card("WIN: Your zoo café has record sales", 200),
    Card("FINE: Health and safety inspection fine", -350),
    Card("WIN: A rare animal is donated to your zoo", 600),
    Card("FINE: Food supplies spoiled due to power cut", -200),
    Card("WIN: You receive a conservation grant", 500),
    Card("FINE: Animal escape causes bad publicity", -450),
    Card("WIN: Your zoo wins 'Best Family Attraction'", 400),
    Card("FINE: You must refund unhappy visitors", -150),
    Card("WIN: Sponsorship deal with wildlife charity", 700),
    Card("FINE: Extra staff wages during busy weekend", -250),
    Card("WIN: TV documentary filmed at your zoo", 800),
    Card("FINE: Unexpected enclosure maintenance", -300),
    Card("WIN: Successful breeding programme", 650),
    Card("FINE: Vet bills higher than expected", -350),
    Card("WIN: You host a sold-out night safari", 450),
    Card("FINE: Storm damage to outdoor enclosures", -500),
    Card("WIN: Gift shop profits exceed expectations", 250),
    Card("FINE: You lose income due to bad weather", -200),
    Card("WIN: Social media campaign boosts visitors", 300),
    Card("FINE: Animal food costs increase", -150),
    Card("WIN: You receive a donation from a benefactor", 1000),
    Card("FINE: You must upgrade security systems", -400),
    Card("WIN: Zoo anniversary celebration brings crowds", 550),
    Card("FINE: Cleaning costs after school holidays", -180),
    Card("WIN: New attraction opens successfully", 600),
    Card("FINE: Marketing campaign fails", -220),
    Card("WIN: Volunteers help reduce running costs", 200),
    Card("FINE: Parking fines from delivery vehicles", -120),
    Card("WIN: Endangered species funding approved", 750),
    Card("FINE: Insurance excess payment required", -300)
]
headPointer = 0

#

def viewAllAnimals(theBoard):
    for i in range(len(theBoard)): 
        print(str(i) + ": " + theBoard[i].getName())

#

def create_players():
    num = int(input("How many players? (2-4): "))
    while num < 2 or num > 4:
        print("Please enter 2, 3, or 4.")
        num = int(input("How many players? (2-4): "))
    players = [None]*num
    for i in range(num):
        players[i] = Player("P"+str(i+1))
    return players
players = create_players()

#

def pickDeck(currentPlayer):
    global headPointer
    
    print(deck[headPointer].getTextToDisplay())
    playersTotal = currentPlayer.getMoney() + deck[headPointer].getAmount()
    currentPlayer.setMoney(playersTotal)
    headPointer=headPointer+1
    if headPointer == len(deck):
        headPointer = 0

#

def checkAnimal(player):
    pos = player.getPosition()
    space = board[pos]
    if space.getOwned() == "free" and space.getCost() > 0:
        ownershipQ = input("Would you like to buy " + space.getName() + " for " + str(space.getCost()) + " ? (Y/N): ").upper()
        if ownershipQ == "Y":
            purchase(player, space)
            return
    if space.getOwned() == player:
        if space.getCurrentLevel() < 3:
            print("Type Y or N")
            upgradingQ = input("Would you like to upgrade", space.getName(), "for", space.getCost(), "?").upper()
            if upgradingQ == "Y":
                space.upgrade()
            return
        if space.getOwned() != "free":
            chargeStay(player, space)

#

def purchase(player, animal):
    balance = player.getMoney()
    costOfBuying = animal.getCost()
    if balance >= costOfBuying:
        player.setMoney(balance - costOfBuying)
        animal.setOwned(player)
        print("You now own", animal.getName())
    else: 
        print("You do not have enough money to purchase this animal.")

#

def chargeStay(player, animal):
    fine = animal.getAmountToCharge()
    player.setMoney(player.getMoney() - fine)

    owner = animal.getOwned()
    owner.setMoney(owner.getMoney() + fine)

    print(player.playerID, "paid", fine, "to", owner.playerID)

#

def playerMove(currentPlayer):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print("You rolled:", dice1, "and", dice2)
    newPos = currentPlayer.getPosition() + dice1 + dice2
    if dice1 == dice2:
        print("You rolled a double! Drawing a card...")
        pickDeck(currentPlayer)
    if newPos > 25:
        newPos -= 26
        currentPlayer.setMoney(currentPlayer.getMoney() + 500)
        print("You passed START and collected 500!")
    currentPlayer.setPosition(newPos)
    print("You're now on", board[newPos].getName())
    if newPos == 13:
        print("This is a SPECIAL tile - you miss your next turn.")
        currentPlayer.skipTurn = True
        return
    else:
        checkAnimal(currentPlayer)

#

def show_menu():
    print("\n=== Zoo Game Menu ===")
    print("1. View animals")
    print("2. Buy animal")
    print("3. Upgrade animal")
    print("4. Roll the Dice")
    print("5. End turn")
    print("6. Quit game")

#

def menu_choice(choice, currentPlayer):
    match choice:
        case "1":
            print("You chose to view animals")
            viewAllAnimals(board)
        case "2":
            print("You chose to buy an animal")
            space = board[currentPlayer.getPosition()]
            if space.getOwned() == "free":
                purchase(currentPlayer, space)
            else:
                print("You cannot buy this animal.")
        case "3":
            print("You chose to upgrade an animal")
            space = board[currentPlayer.getPosition()]
            if space.getOwned() == currentPlayer:
                if space.getCurrentLevel() < 3:
                    space.upgrade()
                    print(space.getName(), "upgraded to level", space.getCurrentLevel())
                else:
                    print("This animal is already at max level.")
            else: 
                print("You do not own this animal")

        case "4":
            print("Rolling...")
            playerMove(currentPlayer)

        case "5":
            print("Ending turn")
            return "end"

        case "6":
            print("Game quitting...")
            return "quit"

        case _:
            print("Invalid choice, try again")

    return "continue"

############
############

running = True
currentPlayerIndex = 0

while running:
    currentPlayer = players[currentPlayerIndex]

    if currentPlayer.skipTurn: 
            print(currentPlayer.playerID, "misses this turn!") 
            currentPlayer.skipTurn = False 
            currentPlayerIndex = (currentPlayerIndex + 1) % len(players) 
            continue


    print(currentPlayer.playerID + "'s turn")       
    
    show_menu()
    choice = input("Enter your choice: ")

    result = menu_choice(choice, currentPlayer)

    if result == "quit":
        running = False

    elif result == "end":
        currentPlayerIndex = (currentPlayerIndex + 1) % len(players)