user = int(input("Enter number 1: "))
user2 = int(input("Enter number 2: "))
user3 = int(input("Enter number 3: "))
user4 = int(input("Enter number 4: "))
users = [user, user2, user3, user4]
from random import choice
random_num = choice(users)
print("The computer has selected:", random_num)