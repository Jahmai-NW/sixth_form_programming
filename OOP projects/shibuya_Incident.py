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
    def __init__(self, theName, theHP, theAttack, theSpecialMove, theSpecialValue, theRankName, theDomainExpansionName, theDomainValue, theSureHit):
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
        self.domainValue = theDomainValue
        self.sureHit = theSureHit
        self.specialValue = theSpecialValue

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

    def getDomainValue(self):
        return self.domainValue

    def setDomainValue(self, amount):
        self.domainValue = amount
    
    def getSureHit(self):
        return self.sureHit

    def setSureHit(self, newHit):
        self.sureHit = newHit

    def getSpecialMoveValue(self):
        return self.specialValue
    
    def getSpecialMove(self):
        return self.specialMove

    

class CursedSpirit():
    def __init__(self, theName, theHP, theAttack, theSpecialMove, theSpecialValue, theRankName, theDomainExpansionName, theDomainValue, theSureHit):
        self.name = theName
        self.hp = theHP
        self.attack = theAttack
        self.specialMove = theSpecialMove
        self.rct = False
        self.domainExpansionName = theDomainExpansionName
        self.domainExpansion = False
        self.rankName = theRankName
        self.rankPoints = 0
        self.domainValue = theDomainValue
        self.sureHit = theSureHit
        self.specialValue = theSpecialValue

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

    def getDomainValue(self):
        return self.domainValue

    def setDomainValue(self, amount):
        self.domainValue = amount

    def getSureHit(self):
        return self.sureHit

    def setSureHit(self, newHit):
        self.sureHit = newHit

    def getSpecialMoveValue(self):
        return self.specialValue

    def getSpecialMove(self):
        return self.specialMove


#max hp = 10000
#min hp = 1

#max attack = 10000
#min attack = 1

#max domainvalue = 500
#min domainvalue = 0

#max exceptions = 5500
#max specialvalue = 5000
#min domainvalue = 1

YujiItadori = Sorcerers("Yuji Itadori", 3000, 2000, "Black Flash", 3500, "Special Grade", "Benevolent Shrine", 200, "gets hit by soul dismantles.")
YutaOkkotsu = Sorcerers("Yuta Okkotsu", 8000, 8000, "Rika", 4000, "Special Grade", "Authentic Mutual Love", 400, "is hit by a technique from Yuta's sword.")
SatoruGojo = Sorcerers("Satoru Gojo", 9500, 9500, "200% Hollow Nuke", 5500, "Special Grade", "Infinite Void", 480, "is forced to bear the weight of boundless information.")
RyomenSukuna = Sorcerers("Ryomen Sukuna", 10000, 10000, "World Cutting Slash", 5500, "Special Grade", "Malevolent Shrine", 500, "is sliced and diced by endless dismantle and cleave attacks.")
YukiTsukumo = Sorcerers("Yuki Tsukumo", 7000, 7000, "Black Hole", 5000, "Special Grade", "Star Rage", 420, "is hit by the effects of infinite mass.")
SuguruGeto = Sorcerers("Suguru Geto", 1500, 1000, "Maximum Uzumaki", 2000, "Special Grade", "Womb Profusion", 20, "is hit by the onslaught of Cursed Spirits.")
Kenjaku = Sorcerers("Kenjaku", 1500, 6000, "Anti-Gravity", 3800, "Special Grade", "Womb Profusion", 490, "is immediately crushed.")
MakiZenin = Sorcerers("Maki Zenin", 2500, 500, "Inhumane Speed", 3400, "Heavenly Restricted", None, 0, "invades the domain.")
MegumiFushiguro = Sorcerers("Megumi Fushiguro", 1000, 2000, "Mahoraga", 5000, "Grade 2", "Chimera Shadow Garden", 250, "is attacked by multiple shadows.")
TojiFushiguro = Sorcerers("Toji Fushiguro", 2250, 700, "Sneak Attack", 3450, "Heavenly Restricted", None, 0, "invades the domain.")
NaoyaZenin = Sorcerers("Naoya Zenin", 700, 500, "24FPS Frame", 3950, "Special Grade 1", None, 0, "is safe.")
KinjiHakari = Sorcerers("Kinji Hakari", 6500, 3000, "Instantaneous Regeneration", 4100, "Grade 1", "Idle Death Gamble", 390, "is severely injured by Jackpot Hakari.")
HajimeKashimo = Sorcerers("Hajime Kashimo", 7800, 7800, "Mythical Beast Amber", 5000, "Special Grade", None, 0, "is safe.")
DaburaKaraba = Sorcerers("Dabura Karaba", 9500, 9500, "Killing Intent", 5000, "Special Grade", "Otherworld Between Darkness and Light: Reverse Transcendence", 500, "is hit by effects which cannot be comprehended by the human mind.")
TsurugiOkkotsu = Sorcerers("Tsurugi Okkotsu", 1000, 500, "Rika Possession", 4500, "Heavenly Restricted", None, 0, "is safe.")
YukaOkkotsu = Sorcerers("Yuka Okkotsu", 1000, 700, "Death Binding Vow: Mahoraga", 5000, "Grade 2", "Chimera Shadow Garden", 100, "is attacked by multiple shadows.")
Maru = Sorcerers("Maru", 1500, 9000, "Environment Flip", 4000, "Grade 1", None, 0, "is safe.")
Cross = Sorcerers("Cross", 1600, 9000, "Environment Flip", 4000, "Grade 1", None, 0, "is safe.")



