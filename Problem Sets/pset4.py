''' Reaction Time Program
Write a program to capture your reaction time based on the following
Print an introductory statement, something like "When prompted hit the enter key"
Wait for a random amount of time between 0 and 5 seconds
Display the message Quick hit the enter key
Print a message something like "That was fast. It took you 0.212 seconds to hit enter", 
note the time value should be based on a variable you calculate.

Use the datetime library to print a human readable date in ISO format.
Use the datetime library to today's date in US format.

Show the code needed to generate a random variate from the standard normal distribution. Store the value in a variable named z_score. 
'''

# import libraries
import datetime
import random
import time

# Start
print("When prompted hit the enter key")
time.sleep(random.randint(0,5))
print("QUICK HIT THE ENTER KEY GO GO GO GO GO GO")
start = time.time()
input()
print(f"That was fast. It took you {time.time() - start:.3f} seconds to hit enter.")