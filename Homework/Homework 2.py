# Amortization Schedule Calculator

# Import Libraries
import numpy_financial as npf

# Variables / Inputs
i_total = 0
p_total = 0
DIV = "-" * 54

# Sample / manual selector
print("Welcome to the Loan Amortizer \n Please enter S for sample report or C to enter new parameters")
mode = input("[S]ample or [C]ustom Input: ")       # Mode Selector
while mode not in "SCsc":
    mode = input("Error. Type [S] or [C]:  ")

timescale = input("[M]onthly or [A]nnual Report: ")        # Annual/Monthly Selector
while timescale not in "AMam":
    timescale = input("Error. Type [M] or [A]:  ")

print(DIV)

# Sample/Custom Mode Selector
if mode in "Ss":
    balance = 360000        # In Dollars
    loan_time = 360         # In Months
    int_percent = 5       # Annual Rate in %
    monthly_pmnt = 2129.54    # Monthly payment in Dollars
    intro = f"{'Balance:':<28}${balance:>15,.2f}\n{'Length of Loan in Months:':<28}{loan_time:>15,}\n{'Annual interest Rate:':<28}{int_percent:>15,.2f}%\n{'Monthly Payment:':<28}${monthly_pmnt:>15,.2f}"
    print(intro)

if mode in "Cc":
    balance = float(input("Balance: $"))
    loan_time = float(input("Loan length in years: ")*12)
    int_percent = float(input("Annual Interest Rate: "))
    monthly_pmnt = float(input("Monthly Payment: $"))

print(DIV)

# Annual/Monthly Period Selector
if timescale in "Mm":
    int_rate = int_percent / 1200
    time = loan_time
    period_pmnt = monthly_pmnt
    time_desc = 'Months'

if timescale in "Aa":
    time = loan_time / 12
    int_rate = int_percent / 100
    period_pmnt = monthly_pmnt * 12
    time_desc = 'Years'

# Payment Amounts
header = f"{time_desc:<10}{'Principal':<15}{'Interest':<15}{'Payment':<15}{'Remaining Balance':<15}"
print(header)
print(DIV)

time = int(time)

for period in (range(1, time)):
    # Payments
    i_payment = abs(npf.ipmt(int_rate, period, time, balance))
    p_payment = period_pmnt - i_payment
    i_total += i_payment
    p_total += p_payment

    if timescale in "Aa":
        if period % 10 == 1 and period > 1:      # introduce a line break after every 10 years.
            print()

    if timescale in "Mm":
        if period % 12 == 1:
            print(f"{'-'*20}{'Year: '}{int((period/12)+1)}{'-'*20}")

    if balance <= p_payment:
        p_payment = balance
        period_pmnt = p_payment + i_payment

    # Calculate Remaining balance
    balance -= p_payment
    print(f"{period:<10}{p_payment:<15,.2f}{i_payment:<15,.2f}{period_pmnt:<15,.2f}{balance:<15,.2f}")

    if balance <= 0:
        break
# Footer
footer = f"{'Total:':<9}$ {p_total:<13,.2f}$ {i_total:<13,.2f}$ {i_total + p_total:<13,.2f}"
print(DIV)
print(footer)

half_life = (period / 2) * 12
print(half_life)