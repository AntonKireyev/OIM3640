''' Problem Set 8
Write a program that generates 500 random integers from 1 to n, 
for example, the first integer will be 1 the second will be 1 or 2, the fifth between 1 and 5, and so on.

The program should write each integer to a file 
Once all integers are written save and close the file

Part 2
open and read the file created into a list
plot the list data as a line plot'''

# Libraries
import os
import matplotlib.pyplot as plt
import random as rand

# Generate 500 random integers
N = 500
integers = [rand.randint(1, value) for value in range(1,N+1)]

# Write Integers to new file
os.chdir(os.getcwd())
f = open("data/integers.txt", "w")
for integer in integers:
    f.write(str(integer)+ ' ')

f.close()

# Open and Read file into a list

datastring = ''
readfile = open("data/integers.txt", "r")
for datapoint in readfile:
    datastring += datapoint

readfile.close()
data = datastring.split()
print(data)

# plot list data as a line plot

plt.plot(data, label = 'Integers')
plt.title("Title", fontsize = 16)
plt.xlabel("N")
plt.ylabel("Integer")
plt.axis()
plt.legend(loc = 2); 
y_values = [0, 100, 200, 300, 400, 500]
plt.yticks(y_values)
plt.show()