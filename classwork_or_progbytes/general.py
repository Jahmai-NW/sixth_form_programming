carPark = [ 
    ["empty", "iamhim", "empty", "empty", "empty", "empty"],
    ["empty", "empty", "empty", "empty", "empty", "empty"],
    ["empty", "empty", "empty", "empty", "empty", "empty"],
    ["empty", "empty", "empty", "empty", "empty", "empty"],
    ["empty", "empty", "empty", "empty", "empty", "empty"],
    ["empty", "empty", "empty", "empty", "empty", "empty"],
    ["empty", "empty", "empty", "empty", "empty", "empty"],
    ["empty", "empty", "empty", "empty", "empty", "empty"],
    ["empty", "empty", "empty", "empty", "empty", "empty"],
    ["empty", "empty", "empty", "empty", "empty", "empty"]
] # initialising car park layout

def menuPanel():
    print('''
    Welcome to Heathrow Airport Car Park! Please select an option:
    1. Park a car
    2. Remove a car
    3. View parked cars
    4. Find a car
    5. Exit
    ''') # menu panel prints options for the user

def parkCar():
    registeration = input("Please enter your car's registeration: ") #asks for input
    row = int(input("Please enter the row you would like to park your car in (1-10): ")) #ask for integer input
    column = int(input("Please enter the column you would like to park your car in (1-6): ")) #ask for integer input

    if row < 1 or row > 10: #if the row  input is out of range
        print("Invalid input, please try again.") #prints statement
        row = int(input("Please enter the row you would like to park your car in (1-10): ")) #ask for integer input
        column = int(input("Please enter the column you would like to park your car in (1-6): ")) #ask for integer input
        

    if column < 1 or column > 6: #if the column input is out of range
        print("Invalid input, please try again.") #prints statement
        row = int(input("Please enter the row you would like to park your car in (1-10): ")) #ask for integer input
        column = int(input("Please enter the column you would like to park your car in (1-6): ")) #ask for integer input

    if carPark[row-1][column-1] == "empty": #check if the parking spot is empty
        carPark[row-1][column-1] = registeration #parks the car, takes 1 away from row and column to return to the 0 index
        print("You have reserved your spot, thank you.") #prints a statement
        for i in range(len(carPark)): #for every value of i in the range of carPark (each row)
            for j in range(len(carPark[i])): #for every value of j in the range of carPark[i] (each column)
                print(carPark[i][j], end=" | ") #prints the value of the current row and column, followed by a vertical bar
            print() #prints a new line after each row is printed

    elif carPark[row-1][column-1] != "empty": #if the parking spot is not empty
        while carPark[row-1][column-1] != "empty":
            print("This spot is occupied, please try again.") #prints statement
            row = int(input("Please enter the row you would like to park your car in (1-10): ")) #ask for integer input
            column = int(input("Please enter the column you would like to park your car in (1-6): ")) #ask for integer input
        if carPark[row-1][column-1] == "empty":
            carPark[row-1][column-1] = registeration
            print("You have reserved your spot, thank you.")
            for i in range(len(carPark)):
                for j in range(len(carPark[i])):
                    print(carPark[i][j], end=" | ")
                print()





def removeCar():
    registeration = input("Please enter your car's registeration: ")
    process = "Incomplete"
    while process != "Complete":
        for row in range(len(carPark)):
            for column in range(len(carPark[row])):
                if carPark[row][column] == registeration:
                    carPark[row][column] = "empty"
                    print("You have removed your car, thank you.")
                    process = "Complete"
                    for i in range(len(carPark)):
                        for j in range(len(carPark[i])):
                            print(carPark[i][j], end=" | ")
                        print()
                    break
            if process == "Complete":
                break
        if process != "Complete":
            print("Car not found, please try again.")
            registeration = input("Please enter your car's registeration: ")


def viewParkedCars():
    for i in range(len(carPark)):
        for j in range(len(carPark[i])):
                print(carPark[i][j], end=" | ")
        print()

def findCar():
    registeration = input("Please enter your car's registeration: ")
    process = "Incomplete"
    while process != "Complete":
        for i in range(len(carPark)):
            for j in range(len(carPark[i])):
                if carPark[i][j] == registeration:
                    print("Car found in row", i+1, ", column", j+1)
                    process = "Complete"
                    break
            if process == "Complete":
                break
        if process != "Complete":
            print("Car not found, please try again.")
            registeration = input("Please enter your car's registeration: ")

while True:
    menuPanel()
    choice = input("Enter your choice: ")

    if choice == "1":
        parkCar()
    elif choice == "2":
        removeCar()
    elif choice == "3":
        viewParkedCars()
    elif choice == "4":
        findCar()
    elif choice == "5":
        exit()
    else:
        print("Invalid choice. Please try again.")
        menuPanel()

