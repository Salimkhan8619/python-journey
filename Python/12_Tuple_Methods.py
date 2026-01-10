# This file demonstrates methods and operations available for tuples in Python.

# Define a tuple of items
items = ("apple", "banana ", "orange")
# Print the last element using negative indexing
print(items[-1])  # Output: "orange"

# Print the length of the tuple
print(len(items))  # Output: 3
# Print the count of "apple" in the tuple
print(items.count("apple"))  # Output: 1
# Print the index of "apple" in the tuple
print(items.index("apple"))  # Output: 0
# Convert tuple to list
list_1 = list(items)
# Print the converted list
print(list_1)