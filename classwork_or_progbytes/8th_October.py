days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

scores = [
    [45, 37, 78, 95, 79, 13, 67],
    [55, 15, 98, 12, 62, 67, 76],
    [35, 75, 74, 54, 12, 41, 14],
    [75, 23, 83, 23, 32, 53, 35],
    [43, 53, 54, 63, 13, 78, 87],
    [72, 29, 25, 12, 72, 98, 89],
    [97, 10, 83, 56, 71, 32, 23],
    [12, 27, 75, 63, 74, 64, 46],
    [90, 14, 12, 61, 63, 54, 45],
    [60, 47, 87, 62, 43, 46, 74]
]

names = ["Jahmai", "Richard", "Mufed", "Derin", "Caleb", "Abeer", "Kianna", "Sem", "Johnathan", "Lionel"]


###################################################################################################



def everyPersonScores():
    for count in range(len(names)):
        print(names[count] + ": " + str(scores[count]))
        

def onePersonScores():
    from time import sleep
    for count in range(len(names)):
        print(str(count) + ": " + names[count])
    person = input("Please enter a name: ")
    for count in range(len(names)):
        if names[count] == person:
            print("Searching...")
            sleep(1)
            print("Found!")
            print(names[count] + ": " + str(scores[count]))


def personOnDay():
    for count in range(len(names)):
        print(str(count) + ": " + names[count])
    person = input("Please enter a name: ")
    for count in range (len(days)):
        print(str(count) + ": " + days[count])
    day = int(input("What day would you like scores for? Please enter the number of the corresponding day: "))

    for count in range(len(names)):
        if names[count] == person:
            print(names[count] + " got " + str(scores[count][day]) + " on " + str(days[day]))

def onePersonAverage():
    for count in range(len(names)):
        print(str(count) + ": " + names[count])
    person = input("Please enter a name: ")
    for count in range(len(names)):
        if names[count] == person:
           total = sum(scores[count]) #adds all the values in one array of the person
           average = total / len(scores[count]) #divides that toal by length of it
           print(names[count] + " has an average score of", int(average), "out of 100 this week.")
           break


def averageForAll():
    total = 0
    count = 0
    for i in range(len(scores)):
        total += sum(scores[i])
        count += len(scores[i])
    average = total / count
    print("The average score for this class is", int(average))


########################################################################################################################################################


while True:
    menu = int(input('''
    Main Menu!
Please enter the number corresponding to your option:

1. List of everyone's scores throughout the week

2. Specific search of one person's scores throughout the week

3. Specific search of one person's scores on one day

4. Search of one person's average score for the week
                     
5. Search for total average of scores in this class
                     
                    6. Exit
ENTER HERE: '''))


    from time import sleep
    if menu == 1:
        print("Searching...")
        sleep(0.5)
        everyPersonScores()

    from time import sleep
    if menu == 2:
        print("Searching...")
        sleep(0.5)
        onePersonScores()

    from time import sleep
    if menu == 3:
        print("Searching...")
        sleep(0.5)
        personOnDay()

    from time import sleep
    if menu == 4:
        print("Searching...")
        sleep(0.5)
        onePersonAverage()

    from time import sleep
    if menu == 5:
        print("Searching...")
        sleep(0.5)
        averageForAll()


    if menu == 6:
        break

    from time import sleep
    print('''
    Going back to menu...
    ''')
    sleep(2)





        