# This script demonstrates using the 'with' statement for file handling in Python
a = "\n salim is  also good"  # The text to append, with a newline
with open("robat.txt", "a") as f:  # Open the file in append mode using 'with' for automatic closing
    f.write(a)  # Write the text to the file