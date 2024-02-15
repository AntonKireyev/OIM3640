''' Problem Set 8
Write a program that generates 500 random integers from 1 to n, 
for example, the first integer will be 1 the second will be 1 or 2, the fifth between 1 and 5, and so on.

The program should write each integer to a file 
Once all integers are written save and close the file

Part 2
open and read the file created into a list
plot the list data as a line plot'''

# Libraries (should be alphabetical order)
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
    f.write(str(integer)+ ' ')      # can use F strings as well.

f.close()

# Open and Read file into a list

datastring = ''
readfile = open("data/integers.txt", "r")
for datapoint in readfile:
    datastring += datapoint
readfile.close()

# Turn Data back into integers

data = [int(x) for x in datastring.split()]
print(data)

# plot list data as a line plot

plt.plot(data, label = 'Integers')
plt.title("Random Integers!", fontsize = 16)
plt.xlabel("N")
plt.ylabel("Integer")
plt.axis()
plt.legend(loc = 2); 
plt.yticks([0, 100, 200, 300, 400, 500])
plt.show()