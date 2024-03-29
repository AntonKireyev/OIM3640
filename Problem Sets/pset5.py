''' DICE Rolling Simulator

A program that simulates rolling two DICE and keeps track of the total of each roll, 
and how many times in the simulation that total was "rolled".  
The program will then output each possible roll total and the number of times it occurred as a pipe or other symbol.  
Allows a user to specify how many rolls to simulate.  
'''
# Import libraries and define variables
import math
import random
DICE = [1,2,3,4,5,6]
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

# Welcome Message and user input
intro = "Welcome to the DICE rolling simulator\nGet ready to roll dem bones!\nHow many rolls should we simulate?\n\n"
rolls = math.floor(float(input(intro)))     # Accounts for non-integer inputs, but not for non-numerical or negative inputs

# simulate # of DICE rolls defined by user and adjust COUNTERs
for iteration in range(rolls):
    d1 = random.choice(DICE)
    d2 = random.choice(DICE)
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