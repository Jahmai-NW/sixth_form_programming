# pupils = ["James", "Mary", "John", "Patricia", "Robert", "Liam", "Olivia", "Noah", "Emma", "Oliver", "River", "Willow"]
# group1 = ["", "", "", "", "", ""]
# group2 = ["", "", "", "", "", ""]

# # print(len(pupils))

# # for i in range(len(pupils)-1):
# #     for j in range(len(pupils)+1):
# #         group1[j] = pupils[i]
# #         group2[j] = pupils[i+1]

# place = 0

# while place <= 6:
#     for i in range(len(pupils)-1):
#         group1[place] = pupils[i]
#         group2[place] = pupils[i+2]
#         place += 1

# print(group1)
# print(group2)
    


school = ["AAAA", "BBBB", "CCCC", "DDDD"]
medal = [4,7,1,3]

newResult = int(input("Please enter the new result: "))
schoolnumber = int(input("Please enter the school number: "))

if schoolnumber == 1:
    medal[0] = newResult

if schoolnumber == 2:
    medal[1] = newResult

if schoolnumber == 3:
    medal[2] = newResult

if schoolnumber == 4:
    medal[3] = newResult

if schoolnumber == -1:
    for i in range(len(medal)-1):
        print("School number:", i+1, ",", "School name:", school[i], ",", "Number of medals:", medal[i])