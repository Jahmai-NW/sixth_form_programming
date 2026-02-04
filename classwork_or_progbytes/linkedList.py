########## LINKED LIST CLASS ###########

class LinkedList():
    # constructor
    def __init__(self, headData):
        self.head = Node(headData)

    def getHead(self):
        return self.head
    
    def add(self, newData):
        return None

########## NODE CLASS #################
class Node():
    # constructor
    def __init__(self,newData):
        self.data = newData
        self.next = None

    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setNext(self, newNext):
        self.next = newNext

#######################################
# MAIN PROGRAM
#######################################

firstPerson = input("What is the first person in your list?: ")
myList = LinkedList(firstPerson)


print(myList)
print(myList.getHead())

print(myList.getHead().getData())