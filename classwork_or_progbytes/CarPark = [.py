CarPark = [
    [" "," ","baka"," "," "," ",],
    [" "," "," "," "," "," ",],
    [" "," "," "," "," "," ",],
    [" "," "," "," "," "," ",],
    [" "," "," "," "," "," ",],
    [" "," "," "," "," "," ",],
    [" "," "," "," "," ","X",],
    [" "," "," "," "," "," ",],
    [" "," "," "," "," "," ",],
    [" "," "," "," "," "," ",],
    ]

def emptyCarPark ():
    for i in range (len(CarPark)):
        for j in range (len(CarPark)[i]):
            len(CarPark)[i][j] == " "

def parkACar ():
    Empty = True
    while Empty == True:

        RowInput = int(input("What row would you like to park in? "))
        Collum = int(input("What collum would you like to park in? "))

        if (CarPark)[RowInput - 1][Collum - 1] != " ":
            print("space is not empty.")
            RowInput = int(input("What row would you like to park in? "))
            Collum = int(input("What collum would you like to park in? "))
            Empty = False
            
        else:
            CarReg = input("Please enter your car's registration number: ")
            (CarPark)[RowInput - 1][Collum - 1] == CarReg
            print(CarPark)
        break

##################



parkACar()
