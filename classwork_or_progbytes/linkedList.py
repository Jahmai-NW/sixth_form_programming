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
        
            while current != None:
                print(current.getData()) # output the data
                current = current.getNext()  # reset current to next item
        # start at the head/start pointer 

    def insert_at_front(self, data):

        # Create a new node
        new_node = Node(data)

        # Check if the head node exists
        if self.head is None:
            self.head = new_node
        else:
            # Update the pointers so the new node is the head
            new_node.set_next(self.head)            
            self.head = new_node

    
    def insert_in_order(self, data):
        """Insert a node into the correct position in an ordered list"""

        # Create a new node
        new_node = Node(data)

        # Start at the head of the list
        current = self.head
        
        # Check if there are no nodes in the list
        if current == None:
            self.head = new_node

        # Check if the new node data is before the head data
        elif new_node.get_data() < current.get_data():
            # Set the new node as the head of the list
            new_node.set_next(self.head)
            self.head = new_node

        # Otherwise find where the new node should be positioned
        else:
            # Repeat until the point of insertion is found
            while (current.get_next() != None and current.get_next().get_data() < new_node.get_data()):
                # Get the next node
                current = current.get_next()

            # Update the pointers of the new and current nodes
            new_node.set_next(current.get_next())
            current.set_next(new_node)



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