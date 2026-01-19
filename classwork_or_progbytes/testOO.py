class Player():
    #private playerID
    #private boardPosition
    #private money

    def __init__(self, thePlayerID):
        self.playerID = thePlayerID
        self.boardPosition = 0
        self.money = 2000

    def getPlayerID(self):
        return self.playerID
    
    def getBoardPosition(self):
        return self.boardPosition
    
    def getMoney(self):
        return self.money
    
    def setPlayerID(self, playerID):
        self.playerID = playerID

    def setBoardPosition(self, boardPosition):
        self.boardPosition = boardPosition

    def setMoney(self, money):
        self.money = money
    

class Animal():
    #private name
    #private cost
    #private L0
    #private L1
    #private L2
    #rpivate L3
    #private imageLink
    #private setSquare
    #private owned

    def __init__(self, theName, theCost, theL0, theL1, theL2, theL3, theImageLink, theSetSquare, theOwned):
        self.name = theName
        self.currentLevel = 0
        self.cost = theCost
        self.L0 = theL0
        self.L1 = theL1
        self.L2 = theL2
        self.L3 = theL3
        self.imageLink = theImageLink
        self.setSquare = theSetSquare
        self.owned = theOwned

    def getName(self):
        return self.name
        
    def getCost(self):
        return self.cost
     
    def getOwned(self):
        return self.owned
    
    def setOwned(self, player):
        self.owned = player 

    def getCurrentLevel(self):
        return self.currentLevel
    
    def upgrade(self, player):
        return None
    

    
    ###!!!
    def getAmountToCharge(self):
        return None
    


class Card():
    #private textToDisplay
    #private amount
    def __init__(self, theTextToDisplay, theAmount):
        self.textToDisplay = theTextToDisplay
        self.amount = theAmount

    def getTextToDisplay(self):
        return self.textToDisplay
    
    def getAmount(self):
        return self.amount
