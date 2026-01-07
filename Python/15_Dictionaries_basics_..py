# Dictionary Basics Demonstration

student={
    "name":"salimkhan",
    "city":"jaipur",
    "company":"Ssc ",
}

# Accessing and printing the value of the 'name' key
print(student ["name"])
# Accessing and printing the value of the 'company' key
print(student ["company"])
# Accessing and printing the value of the 'city' key
print(student ["city"])

# Using get() method to access a non-existent key (returns None)
print(student.get("nameeee"))
# Using get() method to access an existing key
print(student.get("name"))

# Modifying the value of the 'city' key
student["city"]="jewali"
# Printing the entire dictionary after modification
print(student)
