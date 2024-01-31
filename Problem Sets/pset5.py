''' Dice Rolling Simulator

A program that simulates rolling two dice and keeps track of the total of each roll, 
and how many times in the simulation that total was "rolled".  
The program will then output each possible roll total and the number of times it occurred as a pipe or other symbol.  
Allows a user to specify how many rolls to simulate.  
'''
import math
import random

intro = "Welcome to the dice rolling simulator\nGet ready to roll dem bones!\nHow many rolls should we simulate?\n\n"

user_input = input(intro)

rolls = math.floor(float(user_input))
dice = [1,2,3,4,5,6]

COUNTER = "*"

Twos = ""
Threes = ""
Fours = ""
Fives = ""
Sixes = ""
Sevens = ""
Eights = ""
Nines = ""
Tens = ""
Elevens = ""
Twelves = ""

# simulate # of dice rolls defined by user and adjust COUNTERs
for iteration in range(rolls):
    d1 = random.choice(dice)
    d2 = random.choice(dice)
    dsum = d1 + d2
    if dsum == 2:
        Twos += COUNTER
    elif dsum == 3:
        Threes += COUNTER
    elif dsum == 4:
        Fours += COUNTER
    elif dsum == 5:
        Fives += COUNTER
    elif dsum == 6:
        Sixes += COUNTER
    elif dsum == 7:
        Sevens += COUNTER
    elif dsum == 8:
        Eights += COUNTER
    elif dsum == 9:
        Nines += COUNTER
    elif dsum == 10:
        Tens += COUNTER
    elif dsum == 11:
        Elevens += COUNTER
    elif dsum == 12:
        Twelves += COUNTER
    else:
        print("Unexpected Error")
        continue

# Print Outputs
print(f"Simulation outcome:")
print('-' * 20)
print(f"{'Twos':8}: {Twos}")
print(f"{'Threes':8}: {Threes}")
print(f"{'Fours':8}: {Fours}")
print(f"{'Fives':8}: {Fives}")
print(f"{'Sixes':8}: {Sixes}")
print(f"{'Sevens':8}: {Sevens}")
print(f"{'Eights':8}: {Eights}")
print(f"{'Nines':8}: {Nines}")
print(f"{'Tens':8}: {Tens}")
print(f"{'Elevens':8}: {Elevens}")
print(f"{'Twelves':8}: {Twelves}")