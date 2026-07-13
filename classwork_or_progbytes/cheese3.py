Firsttree = [
    [1, "F", 2],
    [3, "D", -1],
    [4, "H", 5],
    [6, "B", 7],
    [-1, "G", -1],
    [-1, "J", 8],
    [-1, "A", -1],
    [-1, "C", -1],
    [-1, "Z", -1],
]

class Node():
    def __init__(self, left, data, right):
        self.left = left
        self.right = right
        self.data = data

        def getData(self):
            return self.data

        def getLeft(self):
            return self.left

        def getRight(self):
            return self.right

class LinkedList():
    def __init__(self):

        def preOrder(p):
            print(Firsttree[p].getData())
            if Firsttree[p].getLeft() != -1:
                preOrder(Firsttree[p].getLeft())
            if Firsttree[p].getRight() != -1:
                preOrder(Firsttree[p].getRight())

