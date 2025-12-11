#### CLASS DEFINITIONS ####
class Dog():
    #constructor
    def __init__(self, theName, theColour):
        self._name = theName
        self._colour = theColour

    # getters
    def getName(self):
        return self._name
    
    def getColour(self):
        return self._colour
    

    # setters
    def setName(self, newName):
        self._name = newName

    def setColour(self, newColour):
        self._colour = newColour

#### MAIN PROGRAM ####

myDog1 = Dog("James", "Golden")
myDog2 = Dog("Sarah", "Brown")
myDog3 = Dog("Pablo", "Unknown")

print(myDog1.getName())
print(myDog2.getName())


print(myDog3.getColour())

# get colour of dog
# check if colour is equal to unknown
    # if true, get new colour input
    # set colour

# output colour, name of dog

dogColour = myDog3.getColour()
if dogColour == "Unknown":
    newColour = input("Pleaase enter colour of dog: ")
    myDog3.setColour(newColour)

print("Name:" + " " + myDog3.getName() + ", "+ myDog3.getColour())

