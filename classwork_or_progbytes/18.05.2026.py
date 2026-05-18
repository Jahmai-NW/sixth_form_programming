stack = []

def push(item):
    stack.append(item)

def pop():
    print(stack.pop())

def peek():
    for i in range(len(stack)):
        return stack[len-1]
    
def size():
    return len(stack)

checkingWord = input("Enter word to check: ")
print(checkingWord)

for i in range(len(checkingWord)):
    push(checkingWord[i])



for i in range(len(checkingWord)):
    pallindrome = True
    if checkingWord[i] != str(pop()):
        pallindrome = False
        
    if pallindrome:
        print("This word is a pallindrome.")
    else: 
        print("This word is not a pallindrome.")
