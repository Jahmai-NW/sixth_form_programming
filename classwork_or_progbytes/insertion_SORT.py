cards = [8, 1, 7, 9, 4]

for i in range(1, len(cards)):
    holder = cards[i]
    pos = i-1
    while cards[pos] > holder and pos >= 0:
        cards[pos+1] = cards[pos] 
        pos = pos - 1
    cards[pos + 1] = holder


print(cards)