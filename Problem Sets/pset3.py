# CD Calculator

# Initialize
print('We are currently offering an amazing 1.5% on 5 year CDs \n Tell me how much you got...... \n I\'ll tell what it will be over the next 5 years.')

# Inputs
balance = float(input('''Enter initial deposit: 
'''))
RATE = 1.015        # Symbolic Constant

# Table Headers
print('Year\t\tBalance\n'+ '_' * 24 +'\n')

# Year and Balance Calculations
for year in range(1,6,1):
    balance *= RATE
    print(f"{year:<15}${balance:<10,.2f}")

'''Generates a list from 1-5, this indicates years passed.
for each loop, increase the balance amount by the rate. This is displayed along with the year.
'''