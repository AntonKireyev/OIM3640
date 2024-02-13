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
i_payments = 0
p_payments = 0
DIV = "-" * 80


# Sample / manual selector
print("Welcome to the Loan Amortizer \n")
mode = input("[S]ample or [M]anual Input: ")       # Mode Selector
while mode not in "SMsm":
    mode = input("[S]ample or [M]anual Input: ")

timescale = input("[M]onthly or [A]nnual Report: ")        # Annual/Monthly Selector
while timescale not in "AMam":
    timescale = input("[M]onthly or [A]nnual Report: ")

# Sample/Manual Mode Selector

if mode == "S":
    balance = 360000   # In Dollars
    loan_time = 360     # In Months
    int_percent = 2.4       # Annual Rate in %
    monthly_pmnt = 2000    # Monthly payment in Dollars
    intro = f"{'Balance:':<28}${balance:>15,.2f}\n{'Length of Loan in Months:':<28}{loan_time:>15,}\n{'Annual interest Rate:':<28}{int_percent:>15,.2f}\n{'Monthly Payment:':<28}${monthly_pmnt:>15,.2f}\n"
    print(intro)

if mode == "M":
    balance = float(input("Balance: "))
    loan_time = float(input("Loan length in months: "))
    int_percent = float(input("Annual Interest Rate: "))
    monthly_pmnt = float(input("Monthly Payment: "))

# Annual/Monthly Period Selector

if timescale == "M":
    int_rate = int_percent / 1200
    time = loan_time
    period_pmnt = monthly_pmnt

if timescale == "A":
    time = loan_time / 12
    int_rate = int_percent / 100
    period_pmnt = monthly_pmnt * 12

# Payment Amounts
header = f"{'Year':<10}{'Principal':<15}{'Interest':<15}{'Payment':<15}{'Remaining Balance':<15}"
print(header)
print(DIV)

for period in range(int(time)+1):
    # Payments
    i_payment = abs(npf.ipmt(int_rate, period, time, balance))
    p_payment = period_pmnt - i_payment
    i_payments += i_payment
    p_payments += p_payment

    if period % 10 == 0:      # introduce a line break every 10 years.
        print()

    if balance <= p_payment:
        p_payment = balance
        period_pmnt = p_payment + i_payment

    # Calculate Remaining balance
    balance -= p_payment
    print(f"{period:<10}{p_payment:<15,.2f}{i_payment:<15,.2f}{period_pmnt:<15,.2f}{balance:<15,.2f}")

    if balance <= 0:
        break
# Footer
footer = f"{'Total:':<9}$ {p_payments:<13,.2f}$ {i_payments:<13,.2f}$ {i_payments + p_payments:<13,.2f}"
print(DIV)
print(footer)