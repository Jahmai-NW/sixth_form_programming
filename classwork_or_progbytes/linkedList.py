########## LINKED LIST CLASS ###########

class LinkedList():
    # constructor
    def __init__(self, headData):
        self.head = Node(headData)

    def getHead(self):
        return self.head
    
    def add(self, newData):

        #start at the head of the list
        current = self.head

        #instantiate a new node
        newNode = Node(newData)

        #checking if the list is empty by seeing if current is equal to none
        if current == None:
            #if the list is empty, set the current/head of the list to the new node being instantiated
            current = newNode

        #checks if the current node's data has a greater value than the new node's data
        elif newNode.getData() < current.getData():
            #if so, the node after new node is now set to current,
            newNode.setNext(current)
            #the head of the list is now the new node
            self.head = newNode

        #checks if the new node's data has a greater value than the current node's data
        elif newNode.getData() > current.getData():
            #as long as the node after current is not equal to none
            while current.getNext() != None:
                #checks if the node after current's data has less value than the new node's data
                if current.getNext().getData() < newNode.getData():
                    #sets current to the node after the current node being looked at
                    current = current.getNext()
            
            #sets the next node after new node to the node that WAS after current
            newNode.setNext(current.getNext())
            #sets the node after current to the new node
            current.setNext(newNode)
                    

    def delete(self, newData):
        current = self.head

        if current == None:
            print("This list is empty")
        
        elif current.getData() == newData.getData():
            current.getNext() == newData.getNext()
            newData.getNext = None



        
    def traverseList(self):
        current = self.head

        # check if list is empty
        if current == None:
            print("List is empty")

            while current != None:
                print(current.getData()) # output the data
                current = current.getNext()
                
                                                # reset current to next item
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
##firstPerson = input("What is the first person in your list?: ")

# instantiated a linked list with first person setup
#myList = LinkedList()



#newNode = Node("Chris")
#myList.add(firstPerson)

#myList.traverseList()

# while True:
#     person = input("What is the first person in your list?: ")
#     newNode = Node(person)
#     myList.add(person)
#     print(newNode.getData())

#     print(newNode.getNext().getData())

firstPerson = input("What is the first person in your list?: ")
myList = LinkedList(firstPerson)
myList.add("Baka")
myList.add("Jerry")
myList.add("Joseph")
print(myList.traverseList())


# print(myList)
# print(myList.getHead())

# print(myList.getHead().getData())