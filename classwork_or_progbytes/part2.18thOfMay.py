theStack = ["", "", "", "", ""]

size = 0
topPointer = 0


def isFull():
    if size == len(theStack):
        print("This stack is full")
    else:
        print("This stack is not full")
    

def isEmpty():
    if size == 0:
        print("This stack is empty")
    else:
        print("This stack is not empty")

def push(item):
    global topPointer
    theStack[topPointer] = item
    topPointer = topPointer + 1

def pop():
    global topPointer
    return theStack[topPointer]

push("yessir")
print(theStack)