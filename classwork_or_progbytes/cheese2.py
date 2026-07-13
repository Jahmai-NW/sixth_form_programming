# Firsttree = [
#     [1, 24, 2],
#     [3, 15, 4],
#     [5, 38, 6],
#     [-1, 9, -1],
#     [-1, 17, -1],
#     [-1, 29, -1],
#     [-1, 58, -1],
# ]




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



def preOrder(p):
    print(Firsttree[p][1])
    if Firsttree[p][0] != -1:
        preOrder(Firsttree[p][0])
    if Firsttree[p][2] != -1:
        preOrder(Firsttree[p][2])

def inOrder(p):
    if Firsttree[p][0] != -1:
        inOrder(Firsttree[p][0])
    print(Firsttree[p][1])
    if Firsttree[p][2] != -1:
        inOrder(Firsttree[p][2])

def postOrder(p):
    if Firsttree[p][0] != -1:
        postOrder(Firsttree[p][0])
    if Firsttree[p][2] != -1:
        postOrder(Firsttree[p][2])
    print(Firsttree[p][1])


preOrder(0)
print()
inOrder(0)
print()
postOrder(0)