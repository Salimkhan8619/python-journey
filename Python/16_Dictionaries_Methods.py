# This file demonstrates various methods available for dictionaries in Python.

# Create a dictionary with student information
student = {
    "name": "salim",
    "City": "Delhi",
    "Company": "GTM",
}

# Remove the 'name' key from the dictionary using pop()
student.pop("name")
print(student)

# Add a new key 'Calls' with value '12th' to the dictionary
student["Calls"] = "12th"
print(student)

# Remove the last item from the dictionary using popitem()
student.popitem()
print(student)

# Delete the 'City' key from the dictionary using del statement
del student["City"]

# Clear all items from the dictionary
student.clear()

# Print the keys of the dictionary (empty after clear)
print(student.keys())
# Print the values of the dictionary (empty after clear)
print(student.values())
# Print the items of the dictionary (empty after clear)
print(student.items())
# Print the entire dictionary (empty after clear)
print(student)