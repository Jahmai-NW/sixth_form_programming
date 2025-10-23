#SUBROUTINE
def greeting():
    global name
    print("Nice to meet you", name + "!")


#MAIN PROGRAM
name = input("Hello! What's your name?: ")
greeting()