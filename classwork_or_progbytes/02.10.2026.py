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



for i in range(1, len(numbers)-1):
    holder = numbers[i]
    pos = i-1
    if numbers[pos] > holder and pos >= 0:
        numbers[pos] = holder
        numbers[i] = numbers[pos]

    holder = numbers[i+1]

print(numbers)
        

