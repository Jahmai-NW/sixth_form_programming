class LinkedList():
    def __init__(self,headData):
        self.head = Node(headData)

    def getHead(self):
        return self.head
    
    def add(self, newData):
        return None
    


class Node():
    def __init__(self, theData):
        self.data = theData
        self.next = None

#####getters
    def getData(self):
        return self.data
    
    def setData(self, data):
        self.data = data
    
    def getNext(self):
        return self.next
    
    def setNext(self, next):
        self.next = next
        

################# MAIN PROGRAM #########################

firstPerson = input("Who is the first person in your list?: ")
myList = LinkedList(firstPerson)

print(myList)
print(myList.getHead())

print(myList.getHead().getData())