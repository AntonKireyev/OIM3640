"""Goal: Create a program to output projected weekly, monthly, and annual pay given inputs.
Givens: 50 weeks per year, $24 Hourly Wage, 40 Hours per week
"""
# Variables
weekly_hours = 40
hourly_wage = 24
weeks_per_year = 50
print("Your weekly hours are: " + str(weekly_hours))
print("Your hourly wage is: $" + str(hourly_wage))
print("Your weeks worked per year are: " + str(weeks_per_year))

"""Defined variables for future use.
Preseet variables are displayed to users.
"""

# Calculations
print("So that means...")

# Weekly Pay
# Weekly Hours * Hourly Wages
weekly_pay = weekly_hours * hourly_wage
print("Your weekly pay is: $" + str(weekly_pay))

# Annual Pay
# Weekly Pay * weeks worked per year (50)
annual_pay = weekly_pay * weeks_per_year
''' Finds annual pay by multiplying weekly pay and the number of weeks worked in the year'''
print("Your annual pay is: $" + str(annual_pay))

# Monthly Pay
# Weekly Pay / annual pay
monthly_pay = annual_pay / 12
print("Your monthly pay is: $" + str(monthly_pay))


"""For each calculation take the rate and multiply it by the time.
This section calculates the weekly, monthly, and annual pay, then displays it for the user.
"""
