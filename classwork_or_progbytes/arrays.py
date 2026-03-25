Grid = [
    ["O","x","x","x"],
    ["x","x","x","x"],
    ["x","x","x","x"],
    ["x","x","x","x"],
    ["x","x","x","x"],
    ["x","x","x","x"],
]

def printgrid():
    for i in range(len(Grid)):
        for j in range(len(Grid[i])):
            print(Grid[i][j], end=" | ")
        print()


def movement():
    row = int(input("Please enter the row you would like to move to (1-6): "))
    column = int(input("Please enter the column you would like to move to (1-4): "))
    for i in range(len(Grid)):
        for j in range(len(Grid[i])):
            if Grid[i][j] == "O":
                Grid[i][j] = "x"
                Grid[row-1][column-1] = "O"
                printgrid()
                return


def trap():
    import random 
    if Grid[random.randint(0,5)][random.randint(0,3)] == "O":
        print("You have been trapped! -5 HP")
        printgrid()
        return

printgrid()
while True:
    movement()
    trap()