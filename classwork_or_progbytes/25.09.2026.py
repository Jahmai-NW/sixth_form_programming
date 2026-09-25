file = open("names", "w")


for i in range(10):
    newName = input("Please enter a name to be stored: ")
    file.write(newName)
    file.write("\n")


file = 

for count in range(len(names)):
    for j in range(0, len(names) - i - 1):

        if names[j] > names[j + 1]:

            temp = names[j]
            names[j] = names[j+1]
            names[j+1] = temp




file.close()