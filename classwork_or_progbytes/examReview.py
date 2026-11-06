        # A, B, C
answers = [
    [True, False, False],
    [False, True, False],
    [False, False, True],
    [True, False, False],
    [False, True, False],
    [False, False, True],
    [False, False, True],
    [False, False, True],
]


counta = 0
countb = 0
countc = 0

for i in range(len(answers)):
    if answers[i][0] == True:
        counta = counta + 1
    elif answers[i][1] == True:
        countb = countb + 1
    elif answers[i][2] == True:
        countc = countc + 1

if counta > countb and counta > countc:
    print(counta)

if countb > counta and countb > countc:
    print(countb)

if countc > counta and countc > countb:
    print(countc)