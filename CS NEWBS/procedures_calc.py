#SUBROUTINE
def addition():
    global num1, num2
    total = num1 + num2
    print(num1, "+", num2, "=", total)

def subtraction():
    global num1, num2
    total = num1 - num2
    print(num1, "-", num2, "=", total)


#MAIN PROGRAM
while True:
    choice = input("Enter addition, subtraction, or stop: ")

    if choice == "stop":
        break

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if choice == "addition":
        addition()
    
    elif choice == "subtraction":
        subtraction()