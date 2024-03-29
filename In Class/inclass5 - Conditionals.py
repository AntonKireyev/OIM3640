''' If Code Block
Code in an if block only runs if something is True
True is anything that is not 0
It may be best to write a comparison'''

if True: 
    print("Do This")

# testing for any user input
value = input("enter something")

if value != "0" and value:
    print("Do this")

print("this happens anyway")

for value in range(-3,3):
    if value:
        print(value)

# Comparison operators: >, >=, <, <=, ==, !=
# If... else... (One of the blocks runs)

value = input ("enter something")
if value:
    print("do this")
else:
    print("do that")

print("this happens anyway")


# if... elif... (else)
# Used when selection is non-binary, best practice is to use else as a catch-all

value = input("enter any number: ")
if value[0].isnumeric() or value[0] == "-":     # testing to see if the first digit is numeric
    value = float(value)
    if value > 0:
        print("That's Positive!")
    elif value < 0:
        print("That's negative!")
    elif value == 0:
        print("That's ZERO!")
else:
    print("That's not a number!")


# Changing Iteration
# Continue, break, Pass

for vowel in 'aeiou':
    print(vowel)

value = input('enter a vowel')
if value in 'aeiou':
    print("that's a vowel")
print("goodbye!")

value = input('enter a vowel')
if value.lower() in 'aeiou':        # use .lower() to account for uppercase
    print("that's a vowel")
print("goodbye!")

for value in range(10):
    if value % 3:
        print(value)
    else:
        continue        # Continue - skips an iteration of the loop

for value in range(10):
    if value % 3:
        continue
    else:
        print(value)

for value in range(10):
    if value % 3:
        break           # Break kills the loop
    else:
        print(value)

if True:
    pass                # placeholder 
else:
    pass

