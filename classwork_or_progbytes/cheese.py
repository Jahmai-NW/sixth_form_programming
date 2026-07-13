# firsttree = [
#     [1, "A", 2],
#     [3, "B", 4],
#     [5, "C", -1],
#     [-1, "D", 6],
#     [-1, "E", -1],
#     [-1, "F", -1],
#     [-1, "G", -1]
# ]



firsttree = [
    [1, "24", 2],
    [3, "D", -1],
    [4, "H", 5],
    [6, "B", 7],
    [-1, "G", -1],
    [-1, "J", 8],
    [-1, "A", -1],
    [-1, "C", -1],
    [-1, "Z", -1],
]



def inOrder(p):
    if firsttree[p][0] != -1:
        inOrder(firsttree[p][0])
    print(firsttree[p][1])
    if firsttree[p][2] != -1:
        inOrder(firsttree[p][2])


def preOrder(p):
    print(firsttree[p][1])
    if firsttree[p][0] != -1:
        preOrder(firsttree[p][0])
    if firsttree[p][2] != -1:
        preOrder(firsttree[p][2])


def postOrder(p):
    if firsttree[p][0] != -1:
        postOrder(firsttree[p][0])
    if firsttree[p][2] != -1:
        postOrder(firsttree[p][2])
    print(firsttree[p][1])



postOrder(0)