Mahito = CursedSpirit("Mahito", 6000, 4000, "Embodiment of Perfection", 4500, "Special Grade", "Self-Embodiment Of Perfection", 450, "is forcefully morphed, as a result of Idle Transfiguration.")
Jogo = CursedSpirit("Jogo", 1500, 3000, "Maximum Meteor", 4600, "Special Grade", "Coffin of the Iron Mountain", 425, "is severely burned.")
Dagon = CursedSpirit("Dagon", 1000, 1500, "Awakening Form", 2700, "Special Grade", "Horizon of the Captivating Skandha", 400, "is attacked by sea creatures.")
Choso = CursedSpirit("Choso", 2000, 2000, "Supernova", 2500, "Grade 1", None, 0, "is safe.")
Naoya = CursedSpirit("Cursed Spirit Naoya", 4000, 4000, "24FPS Frame on Air", 3950, "Special Grade", "Time Cell Moon Palace", 470, "fails to abide by Naoya's 24FPS rule. Their cells are shredded and torn apart.")

TotalSorcerers = [YujiItadori, YutaOkkotsu, SatoruGojo, RyomenSukuna, YukiTsukumo, SuguruGeto, Kenjaku, MakiZenin, MegumiFushiguro, TojiFushiguro, NaoyaZenin, KinjiHakari, HajimeKashimo,YukaOkkotsu, TsurugiOkkotsu, DaburaKaraba, Maru, Cross]
TotalSpirits = [Mahito, Jogo, Dagon, Choso, Naoya]

################################# GAMEPLAY FUNCTIONS #############################################################################################################

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



def fightingAnnounceSor():
    from random import choice
    fighter1 = choice(TotalSorcerers)
    fighter2 = choice(TotalSorcerers)
    if fighter1.getName() != fighter2.getName():
        print("")
        print(fighter1.getName(), "vs", fighter2.getName())
        moreAttack(fighter1, fighter2)
        print("")


def fightingAnnounceCur():
    from random import choice
    fighter1 = choice(TotalSpirits)
    fighter2 = choice(TotalSpirits)
    if fighter1.getName() != fighter2.getName():
        print("")
        print(fighter1.getName(), "vs", fighter2.getName())
        moreAttack(fighter1, fighter2)
        print("")


def fightingAnnounceBoth():
    from random import choice
    fighter1 = choice(TotalSorcerers)
    fighter2 = choice(TotalSpirits)
    if fighter1.getName() != fighter2.getName():
        print("")
        print(fighter1.getName(), "vs", fighter2.getName())
        moreAttack(fighter1, fighter2)
        print("")

def domainClash():
    from random import choice
    fighter1 = choice(TotalSorcerers)
    fighter2 = choice(TotalSpirits)
    if fighter1.getName() != fighter2.getName():
        print("")
        print(fighter1.getName(), "expands", fighter1.getTheDomainExpansionName(), "and", fighter2.getName(), "expands", fighter2.getTheDomainExpansionName())
        print("")

        if fighter1.getDomainValue() > fighter2.getDomainValue():
            print(fighter1.getTheDomainExpansionName(), "is more refined and wins the clash.", fighter2.getName(), fighter1.getSureHit())

        elif fighter1.getDomainValue() < fighter2.getDomainValue():
            print(fighter2.getTheDomainExpansionName(), "is more refined and wins the clash.", fighter1.getName(), fighter2.getSureHit())

        elif fighter1.getDomainValue() == 0 and fighter2.getDomainValue() == 0:
            if fighter1.getAttack() > fighter2.getAttack():
                print(fighter1.getName(), "wins in hand to hand combat")
            elif fighter1.getAttack() < fighter2.getAttack():
                print(fighter2.getName(), "wins in hand to hand combat")
            elif fighter1.getAttack() == fighter2.getAttack():
                print("A brutal stalemate has occured.")

        elif fighter1.getDomainValue() == fighter2.getDomainValue():
            print(fighter1.getTheDomainExpansionName(), "and", fighter2.getTheDomainExpansionName(), "are equal in refinement. The clash is equal.")

