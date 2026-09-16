cards = [5, 12, 6, 4, 10, 1]

for i in range(1, len(cards)): #for i in range 1 to the length of cards array (6)
    holder = cards[i] #the value of the current card's index (1 in this case) is stored in holder
    pos = i-1 #value of index - 1 is stored in pos
    while pos >= 0 and cards[pos] > holder: #as long as pos is equal to or greater than 0, and the card before the current card is bigger than the current cards value
        cards[pos+1] = cards[pos] #the current card is changed to the card before the current card
        pos = pos - 1 #the value of (index -1) -1 is stored in ois
    cards[pos + 1] = holder #the value stored in holder is transferred to the value of card with index pos + 1
print(cards) #prints cards


#in the first instance:
#length of array is 6
# 12 is stored in holder
# 0 is stored in pos
# pos = 0 but cards[0] (5) is not bigger than 12, so skips over
# holder (12) is stored in cards[1] (12)

#holder = 6
# i = 2
# pos = 1
# pos > 0, cards[1] (12) > 6
# cards[1] (12) is set/moved to cards[2]
# pos = 1-1 = 0
