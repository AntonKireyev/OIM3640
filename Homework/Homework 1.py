''' Gold Dollar Price Equivalent Calculator

Author: Anton Kireyev
File Created: 1/27/2024

Convert weight of gold in pounds and ounces to grams and kilograms, then calculate the price.
User enters the number of pounds and ounces. Output the total weight in grams and kilograms, the total value, and unit prices
1 ounce = 28.35 grams, 1 pound = 453.59 grams, Sample Run: Assumes SPOT price of gold is $1868.40 per ounce
'''

# Get Variables
pounds = float(input("How many pounds? "))
ounces = float(input("How many ounces? "))

grams = (pounds * 453.59) + (ounces * 28.35)
kilograms = grams / 1000

# Use Symbolic constants - defines cost per ounce and per gram.
OUNCE_COST = 1868.4
GRAM_COST = OUNCE_COST / 28.35

total_ounces = grams / 28.35
total_cost = GRAM_COST * grams

# Output
print(f"\n" f"The total weight is {grams:.2f} grams ({kilograms:.2f} kilograms).")      # Use f"\n" to push text to new line
print(f"The total cost of {total_ounces:.1f} ounces of gold is ${total_cost:.2f}")
print(f"\n" f"Cost per ounce: ${OUNCE_COST:.1f}")
print(f"Cost per gram: ${GRAM_COST:.1f}")