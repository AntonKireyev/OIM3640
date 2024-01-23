"""Goal: Create a program to output projected weekly, monthly, and annual pay given inputs.
Givens: 50 weeks per year, $24 Hourly Wage, 40 Hours per week
"""

""" Define Variables. """

weekly_hours = 40
hourly_wage = 24
weeks_per_year = 50
weekly_pay = 0
monthly_pay = 0
annual_pay = 0
print("Your weekly hours are: "+ str(weekly_hours))
print("Your hourly wage is: $"+ str(hourly_wage))
print("Your weeks worked per year are: "+ str(weeks_per_year))

"""The purpose of this section is to create our variables for future use.
Variables that we calculate are initially set to 0.
Set variables are printed for user clarity.
"""

""" Calculations. """

print("So that means...")

# Weekly Pay
# Hours Worked Weekly * Hourly Wage
weekly_pay = weekly_hours * hourly_wage
print("Your weekly pay is: $"+ str(weekly_pay))

# Monthly Pay
# Weekly Pay * Weeks Per Month (4)
monthly_pay = weekly_pay * 4
print("Your monthly pay is: $"+ str(monthly_pay))

# Annual Pay
# To find annual pay we take the weekly rate and multiply it by the number of weeks worked in a year.
# Weekly Pay * weeks worked per year (50)
annual_pay = weekly_pay * weeks_per_year
print("Your annual pay is: $"+ str(annual_pay))

"""For each calculation take the rate and multiply it by the time.
For Weekly pay, need to know the hourly rate and the hours worked per week.
For Monthly pay, take the weekly pay and multiply it by the number of full weeks per month (4).
For Annual pay, take the weekly pay and multiply it by the number of weeks worked in a year.
"""

