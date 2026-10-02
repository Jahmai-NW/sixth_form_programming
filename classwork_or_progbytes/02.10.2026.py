numbers = [5, 9, 12, 4, 43, 10, 60]

# look at first number and second number
# check if first number is bigger than second number
# if yes, swap: second number stored, first number becomes second number, stored number becomes first number
# if no, skip da swap
# 


# swap = False
# for i in range(len(numbers)-1):
#     holder = numbers[i]
#     if holder > numbers[i+1]:
#         swap = True
#         while swap == True:
#             holder = numbers[i+1]
#             numbers[i+1] = numbers[i]
#             numbers[i] = holder
#             swap = False
#     else:
#         i = i+1
        

# print(numbers)
    




#######
# 

# look at second number first
# if second number bigger than first number
# move to third number
# 
# 
# 


print(numbers)
for i in range(1, len(numbers)): #for i in the range of 1 to 7
    holder = numbers[i] # second item is stored inside holder
    pos = i-1 # pos is set to index-1
    while numbers[pos] > holder and pos >= 0: #as long as the previous number is bigger than the current number, and pos is bigger than/equal to 0
        numbers[pos+1] = numbers[pos] # current item is set to previous item
        pos = pos - 1 # pos is set to pos-1
    numbers[pos+1] = holder #current item is stored inside holder

print(numbers)
        

