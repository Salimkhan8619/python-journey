# File: 06_Operators.py
# This file demonstrates various operators in Python.
# Operators are symbols that perform operations on variables and values.
# Python supports arithmetic, comparison, assignment, logical, and other types of operators.

# Assignment Operator
a = 10  # Assigns the value 10 to variable a
b = 3   # Assigns the value 3 to variable b

# Arithmetic Operators
# These perform mathematical operations
print(a + b)  # Addition: 10 + 3 = 13
print(a - b)  # Subtraction: 10 - 3 = 7
print(a * b)  # Multiplication: 10 * 3 = 30
print(a / b)  # Division: 10 / 3 = 3.333...
print(a // b) # Floor Division: 10 // 3 = 3
print(a % b)  # Modulus: 10 % 3 = 1
print(a ** b) # Exponentiation: 10 ** 3 = 1000

# Comparison Operators
# These compare two values and return True or False
print(a == b) # Equal to: 10 == 3 → False
print(a != b) # Not equal to: 10 != 3 → True
print(a > b)  # Greater than: 10 > 3 → True
print(a < b)  # Less than: 10 < 3 → False
print(a >= b) # Greater than or equal to: 10 >= 3 → True
print(a <= b) # Less than or equal to: 10 <= 3 → False

# Assignment Operators with operations
a = 5  # Reassign a to 5
print(a)  # Prints 5

a += 5  # Equivalent to a = a + 5 → a = 5 + 5 = 10
print(a)  # Prints 10

a -= 3  # Equivalent to a = a - 3 → a = 10 - 3 = 7
print(a)  # Prints 7

a *= 2  # Equivalent to a = a * 2 → a = 7 * 2 = 14
print(a)  # Prints 14

a /= 3  # Equivalent to a = a / 3 → a = 14 / 3 = 4.666...
print(a)  # Prints 4.666...

a %= 2  # Equivalent to a = a % 2 → a = 4.666 % 2 = 0.666...
print(a)  # Prints 0.666...

a //= 2 # Equivalent to a = a // 2 → a = 0.666 // 2 = 0.0
print(a)  # Prints 0.0

a **= 2 # Equivalent to a = a ** 2 → a = 0.0 ** 2 = 0.0
print(a)  # Prints 0.0

# Additional Assignment Operation
a += 3  # Equivalent to a = a + 3 → a = 0.0 + 3 = 3.0
print(a)  # Prints 3.0

# Logical Operators
# These perform logical operations and return True or False
print(False and True)   # AND: False and True → False
print(True and False)   # AND: True and False → False
print(False or True)    # OR: False or True → True
print(True or False)    # OR: True or False → True
print(not(True))        # NOT: not True → False
print(not(False))       # NOT: not False → True
