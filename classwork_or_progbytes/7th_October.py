num1 = int(input("Enter number of paper bags: "))
num2 = int(input("Enter number of sweets: "))

while num2 > num1:
    if num2 % num1 == 0:
        if num2 % 2 == 0:
            print("There are enough bags.")
        else:
            print("There are not enough bags.")
    else:
        print("There are not enough bags.")
    
