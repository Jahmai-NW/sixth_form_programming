#SUBROUTINES
def guessNum():
     global guess
     guess = str(input("Guess the four digit number or Exit: "))

def hardguessNum():
     global guess
     guess = str(input("Guess the five digit number or Exit: "))

def guessDigit1():
    if guess[0] == number[0]:
        print("The first digit from your guess is correct!")

def guessDigit2():
    if guess[1] == number[1]:
        print("The second digit from your guess is correct!")

def guessDigit3():
    if guess[2] == number[2]:
        print("The third digit from your guess is correct!")

def guessDigit4():
    if guess[3] == number[3]:
        print("The fourth digit from your guess is correct!")

def noDigit():
        if guess[0] != number[0]:
                if guess[1] != number[1]:
                        if guess[2] != number[2]:
                                 if guess[3] != number[3]:
                                    print("None of the digits from your guess are correct.")

def hardguessDigit1():
    if guess[0] == number2[0]:
        print("A number from your guess is correct!")

def hardguessDigit2():
    if guess[1] == number2[1]:
        print("A number from your guess is correct!")

def hardguessDigit3():
    if guess[2] == number2[2]:
        print("A number from your guess is correct!")

def hardguessDigit4():
    if guess[3] == number2[3]:
        print("A number from your guess is correct!")

def hardguessDigit5():
     if guess[4] == number2[4]:
          print("A number from your guess is correct!")

def hardnoDigit():
        if guess[0] != number2[0]:
                if guess[1] != number2[1]:
                        if guess[2] != number2[2]:
                                 if guess[3] != number2[3]:
                                    if guess[4] != number2[4]:
                                        print("None of the digits from your guess are correct.")
def hardMode():
    from random import randint
    number2 = str(randint(10000,100000))
    guessCount = 0
    while True:
        hardguessNum()
        hardguessDigit1()
        hardguessDigit2()
        hardguessDigit3()
        hardguessDigit4()
        hardnoDigit()

        while guess != number2:
            guessCount += 1
            hardguessNum()
            hardguessDigit1()
            hardguessDigit2()
            hardguessDigit3()
            hardguessDigit4()
            hardnoDigit()

        if guess == number2:
            print("You got it! Well done! It took", guessCount, "tries!")
            number2 = str(randint(10000,100000))

        if guess == "Exit.":
            print("The number was", number2)
            number2 = str(randint(10000,100000))

####################################################################
from random import randint
number = str(randint(1000,10000))
number2 = str(randint(10000,100000))
guessCount = 0
guess = input("Welcome! Would you like the easy version or hard version?: ")
if guess == "Hard":
    hardMode()
elif guess == "Easy":
    while True:
        guessNum()
        guessDigit1()
        guessDigit2()
        guessDigit3()
        guessDigit4()
        noDigit()

        while guess != number:
            guessCount += 1
            guessNum()
            guessDigit1()
            guessDigit2()
            guessDigit3()
            guessDigit4()
            noDigit()

        if guess == number:
            print("You got it! Well done! It took", guessCount, "tries!")
            number = str(randint(1000,10000))

        if guess == "Exit":
            print("The number was", number)
            number = str(randint(1000,10000))



    

#stringedNumber = str(number)