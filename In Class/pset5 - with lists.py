#   Dice rolling simulator

import random

print('Welcome to the dice rolling game')
rolls = int(input('how many rolls do u want'))

counts = [0 for x in range(11)]
roll_values = list(range(2,13))

for count in range(rolls):
    roll = random.randint(1,6) + random.randint(1,6)

    if roll == 2:
        counts[0] +=1
    elif roll == 3:
        counts[1] += 1
    elif roll == 4:
        counts[2] += 1
    elif roll == 5:
        counts[3] += 1
    elif roll == 6:
        counts[4] += 1
    elif roll == 7:
        counts[5] += 1
    elif roll == 8:
        counts[6] += 1
    elif roll == 9:
        counts[7] += 1
    elif roll == 10:
        counts[8] += 1
    elif roll == 11:
        counts[9] += 1
    elif roll == 12:
        counts[10] += 1


print(f"Simulation outcome:")
print('-' * 20)

for iteration in range(11):
    print(f"{roll_values[iteration]:<8}: {counts[iteration]*'|'}")


