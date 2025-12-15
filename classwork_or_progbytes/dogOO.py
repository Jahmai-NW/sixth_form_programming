#### CLASS DEFINITIONS ####
class Dog():
    #constructor
    def __init__(self, theName, theColour):
        self._name = theName
        self._colour = theColour
        self._age = int(input("Please enter age: "))

    # getters
    def getName(self):
        return self._name
    
    def getColour(self):
        return self._colour
    
    def getAge(self):
        return self._age
    

    

    # setters
    def setName(self, newName):
        self._name = newName

    def setColour(self, newColour):
        self._colour = newColour

    def setAge(self, newAge):
        self._age = newAge

    
    # methods
    def birthday(self):
        self._age = self._age + 1
        print("Happy Brithday!")
        print("You have reached " + str(dogName.getAge()) + " years old.")

#### MAIN PROGRAM ####

myDog1 = Dog("James", "Golden")
myDog2 = Dog("Sarah", "Brown")
myDog3 = Dog("Pablo", "Unknown")

#print(myDog1.getName())
#print(myDog2.getName())


#print(myDog3.getColour())

# get colour of dog
# check if colour is equal to unknown
    # if true, get new colour input
    # set colour

# output colour, name of dog
def dogColourCheck(myDog3):
    dogColour = myDog3.getColour()
    if dogColour == "Unknown":
        newColour = input("Pleaase enter colour of dog: ")
        myDog3.setColour(newColour)

    print("Name:" + " " + myDog3.getName() + ", "+ myDog3.getColour())

#age attribute, checks age, younger than 3, go to vet, older than 10, get a new dog

dogAge = myDog1.getAge()
dogName = myDog1.getName()
if dogAge < 3:
    print("You should take", dogName, "to the vet.")
elif dogAge > 10: 
    print("You should ditch", dogName, "and get a new dog.")
else:
    print(dogName, "should be fine.")


dogAge = myDog2.getAge()
dogName = myDog2.getName()
if dogAge < 3:
    print("You should take", dogName, "to the vet.")
elif dogAge > 10: 
    print("You should ditch", dogName, "and get a new dog.")
else:
    print(dogName, "should be fine.")


dogAge = myDog3.getAge()
dogName = myDog3.getName()
if dogAge < 3:
    print("You should take", dogName, "to the vet.")
elif dogAge > 10: 
    print("You should ditch", dogName, "and get a new dog.")
else:
    print(dogName, "should be fine.")



