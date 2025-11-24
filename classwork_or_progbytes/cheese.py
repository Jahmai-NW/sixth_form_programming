def multiples(table, startnum, endnum, pupilName):
    print("Hi, " + pupilName + "...here is your times table")
    #product = table * i
    for i in range(startnum,endnum+1):
        product = table * i
        print(str(table) + " x " + str(i) + " = " + str(product))

        
    
pupilName = input("What is your name?:  ")
table = int(input("Enter times table: "))
startnum = int(input("Enter start number: "))
endnum = int(input("Enter end number: "))

multiples(table, startnum, endnum, pupilName)


