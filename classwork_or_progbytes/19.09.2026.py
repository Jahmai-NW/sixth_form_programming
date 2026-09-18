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
        if points[i+1] >= topScore:
            topScore = points[i+1]

    print(topScore)


print(teams)
pointsAssign()
leagueWinner()

while True:

    print('''           
        Main Menu
    1. Sort alphabetically
    2. Sort by points
    3. Find out league winner
    4. Display Leaderboard
    5. Exit
    ''')

    choice = int(input("Please enter the required service: "))

    if choice == 1:
        None

    if choice == 2:
        None

    if choice == 3:
        None

    if choice == 4:
        None

    if choice == 5:
        quit()


