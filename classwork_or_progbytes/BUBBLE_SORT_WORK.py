cards = [2, 3, 4, 7, 8, 10, 12, 13]

unsortedCards = [13, 4, 3, 7, 2, 10, 8, 12]

 # loop to access each array element
for i in range(len(unsortedCards)):

    # loop to compare array elements
    for j in range(0, len(unsortedCards) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
        if unsortedCards[j] > unsortedCards[j + 1]:

        # swapping elements if elements
        # are not in the intended order
            temp = unsortedCards[j]
            unsortedCards[j] = unsortedCards[j+1]
            unsortedCards[j+1] = temp


print(unsortedCards)