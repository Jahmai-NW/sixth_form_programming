teams = ["Arsenal", "Liverpool", "Tottenham", "Bournemouth", "Man City"]
points = [16, 15, 14, 14, 13]




def team_search(teams):
    for count in range(len(teams)):
        print(teams[count])

        



def each_team(teams):
    team = input("Enter a team: ")
    for count in range(len(teams)):
        if team == teams[count]:
            print("This team is in the top 5!")
        elif team != teams[count]:
            print("This team is not good enough for the top 5.")
            break



def points_to_team(teams, points):
    team = input("Enter a team: ")
    for count in range(len(teams)):
        if team == teams[count]:
            print(team + ": " + str(points[count]))
        else:
            print("This team isn't in the top 5!")
            break



def top_5_points():
    for count in range(len(teams)):
        print(teams[count]+": "+ str(points[count]))



#########################################################

while True:
    global choice
    choice = input("Please enter one of the following - Top 5 Teams, Top 5 Search, Top 5 Point Search, Top 5 Points: ")

    if choice == "Top 5 Teams":
        team_search(teams)

    elif choice == "Top 5 Search":  
        each_team(teams)

    elif choice == "Top 5 Point Search":
        points_to_team(teams, points)

    elif choice == "Top 5 Points":
        top_5_points()

    else:
        print("Sorry, that was an invalid choice, please try again.")
    