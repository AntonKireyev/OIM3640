# Counting and conditional Loops

# Counting Loops
# Anytime you repeat the same code (mre than once), you should probably write a loop structure
'''
# range([start], stop, [step])
for index in range(3):
    print(index)

# it STOPS one number before the stop.
for index in range(1, 4):
    print(index)

# we can define a step
for index in range(0, 50, 5):
    print(index)'''

# We can also do math on the outputs
for index in range(5):
    print(f"{index ** 2}")

# LISTS

range(10)

# This iterates over the range
numbers = list(range(10))
print(numbers)

for number in numbers:
    print(f"{number ** 2}")

# if we want to find a number, we have to search for the number index

numbers = list(range(1,10))
numbers

# lists start at 0, so the first number index is 0
number[0]

## We can count in reverse as well

import time
for second in range(10, 0, -1):
    print(second)
    time.sleep(1)

# sleep is part of the python standard library, causes the loop to pause for a second.
    
## You can also list strings
fruits = ['kiwi', 'pear', 'apple']

for fruit in fruits:
    print(f"{fruit} is a fruit")

## Can do it for a singular string
greeting = "Hello"
for letter in greeting:
    print(letter)

list(greeting)

len(fruits)
len(greeting)

for index in range(len(greeting)):
    print(f"{index:<10}{greeting[index]}")
    
# We can define two letters
for index, letter in enumerate(greeting):
    print(f"{index:<10}{letter}")