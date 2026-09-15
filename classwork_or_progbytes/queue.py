q = ["Sarah", "Charles", "Bob", "Melissa"]

maxSize = 4

def enqueue(item, q):
    if not isFull(q):
        q.append(item)

def dequeue(q):
    return q.pop(0)

def isFull(q):
    if len(q) == maxSize:
        return True

def isEmpty(q):
    if len(q) < 1:
        return True

