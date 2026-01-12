# This script demonstrates how to append text to a file in Python
a = "salim khan is also good "  # The text to append
file = open("robot.txt", "a")  # Open the file in append mode
file.write(a)  # Write the text to the file
file.close()  # Close the file