teams = ["Arsenal", "Chelsea", "Crystal Palace", "Manchester United", "Liverpool", "Manchester City", "Everton", "Spurs", "Hull", "Brighton"]
points = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]



def pointsAssign():
    for i in range(len(points)):
        assign = int(input("Please enter total points for each team:" ))
        points[i] = assign
    print(points)

def leagueWinner():
    i = 0
    topScore = points[i]

    for i in range(len(points)-1):
        if points[i-1] >= topScore:
            topScore = points[i-1]
            team = teams[i-1]
    print(team + ": " + str(topScore) + "pts")


def alphaSort():
    for i in range(1, len(teams)):
        holder = teams[i]
        pos = i-1
        while teams[pos] > holder and pos >= 0:
            teams[pos+1] = teams[pos]
            pos = pos - 1
        teams[pos+1] = holder

def pointsSort():
    for i in range(1, len(points)):
        holder = points[i]
        pos = i-1
        while teams[pos] > holder and pos >= 0:
            points[pos+1] = points[pos]
            pos = pos - 1
        points[pos+1] = holder
        
        
        
        
        

            


print(teams)
pointsAssign()


while True:

    print('''           
        Main Menu
    1. Sort alphabetically
    2. Sort by points
    3. Find out league winner
    4. Exit
    ''')

    choice = int(input("Please enter the required service: "))

    if choice == 1:
        alphaSort()

    if choice == 2:
        pointsSort()

    if choice == 3:
        leagueWinner()

    if choice == 4:
        quit()


