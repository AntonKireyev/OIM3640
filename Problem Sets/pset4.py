''' Reaction Time Program
Write a program to capture your reaction time based on the following
Print an introductory statement, something like "When prompted hit the enter key"
Wait for a random amount of time between 0 and 5 seconds
Display the message Quick hit the enter key
Print a message something like "That was fast. It took you 0.212 seconds to hit enter", 
note the time value should be based on a variable you calculate.
'''

# import libraries
import random
import time

# Start
print("When prompted hit the enter key, GET READY on 3")
for iteration in range(1,4):
    print(iteration)
    time.sleep(1)

times = []
# Run it X number of times
for attempt in range(5):
    time.sleep(random.randint(0,5))
    print("QUICK HIT THE ENTER KEY GO GO GO GO GO GO")
    start = time.time()
    input()
    reaction = time.time() - start
    times.append(reaction)
    print(f"That was fast. It took you {reaction:.3f} seconds to hit enter.")
    print(f"{attempt + 1} of 5")

print("Summary Report".center(30, "_"))
average_time = sum(times) / len(times)
slowest_time = max(times)
fastest_time = min(times)
print(f"Your average time was: {average_time:.3f}")
print(f"Your slowest time was: {slowest_time:.3f}")
print(f"Your fastest time was: {fastest_time:.3f}")




