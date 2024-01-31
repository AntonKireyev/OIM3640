''' Dice Rolling Simulator

This problem makes use of the random module, either a for loop or while loop and if...elif...else. 
Try entering import random into the shell, then explore the functions within the module. 
For this activity you will need to simulate rolling dice.  
Can you figure out a way to “randomly roll” a single 6-sided die? 
Now write a program that simulates rolling two dice and keeps track of the total of each roll, 
and how many times in the simulation that total was "rolled".  
The program will then output each possible roll total and the number of times it occurred as a pipe or other symbol.  
Allow a user to specify how many rolls to simulate.  
'''

import random

rolls = int(input("how many rolls: "))
dice = [1,2,3,4,5,6]

'''
two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eight = 0
nine = 0
ten = 0
eleven = 0
twelve = 0
'''

# print # of dice rolls defined by user
for iteration in range(rolls):
    d1 = random.choice(dice)
    d2 = random.choice(dice)
    dsum = d1 + d2
    print(f"{iteration:<10}{d1} + {d2} = {dsum}")

   
    

