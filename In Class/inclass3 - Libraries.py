# Python Libraries

# time
import time
time.sleep(1)
print("Hello")

#help(time.daylight)

# import specific functions
from time import sleep, time
sleep(1)
print("hello2")

# epoch time - seconds since 1/1/1970
print(time())

# import all functions in the library
from random import *    # import everything from random - dont do this
import random       # import just the "wrapper" from random, this is better
print(random.random())
print(random.randint(1,6))

# timer
start = time()
sleep(random.randint(1,5))
print(f"{time() - start:.2f}")

# rock paper scissors
choices = ['rock', 'paper', 'scissors']
print(random.choice(choices))

# random sample - Good for statistical analysis with large datasets
random.sample(choices, 2)

# MATH
import math
print(math.pi)
math.e      # eulers's constant
5 // 2      # floor math - you get integer value.
math.floor(5 / 2)
math.ceil(5 / 2)
4 ** 0.5        #sqrt
math.sqrt(4)

# Simulate stock price
from math import exp, sqrt
from random import normalvariate as norm        # can use "as" to alias a variable, in this case we alias normalvariate as norm
x = 1
exp(x)      # raises euler's constant by x

rate = 0.0525
sigma = 0.18
T = 1/252
spy = 487

price = spy * exp((rate - 0.5* sigma **2) * T + sigma * sqrt(T) * norm())       # Brownian Motion Equation
print(price)

ending_values = []
for iteration in range(10000):
    price = spy * exp((rate - 0.5* sigma **2) * T + sigma * sqrt(T) * norm())       # Brownian Motion Equation
    ending_values.append(price)     # Use append to add a new item to the list

print(ending_values[:20])
print(len(ending_values))
print(max(ending_values))
print(min(ending_values))
sum(ending_values)

mean = sum(ending_values)/len(ending_values)

# standard deviation
mean = sum(ending_values)/len(ending_values)
ss = 0
for value in ending_values:
    ss += (value - mean) ** 2

print(f"{ss:,.2f}")
var = ss / (len(ending_values) -1)
std = sqrt(var)
print(f"{var:,.2f}")
print(f"{std:,.2f}")
# Polymorphism
len("hello")
max("hello")
ord('o')        # uppercase will get you a smaller value than lowercase


# Date Time
import datetime as dt
dt.datetime.today()
dt.date.today()         # YYYY - MM - DD (ISO)
print(dt.date.today())

today = dt.date.today()
print(today.strftime("%A %B %d %Y"))    # string formatting

today.year
today.month
today.day

import datetime
today = datetime.date.today()
today.strftime("%m %d %Y") 

import random
print(random.normalvariate())