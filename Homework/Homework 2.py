# Amortization Schedule Calculator

''' Instructions:
The program takes several inputs from the user and then outputs either monthly or annual loan
amortization report. In addition, a loan summary is output (see sample output below).
This program uses the functions from the numpy_financial package to calculate payments. 
NumPy Financial has a number of functions that essentially work like Excel spreadsheet functions. 
After reading through this document and examining the sample output, take a look at the documentation here to see what functions might be useful for this assignment.
You should be able to write the solution to this assignment in about 100 lines of code, depending on
how much white space you include and how many comments you provide. If you find yourself writing
20 or 30 lines, probably you forgot something (or your code is very brief), and if you find yourself writing
more than 150-200 lines of code, you might check again to see what you can do to structure your
solution more efficiently.
'''

# Import Libraries
import numpy_financial as npf

# Variables / Inputs
# Lists for Calculations
i_payments = []
p_payments = []


# Sample / manual selector
mode = input("type S for sample or M for manual input: ")
while mode not in "SM":
    mode = input("type S for sample or M for manual input: ")

if mode == "S":
    balance = 360000   # In Dollars
    loan_time = 360     # In Months
    int_rate = 2.4/100       # Annual Rate in %
    monthly_pmnt = 2000    # Monthly payment in Dollars

if mode == "M":
    balance = input("Balance: ")
    loan_time = input("Loan length in months: ")
    int_rate = input("Annual Interest Rate: ")/100
    monthly_pmnt = input("Monthly Payment: ")

# Logic / Conversions
yearly_pmnt = monthly_pmnt * 12
year_total = loan_time/12

# Payment Amounts
header = f"{'Year':<10}{'Principal':<15}{'Interest':<15}{'Payment':<15}{'Remaining Balance':<15}"
div = "=" * 80
print(header)
print(div)

for count in range(int(loan_time / 12)):
    year = count+1      # count years
   
    # Payments
    i_payment = abs(npf.ipmt(int_rate, year, year_total, balance))
    p_payment = yearly_pmnt - i_payment

    i_payments.append(i_payment)
    p_payments.append(p_payment)

    # Calculate Remaining balance
    balance -= p_payment
    
    print(f"{year:<10}{p_payment:<15,.2f}{i_payment:<15,.2f}{yearly_pmnt:<15,.2f}{balance:<15,.2f}")

    if year % 10 == 0:      # introduce a line break every 10 years.
        print()
    else:
        pass

# Footer
    
