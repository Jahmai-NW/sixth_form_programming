from random import sample
days = ["Monday" , "Tuesday" , "Wednesday" , "Thursday" , "Friday"]
two_days = sample(days , 2)
print("You will be set homework on:" , *two_days)

from random import shuffle
mylist = ["apple", "banana", "cherry"]
print("Before shuffle:", mylist)
shuffle(mylist)
print("After shuffle:", mylist)

from time import ctime
print("Current time:", ctime())


from colorama import Fore

print(Fore.BLACK + "Hello There")


import os


print("Hello")
os.system("clear")
print("Bye")