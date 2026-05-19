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
    def __init__(self, theName, theHP, theAttack, theSpecialMove, theRankName, theDomainExpansionName):
        self.name = theName
        self.hp = theHP
        self.attack = theAttack
        self.specialMove = theSpecialMove
        self.rct = False
        self.domainExpansionName = theDomainExpansionName
        self.domainExpansion = False
        self.simpleDomain = False
        self.rankName = theRankName
        self.rankPoints = 0

    def getName(self):
        return self.name

    def setRCT(self):
        self.rct = True

    def getTheDomainExpansionName(self):
        return self.domainExpansionName

    def setTheDomainExpansionName(self, newDomainExpansionName):
        self.domainExpansionName = newDomainExpansionName

    def setDomainExpansion(self):
        self.domainExpansion = True

    def setSimpleDomain(self):
        self.simpleDomain = True

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

    def getSpecialMove(self):
        return self.specialMove

    

class CursedSpirit():
    def __init__(self, theName, theHP, theAttack, theSpecialMove, theRankName, theDomainExpansionName):
        self.name = theName
        self.hp = theHP
        self.attack = theAttack
        self.specialMove = theSpecialMove
        self.rct = False
        self.domainExpansionName = theDomainExpansionName
        self.domainExpansion = False
        self.rankName = theRankName
        self.rankPoints = 0

    def getName(self):
        return self.name

    def setRCT(self):
        self.rct = True

    def getTheDomainExpansionName(self):
        return self.domainExpansionName

    def setTheDomainExpansionName(self, newDomainExpansionName):
        self.domainExpansionName = newDomainExpansionName
        
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


YujiItadori = Sorcerers("Yuji Itadori", 3000, 1000, "Black Flash", "Special Grade", "Benevolent Shrine")
YutaOkkotsu = Sorcerers("Yuta Okkotsu", 8000, 8000, "Summon Rika", "Special Grade", "Authentic Mutual Love")
SatoruGojo = Sorcerers("Satoru Gojo", 9500, 9500, "200% Hollow Purple", "Special Grade", "Infinite Void")
RyomenSukuna = Sorcerers("Ryomen Sukuna", 10000, 10000, "World Cutting Slash", "Special Grade", "Malevolent Shrine")
YukiTsukumo = Sorcerers("Yuki Tsukumo", 7000, 7000, "Black Hole", "Special Grade", "Star Rage")
SuguruGeto = Sorcerers("Suguru Geto", 1500, 1000, "Uzumaki", "Special Grade", "Womb Profusion")
Kenjaku = Sorcerers("Kenjaku", 1500, 6000, "Anti-Gravity", "Special Grade", "Womb Profusion")
MakiZenin = Sorcerers("Maki Zenin", 2500, 500, "Inhumane Speed", "Heavenly Restricted", None)
MegumiFushiguro = Sorcerers("Megumi Fushiguro", 1000, 9000, "Summon Mahoraga", "Grade 2", "Chimera Shadow Garden")
TojiFushiguro = Sorcerers("Toji Fushiguro", 2250, 700, "Sneak Attack", "Heavenly Restricted", None)
NaoyaZenin = Sorcerers("Naoya Zenin", 700, 500, "Enforce 24FPS", "Special Grade 1", None)
KinjiHakari = Sorcerers("Kinji Hakari", 6500, 3000, "Instantaneous Regeneration", "Grade 1", "Idle Death Gamble")
HajimeKashimo = Sorcerers("Hajime Kashimo", 7800, 7800, "Mythical Beast Amber", "Special Grade", None)


Mahito = CursedSpirit("Mahito", 6000, 4000, "Embodiment of Perfection", "Special Grade", "Self-Embodiment Of Perfection")
Jogo = CursedSpirit("Jogo", 1500, 3000, "Maximum Meteor", "Special Grade", "Coffin of the Iron Mountain")
Dagon = CursedSpirit("Dagon", 1000, 1500, "Awakening Form", "Special Grade", "Horizon of the Captivating Skandha")
Choso = CursedSpirit("Choso", 2000, 2000, "Supernova", "Grade 1", None)
Naoya = CursedSpirit("Cursed Spirit Naoya", 4000, 4000, "Apply 24FPS on Air", "Special Grade", "Time Cell Moon Palace")

TotalSorcerers = [YujiItadori, YutaOkkotsu, SatoruGojo, RyomenSukuna, YukiTsukumo, SuguruGeto, Kenjaku, MakiZenin, MegumiFushiguro, TojiFushiguro, NaoyaZenin, KinjiHakari, HajimeKashimo]
TotalSpirits = [Mahito, Jogo, Dagon, Choso, Naoya]

################################# GAMEPLAY FUNCTIONS
def moreAttack(fighter1, fighter2):
    if fighter1.getAttack() > fighter2.getAttack():
        print(fighter1.getName(), "won by using their base moves.")
    elif fighter1.getAttack() < fighter2.getAttack():
        print(fighter2.getName(), "won by using their base moves.")
    elif fighter1.getAttack() == fighter2.getAttack():
        print(fighter1.getName(), "and", fighter2.getName(), "are in a stalemate...")
    elif fighter1.getAttack() > (2*int(fighter2.getAttack())):
        print(fighter1.getName(), "won by using", fighter1.getSpecialMove())
    elif (2*int(fighter1.getAttack())) < fighter2.getAttack():
        print(fighter2.getName(), "won by using", fighter2.getSpecialMove())



def fightingAnnounce():
    from random import choice
    fighter1 = choice(TotalSorcerers)
    fighter2 = choice(TotalSorcerers)
    if fighter1.getName() != fighter2.getName():
        print(fighter1.getName(), "vs", fighter2.getName())
        moreAttack(fighter1, fighter2)


fightingAnnounce()
    



    
