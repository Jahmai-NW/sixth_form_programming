q = []
maxSize = 10

def enqueue(item, q):
    q.append(item)

def dequeue(item, q):
    item = input("Please enter the item you want to remove: ")
    for i in range(len(q)):
        if item == q[i]:
            q.remove(q[i])
    else:
        print("This item does not exist.")

def isFull(q):
    if len(q) == maxSize:
        return True
    
def isEmpty(q):
    if len(q) < 1:
        return True
    

enqueue("Bob", q)
print(q)