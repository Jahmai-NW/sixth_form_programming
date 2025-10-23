import random

random.randint() #give range
        #or
from random import randint
number = randint(1,100)
print("A random number between 1 and 100 is" , number)


random.choice() #give list or array, or even normal string
        #or
from random import choice
animals = ["cat" , "dog" , "horse" , "cow"]
randomanimal = choice(animals)
print("A random animal is", randomanimal)


random.sample() #give array, outputs more than one string

random.shuffle()

#####################################################

import time

time.sleep()
        #or
from time import sleep
for second in range(1,11):
    print(second)
    sleep(1)


   
time.ctime()
        #or
from time import ctime
print("Current time:" , ctime())




time.strftime()


##################################################

import math

math.sqrt()

math.pi


##############################################################

