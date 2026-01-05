items = ["apple", "banana ", "orange"]  # Define a list of items
print (len(items))  # Print length of items list (3)
items.append("strawberries")  # Add "strawberries" to the end
items.insert(1,"strawberries")  # Insert "strawberries" at index 1
items.extend(["more bananas" ,"pineapples"])  # Extend list with another list
items.append(["more bananas" ,"pineapples"])  # Append a list as a single element
items.remove("apple")  # Remove first occurrence of "apple"
items.pop(1)  # Remove element at index 1
items[0] = "grapes"  # Change first element to "grapes"


print(items.index("orange"))  # Print index of "orange"
print(items.count("orange"))  # Print count of "orange"


print(items)  # Print the modified items list
numbers =[11,55,8,5,66,3,66,4,]  # Define a list of numbers
numbers.sort()  # Sort numbers in ascending order
numbers.sort(reverse=True)  # Sort numbers in descending order
print(numbers)  # Print sorted numbers
print(11 in numbers)  # Check if 11 is in numbers (True)

# items.clear()  # Commented out: would clear the list