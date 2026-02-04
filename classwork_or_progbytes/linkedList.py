########## LINKED LIST CLASS ###########

class LinkedList():
    # constructor
    def __init__(self, headData):
        self.head = Node(headData)

    def getHead(self):
        return self.head
    
    def add(self, newData):
        return None
    
    def traverseList(self):
        current = self.head

        # check if list is empty
        if current == None:
            print("List is empty")
        else:
            print(current.getData())
        
            while current.getNext() != None:
                current = current.getNext()
                print(current.getData())
        # start at the head/start pointer



        # output item  
        # go to next pointer
        # output item 
        # repeat until we get to the end
        # 
    
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

# create a variable to hold the name of first person to put in list
firstPerson = input("What is the first person in your list?: ")

# instantiated a linked list with first person setup
myList = LinkedList(firstPerson)



newNode = Node("Chris")
myList.getHead().setNext(newNode)

myList.traverseList()



# print(myList)
# print(myList.getHead())

# print(myList.getHead().getData())