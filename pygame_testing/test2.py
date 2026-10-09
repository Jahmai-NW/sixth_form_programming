import random
import pygame as pd 

def sim_penalty():
    x=[]
    y=[]
    for i in range(10000):
        x_result = random.randint(0,1)
        y_result = random.randint(0,1)
        x.append(x_result)
        y.append(y_result)
        x_sum = pd.Series(x).sum()
        y_sum = pd.Series(y).sum()
        if i>=3 and i<=5:                                                              
            if x_sum>3 and y_sum<3:
                winner = 'X'
                break
            if y_sum>3 and x_sum<3:
                winner = 'Y'
                break
            if y_sum==3 and x_sum==0:
                winner = 'Y'
                break    
            if x_sum==3 and y_sum==0:
                winner = 'X'
                break
        if i==5:
            if x_sum > y_sum:
                winner = 'X'
                break
            if x_sum < y_sum:
                winner = 'Y'
                break
        if i>5:
            if x_result > y_result:
                winner = 'X'
                break
            if y_result > x_result:
                winner = 'Y'
                break


    return {'Team A':x_sum,'Team B':y_sum,'Total Penalties':i+1,'Winner':winner*2}