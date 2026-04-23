class Node():

    # constructor
    def __init__(self, theValue):
        self.value = theValue
        self.nextNode = None

    def getValue(self):
        return self.value

    def setNextNode(self, newNode):
        self.nextNode = newNode

    def getNextNode(self):
        return self.nextNode

    def setValue(self, newValue):
        self.value = newValue




# instantiate a node

node1 = Node("Bob")
node2 = Node("Tony")
node3 = Node("Ivan")
node4 = Node("Matt")
node5 = Node("Jahmai")



headpointer = node1
# print(headpointer.getValue())

headpointer.setNextNode(node2)
# print(headpointer.getNextNode().getValue())

headpointer.getNextNode().setNextNode(node3)
# print(headpointer.getNextNode().getNextNode().getValue())

headpointer.getNextNode().getNextNode().setNextNode(node4)
# print(headpointer.getNextNode().getNextNode().getNextNode().getValue())

headpointer.getNextNode().getNextNode().getNextNode().setNextNode(node5)
# print(headpointer.getNextNode().getNextNode().getNextNode().getNextNode().getValue())

print("----------------------------------")

########################################################################################################################

current = headpointer
while current != None:
    print(current.getValue())
    current = current.getNextNode()
