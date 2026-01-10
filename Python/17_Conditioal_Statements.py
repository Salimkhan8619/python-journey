# This file demonstrates basic conditional statements in Python using if, elif, and else.

# Prompt the user to enter a number and convert it to an integer
a = int(input("Enter a number Here:"))

# Check if the number is greater than 18
if a > 18:
    print("a is greater than 18")
# Check if the number is less than 16
elif a < 16:
    print("a is less than 16")
# If neither condition is true, the number is between 16 and 18 inclusive
else:
    print("a is not greater than 18")

