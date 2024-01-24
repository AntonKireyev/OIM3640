# Ticket sales calculator
ticket_price = float(input("What is the ticket price?"))
ticket_quantity = int(input("How many tickets?"))
state_tax = 0.0625
city_tax = 0.075

# Calculate Outputs
taxable = ticket_price * ticket_quantity
total_state_tax = float(state_tax * taxable)
print(f"Your total state tax is {total_state_tax}")
total_city_tax = float(city_tax * taxable)
print(f"Your total city tax is {total_city_tax}")

# Total Ticket Cost
total_cost = taxable + total_state_tax + total_city_tax
print(f"Your total cost is {total_cost}")


#old ways to print
print("Ticket cost: %15.2f" %(total_cost))
print("{:15s}{:15.2f}".format('State Tax:', total_state_tax))

# F string
print(f"City tax {total_city_tax:15,.2f}")
