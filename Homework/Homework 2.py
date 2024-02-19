# Amortization Schedule Calculator

# Libraries
import numpy_financial as npf
import math

# Variables / Inputs
i_total = list()
p_total = list()
DIV = "-" * 54

# Sample / manual selector
print("Welcome to the Loan Amortizer\nPlease enter S for sample report or C to enter new parameters")
mode = input("[S]ample or [C]ustom Input: ")       # Mode Selector
while mode not in "SCsc":
    mode = input("Error! Type [S] or [C]:  ")

timescale = input("[M]onthly or [A]nnual Report: ")        # Annual/Monthly timescale Selector
while timescale not in "AMam":
    timescale = input("Error! Type [M] or [A]:  ")

print(DIV)

# Sample/Custom Mode Selector
if mode in "Ss":
    balance = 360000        # In Dollars
    user_loan_time = 10         # In Years
    user_int_percent = 5.00       # Annual Rate in %
    monthly_pmnt = npf.pmt(user_int_percent/1200, user_loan_time, -balance)   # Monthly payment in Dollars

if mode in "Cc":
    balance = input("Loan Amount: $")
    while True:
        if balance.isnumeric():
            break
        else:
            balance = input("Error! Enter valid loan amount: $")
    balance = float(balance)

    user_loan_time = input("Loan length in years (between 10-40): ")
    while True:
        if user_loan_time.isnumeric() and int(user_loan_time) >= 10 and int(user_loan_time) <= 40:
            break
        else:
            user_loan_time = input("Error! Please enter a number of years between 10 and 40: ")
    user_loan_time = int(user_loan_time)

    user_int_percent = input("Annual Interest Rate: ")
    while True:
        if user_int_percent.replace(".","").isnumeric() and float(user_int_percent) >= 0:
            break
        else:
            user_int_percent = input("Error! Please enter a positive annual interest rate: ")
    user_int_percent = float(user_int_percent)

    monthly_pmnt = npf.pmt(user_int_percent/1200, user_loan_time, -balance)   # Monthly payment in Dollars

intro = f"{'Balance:':<28}${balance:>15,.2f}\n{'Length of Loan in Months:':<28}{user_loan_time:>16,.0f}\n{'Annual interest Rate:':<28}{user_int_percent:>15,.2f}%\n{'Monthly Payment:':<28}${monthly_pmnt:>15,.2f}"
print(intro)
print(DIV)

# Annual/Monthly Period Data Selector
if timescale in "Mm":
    int_rate = user_int_percent / 1200
    term = user_loan_time * 12
    period_pmnt = monthly_pmnt
    time_desc = 'Months'

if timescale in "Aa":
    term = user_loan_time
    int_rate = user_int_percent / 100
    period_pmnt = monthly_pmnt * 12
    time_desc = 'Years'

# Payment Amounts
header = f"{time_desc:<10}{'Principal':<15}{'Interest':<15}{'Payment':<15}{'Total Principal Paid':<15}"
print(header)
print(DIV)

for period in (range(1, int(term)+1)):
    # Payments
    i_payment = npf.ipmt(int_rate, period, term, -balance)
    p_payment = npf.ppmt(int_rate, period, term, -balance)
    i_total.append(i_payment)
    p_total.append(p_payment)

    if timescale in "Aa":
        if period % 10 == 1 and period > 1:      # introduce a line break after every 10 years.
            print()

    if timescale in "Mm":
        if period % 12 == 1:        # Introduce a year counter/divider after every 12 months.
            print(f"{'-'*20}{'Year: '}{int((period/12)+1)}{'-'*20}")

    # Print period information
    print(f"{period:<10}{p_payment:<15,.2f}{i_payment:<15,.2f}{p_payment + i_payment:<15,.2f}{sum(p_total):<15,.2f}")

# Footer
footer = f"{'Total:':<9}$ {sum(p_total):<13,.2f}$ {sum(i_total):<13,.2f}$ {sum(i_total) + sum(p_total):<13,.2f}"
print(DIV)
print(footer)

principal_paid = 0
for index in range(1, len(p_total)+1):
    principal_paid += p_total[index]
    if principal_paid >= math.ceil(balance/2):
        print(f"\nThe principal is half paid off after {index:.0f} {time_desc.lower()}!")
        break
