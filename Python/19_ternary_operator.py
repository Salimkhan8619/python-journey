# This file demonstrates the use of the ternary operator in Python,
# which is a concise way to write conditional expressions.

# Define the age
age = 20

# Use ternary operator to determine status based on age
# Syntax: value_if_true if condition else value_if_false
status = "Adult" if age >= 18 else "Minor"
print(status)

# Traditional if-else for comparison
if age > 20:
    pass  # Do nothing if age > 20
else:
    print("Else code")  # Print message if age <= 20