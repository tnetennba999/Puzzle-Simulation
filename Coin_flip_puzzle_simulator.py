'''
coin filp simulation
question: there are 100 coins lay flat on a table. 10 of them are head, remaining 90 are tails.
You could not feel/see which coin is head/tail.
Split 2 piles of coin so that each pile has the same number of head coin.
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import seaborn as sns
from astropy.table import QTable, Table, Column
from scipy.stats import 

#create a list of 10 coins, T/0 as Tail; H/1 as Head

coin = []
total_coin = 100
num_head = 10
first_pile = []
def coin_set_creator():
    for i in range(num_head):
        coin.append('H')
    for i in range(total_coin - num_head):
        coin.append('T')
    random.shuffle(coin)
    print("There are " + str(total_coin) + " coins. " + str(num_head) + " of them are head.")
    print(list(coin))
    print("\n")
    print("NOW! Pick and flip!")
    for i in range(num_head):
        pick = coin.pop(i)
        if pick == "H":
            pick = "T"
        else:
            pick = "H"
        first_pile.append(pick)
    print(str(num_head) + " were picked, fliped and assigned to the first pile.")
    print(list(first_pile))
    print("\n")
    print("The untouched coins were assigned to the second pile.")
    print(list(coin))
    print("\n")
coin_set_creator()

H_num_1 = first_pile.count('H')
T_num_1 = first_pile.count('T')
H_num_2 = coin.count('H')
T_num_2 = coin.count('T')

t = Table()
a = ["1st", "2nd"]
b = [H_num_1, H_num_2]
c = [T_num_1, T_num_2]
t = Table([a, b, c], names=('Pile', 'Number of Head', 'Number of Tail'))
print(t)
print("The number of head for both piles are " + str(H_num_1)+".")

#Find average final number of head based on hypothesis below.
#Q1. Under same initial number of heads, do the size of total coins affect final number of head?
#Q2. Under same total coins, do the size of initial number of heads affect the final number of head?
#Q3. Is there a relationship that widen or shallow the fluctuation of the final number of head?





