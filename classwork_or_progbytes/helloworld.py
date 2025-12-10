carPark = [
    ["baka", " ", " ", " ", " ", " ",],
    [" ", " ", " ", " ", " ", " ",],
    [" ", " ", " ", " ", " ", " ",],
    [" ", " ", " ", " ", " ", " ",],
    [" ", " ", " ", " ", " ", " ",],
    [" ", " ", " ", " ", " ", " ",],
    [" ", " ", " ", " ", " ", " ",],
    [" ", " ", " ", " ", " ", " ",],
    [" ", " ", " ", " ", " ", " ",],
    [" ", " ", " ", " ", " ", " ",],
]



def emptyCarPark(carPark):
    for i in range(len(carPark)):
        for j in range(len(carPark[i])):
            carPark[i][j] = " " 

    print("All spaces have been reset.")
    print(" ")
    menu()


def parkACar(carPark):
    Empty = False
    while Empty == False:
        rowInput = int(input("Please enter your desired row: "))
        columnInput = int(input("Please enter your desired column: "))

        if (carPark)[rowInput - 1][columnInput - 1] != " ":
            rowInput = int(input("Please enter your desired row: "))
            columnInput = int(input("Please enter your desired column: "))
            Empty == False

        else:
            Empty = True
            carReg = input("Please enter your car's registration number: ")
            carPark[rowInput - 1][columnInput - 1] = carReg 
            carPark.insert(rowInput-1, columnInput-1)
            print(carPark)
        break
    menu()
         
     



######## MAIN PROGRAM



#DISPLAY MENU OF OPTIONS
def menu():
    while True: 
        print("Please see Menu below: \n")
        print("1. Reset all spaces in the car park to 'empty' ")
        print("2. Park a car ")
        print("3. Remove a car ")
        print("4. Display the car ")
        print("5. Quit\n")

        print(carPark)

        option = input("Enter your choice: ")

##### accept choice

        while option != "5":

            if option == "1":
                emptyCarPark(carPark)

            if option == "2":
                parkACar(carPark)

menu()
    



























