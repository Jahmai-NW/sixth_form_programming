#############

#jahmai do a oop where u make a linked list into a table.
#The contents are as follows: make a feild with cursed spirit,
#Field with sorcerors. All should be specified by rank
#Have an array link to the list which stors all items
#Array in pythoin is a list so it is alr ig
#Then for the main program import rnd
#and rnd select items and spirits and sorcerors
#Make sure u assign hp and attack 
#items should have just attack

#Main program should rnd match sorceror vs cursed spirit
#both get a rnd item and fight

#display win only



class Sorcerers():
    def __init__(self, theName, theHP, theAttack, theSpecialMove, theRankName):
        self.name = theName
        self.hp = theHP
        self.attack = theAttack
        self.specialMove = theSpecialMove
        self.rct = False
        self.domainExpansion = False
        self.rankName = theRankName
        self.rankPoints = 0

    def getName(self):
        return self.name

    def setRCT(self):
        self.rct = True

    def setDomainExpansion(self):
        self.domainExpansion = True

    def getAttack(self):
        return self.attack

    def getHP(self):
        return self.hp

    def setHP(self, newHP):
        self.hp = newHP

    def getRankName(self):
        return self.rankName

    def setRankName(self, newRank):
        self.rankName = newRank

    def getRankPoints(self):
        return self.rankPoints

    def setRankPoints(self, amount):
        self.rankPoints = amount

    

class CursedSpirit():
    def __init__(self, theName, theHP, theAttack, theSpecialMove, theRankName):
        self.name = theName
        self.hp = theHP
        self.attack = theAttack
        self.specialMove = theSpecialMove
        self.rct = False
        self.domainExpansion = False
        self.rankName = theRankName
        self.rankPoints = 0

    def getName(self):
        return self.name

    def setRCT(self):
        self.rct = True

    def setDomainExpansion(self):
        self.domainExpansion = True

    def getAttack(self):
        return self.attack

    def getHP(self):
        return self.hp

    def setHP(self, newHP):
        self.hp = newHP

    def getRankName(self):
        return self.rankName

    def setRankName(self, newRank):
        self.rankName = newRank

    def getRankPoints(self):
        return self.rankPoints

    def setRankPoints(self, amount):
        self.rankPoints = amount

#max hp = 10000
#min hp = 1

#max attack = 10000
#min attack = 1


YujiItadori = Sorcerers("Yuji Itadori", 3000, 1000, "Black Flash", "Special Grade")
YutaOkkotsu = Sorcerers("Yuta Okkotsu", 8000, 8000, "Summon Rika", "Special Grade")
SatoruGojo = Sorcereres("Satoru Gojo", 9500, 9500, "200% Hollow Purple", "Special Grade")
RyomenSukuna = Sorcerers("Ryomen Sukuna", 10000, 10000, "World Cutting Slash", "Special Grade")
YukiTsukumo = Sorcerers("Yuki Tsukumo", 7000, 7000, "Black Hole", "Special Grade")
SuguruGeto = Sorcerers("Suguru Geto", 1500, 1000, "Uzumaki", "Special Grade")
Kenjaku = Sorcerers("Kenjaku", 1500, 6000, "Anti-Gravity", "Special Grade")
MakiZenin = Sorcerers("Maki Zenin", 2500, 500, "Inhumane Speed", "Heavenly Restricted")
MegumiFushiguro = Sorcerers("Megumi Fushiguro", 1000, 9000, "Summon Mahoraga", "Grade 2")

Mahito = CursedSpirit("Mahito", 6000, 4000, "Embodiment of Perfection", "Special Grade")
Jogo = CursedSpirit("Jogo", 1500, 2000, "Maximum Meteor", "Special Grade")
Dagon = 



    
