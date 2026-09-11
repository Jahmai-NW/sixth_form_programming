cards = [2, 3, 4, 7, 8, 10, 12, 13]

unsortedCards = [13, 4, 3, 7, 2, 10, 8, 12]

swap = True
swapCount = 0

while swap == True:
    for i in range(len(unsortedCards)):
        while swap == True:
            if unsortedCards[i] > unsortedCards[i+1]:
                temp = unsortedCards[i+1]
                unsortedCards[i+1] = unsortedCards[i]
                unsortedCards[i] = temp
                swapCount += 1
            else:
                continue
            swap = False
print(unsortedCards[i])