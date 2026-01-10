# This file demonstrates various aspects of functions in Python,
# including function definitions, parameters, default arguments, keyword arguments, and lambda functions.

def greet(fname, lname):
    """
    Greets a person with their first and last name.

    Args:
        fname (str): First name of the person.
        lname (str): Last name of the person.
    """
    print("Good Morning!", fname, lname)
    print("How are you!")
    print("Thank you!")

# Calling the greet function with different names
greet("salim", "Khan")
greet("Khushi", "Mohammad")

def add(a, b):
    """
    Adds two numbers and returns the result.
    Note: The print statement is commented out, so this function returns None.

    Args:
        a (int or float): First number.
        b (int or float): Second number.

    Returns:
        None: Since the return statement is missing.
    """
    # print(a + b)  # This line is commented out

# Calling add function and printing the result (which is None)
c = add(5, 4)
print(c)

def greet(name="User"):
    """
    Greets a person with a default name if none is provided.

    Args:
        name (str): Name of the person to greet. Defaults to "User".
    """
    print("Hello", name)

# Calling greet with default and custom name
greet()
greet("salim")

def greet(name="", City="Sikar"):
    """
    Greets a person with their name and city, using default values.

    Args:
        name (str): Name of the person. Defaults to empty string.
        City (str): City of the person. Defaults to "Sikar".
    """
    print("Hello", name, City)

# Calling greet with keyword arguments
greet(City="sikar", name="salim")

# Lambda function for addition
add = lambda ab, cd: ab + cd
print(add(5, 7))