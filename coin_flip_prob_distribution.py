#Find average final number of head based on hypothesis below.
#Q1. Under same initial number of heads, do the size of total coins affect final number of head?
#Q2. Under same total coins, do the size of initial number of heads affect the final number of head?
#Q3. Is there a relationship that widen or shallow the fluctuation of the final number of head?

import numpy as np
import matplotlib.pyplot as plt
import random

#create a list of 10 coins, T/0 as Tail; H/1 as Head

coin = []
total_coin = 100
num_head = 15
first_pile = []

def coin_set_creator():
    for i in range(num_head):
        coin.append('H')
    for i in range(total_coin - num_head):
        coin.append('T')
    random.shuffle(coin)
    #print("There are " + str(total_coin) + " coins. " + str(num_head) + " of them are head.")
    #print(list(coin))
    #print("\n")
    #print("NOW! Pick and flip!")
    for i in range(num_head):
        pick = coin.pop(i)
        if pick == "H":
            pick = "T"
        else:
            pick = "H"
        first_pile.append(pick)


def many_trial():  
    print("Start running." + "\n")
    trial = 0
    total_run_time = 50000
    trial_store = []
    while trial < total_run_time:
        coin_set_creator()
        H_num_1 = first_pile.count('H')
        trial_store.append(H_num_1)
        first_pile.clear()
        coin.clear()
        trial += 1
     
    # intilize a null list 
    unique_list = [] 
    
    # traverse for all elements 
    for x in trial_store: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x)
    unique_list.sort()
    
    print("Total coin: " + str(total_coin) + "; Initial heads: " + str(num_head) + "\n")
    #print(trial_store)
    print("Total trials: " + str(total_run_time) + "\n" + "Final heads number appear possibility: " + str(len(unique_list)))
    print(unique_list)
    
    #plot graph
    x = unique_list
    #count number in unique list
    count_unique_list = []
    for i in unique_list:
        count = trial_store.count(i)
        count_unique_list.append(count)
    print("Count its frequency:")
    print(count_unique_list)
     
    y = count_unique_list
    plt.bar(x, y, width=0.8, color=['blue'])
    plt.xticks(np.arange(min(x), max(x)+1, 1.0))
    plt.show()
    
many_trial()

#creat a probability distribution


