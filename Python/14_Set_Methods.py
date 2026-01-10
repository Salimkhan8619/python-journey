# This file demonstrates various methods available for sets in Python.

# Create a set with initial items
items = {"apple ", "banana", "tomato"}
# Add a single item to the set
items.add("orange")
# Print the set after adding
print(items)

# Update the set with multiple items from another set
items.update({"mango", "Peach"})
# Print the set after updating
print(items)
# Remove a specific item (raises KeyError if not found)
items.remove("banana")
# Print the set after removing
print(items)
# Discard a specific item (no error if not found)
items.discard("tomatossssss")
# Print the set after discarding
print(items)

# Pop a random item from the set
a = items.pop()
# Print the popped item
print(a)

# Define two sets for set operations
b = {1, 2, 3, 6}
c = {4, 3, 5, 6}
# Compute the union of sets b and c
result = b.union(c)
# Print the union result
print(result)
# Compute the intersection of sets b and c
result = b.intersection(c)
# Print the intersection result
print(result)