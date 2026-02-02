people = ["Gary", "Sophie", "Charles", "Bob", "Hugo", "Julian", "Lorenzo", "Oliver", "Sasha", "Mason"]

searchingQ = input("Please enter a name to be searched: ")
for i in range(len(people)):
    if searchingQ in people:
        if searchingQ == people[i]:
            print("Found", people[i], "in position", (i+1))
        searchingQ = input("Please enter a name to be searched: ")
    elif searchingQ not in people:
        print("Not Found")
        searchingQ = input("Please enter a name to be searched: ")