def deathmatchSor():
    from random import choice
    fighter1 = choice(TotalSorcerers)
    fighter2 = choice(TotalSorcerers)
    if fighter1.getName() != fighter2.getName():
        print("")
        print(fighter1.getName(), "vs", fighter2.getName())
        print("They both waste no time and using their strongest moves to avoid death.")
        print("")
        if fighter1.getSpecialMoveValue() > fighter2.getSpecialMoveValue():
            print(fighter1.getName(), "won by using", fighter1.getSpecialMove())
        elif fighter1.getSpecialMoveValue() < fighter2.getSpecialMoveValue():
            print(fighter2.getName(), "won by using", fighter2.getSpecialMove())
        elif fighter1.getSpecialMoveValue() == fighter2.getSpecialMoveValue():
            print(fighter1.getName(), "and", fighter2.getName(), "are in a stalemate...")


def deathmatchCur():
    from random import choice
    fighter1 = choice(TotalSpirits)
    fighter2 = choice(TotalSpirits)
    if fighter1.getName() != fighter2.getName():
        print("")
        print(fighter1.getName(), "vs", fighter2.getName())
        print("They both waste no time and using their strongest moves to avoid death.")
        print("")
        if fighter1.getSpecialMoveValue() > fighter2.getSpecialMoveValue():
            print(fighter1.getName(), "won by using", fighter1.getSpecialMove())
        elif fighter1.getSpecialMoveValue() < fighter2.getSpecialMoveValue():
            print(fighter2.getName(), "won by using", fighter2.getSpecialMove())
        elif fighter1.getSpecialMoveValue() == fighter2.getSpecialMoveValue():
            print(fighter1.getName(), "and", fighter2.getName(), "are in a stalemate...")


def deathmatchBoth():
    from random import choice
    fighter1 = choice(TotalSorcerers)
    fighter2 = choice(TotalSpirits)
    if fighter1.getName() != fighter2.getName():
        print("")
        print(fighter1.getName(), "vs", fighter2.getName())
        print("They both waste no time and using their strongest moves to avoid death.")
        print("")
        if fighter1.getSpecialMoveValue() > fighter2.getSpecialMoveValue():
            print(fighter1.getName(), "won by using", fighter1.getSpecialMove())
        elif fighter1.getSpecialMoveValue() < fighter2.getSpecialMoveValue():
            print(fighter2.getName(), "won by using", fighter2.getSpecialMove())
        elif fighter1.getSpecialMoveValue() == fighter2.getSpecialMoveValue():
            print(fighter1.getName(), "and", fighter2.getName(), "are in a stalemate...")


def informationDisSor():
    for i in range(len(TotalSorcerers)):
        print(TotalSorcerers[i].name)
        print(" - HP:", TotalSorcerers[i].hp)
        print(" - ATT:", TotalSorcerers[i].attack)

def informationDisCur():
    for i in range(len(TotalSpirits)):
        print(TotalSpirits[i].name)
        print(" - HP:", TotalSpirits[i].hp)
        print(" - ATT:", TotalSpirits[i].attack)








###############################################################################################################################################################


running = True
while running:
    print('''
            type -1 to quit.
        1. Practice Duel: Sorcerer vs Sorcerer
        2. Practice Duel: Cursed Spirit vs Cursed Spirit
        3. Practice Duel: Sorcerer vs Cursed Spirit
        4. Deathmatch: Sorcerer vs Sorcerer
        5. Deathmatch: Cursed Spirit vs Cursed Spirit
        6. Deathmatch: Sorcerer vs Cursed Spirit
        7. Domain Clash between Sorcerers and Cursed Spirits
        8. Display Information on Sorcerers
        9. Display Information on Cursed Spirits
          
    ''')

    option = int(input("Please enter your choice: "))

    if option == 1:
        fightingAnnounceSor()

    if option == 2:
        fightingAnnounceCur()

    if option == 3:
        fightingAnnounceBoth()

    if option == 4:
        deathmatchSor()

    if option == 5:
        deathmatchCur()

    if option == 6:
        deathmatchBoth()

    if option == 7:
        domainClash()

    if option == 8:
        informationDisSor()

    if option == 9:
        informationDisCur()

    if option == -1:
        running = False