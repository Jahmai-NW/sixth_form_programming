class Node():
    def __init__(self, theData):
        self.data = theData
        self.left = None
        self.right = None

    def getData(self):
        return self.data

    def setLeft(self, newLeft):
        self.left = newLeft

    def getLeft(self):
        return self.left

    def setRight(self, newRight):
        self.right = newRight

    def getRight(self):
        return self.right


class tree():
    def __init__(self, theHead, theNode):

        self.head = theHead

        def preOrder(p):
            print(tree[p].getData)
            if tree[p].getLeft() != None:
                preOrder(tree[p].getLeft())
            if tree[p].getRight() != None:
                preOrder(tree[p].getRight())

        def inOrder(p):
            if tree[p].getLeft() != None:
                inOrder(tree[p].getLeft())
            print(tree[p].getData)
            if tree[p].getRight() != None:
                inOrder(tree[p].getRight())

        def postOrder(p):
            if tree[p].getLeft() != None:
                postOrder(tree[p].getLeft())
            if tree[p].getRight() != None:
                postOrder(tree[p].getRight())
            print(tree[p].getData)




        def add(self, theNode):

            #start at the head of the list
            current = self.head

        #instantiate a new node
            newData = Node(newData)

        #checking if the list is empty by seeing if current is equal to none
        if current == None:
            #if the list is empty, set the current/head of the list to the new node being instantiated
            current = newData

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


###########################################################################################################


A = Node("A")


B = Node("B")

C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")   
G = Node("G")
H = Node("H")




newTree = tree(A, B, C, D, E, F, G, H)
#fairs

