theStack = ["", "", "", "", ""]

top = 0
size = 0

def push(item):
    global top, size

    if isFull():
        print("ERROR: Stack Overflow")
        return
        
    theStack[top] = item
    top = top + 1
    size = size + 1


def pop():
    global top, size

    if isEmpty():
        print("ERROR: Stack Empty")
        return
    
    top = top - 1
    size = size - 1
    return theStack[top]


def isFull():
    if size == (len(theStack)-1):
        return True
    else:
        return False

def isEmpty():
    if size == 0:
        return True
    else:
        return False
    
while True:
    print('''
            1. View stack
            2. Push an item
            3. Pop an item
            4. Check if stack is full
            5. Check if stack is empty

          ''')
    
    choice = int(input("Please enter a value: "))

    if choice == 1:
        print(theStack)

    if choice == 2:
        item1 = input("Enter data: ")
        push(item1)

    if choice == 3:
        print(pop())

    if choice == 4:
        isFull()

    if choice == 5:
        isEmpty()
    




