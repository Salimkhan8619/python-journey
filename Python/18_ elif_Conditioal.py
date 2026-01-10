# This file demonstrates the use of elif (else if) conditional statements in Python,
# allowing multiple conditions to be checked in sequence.

# Define the score
score = 63

# Check the grade based on score ranges using if-elif-else
if score >= 80:
    print("Grade A")
elif score >= 70:
    print("Grade B")
elif score >= 60:
    print("Grade C")
elif score >= 50:
    print("Grade D")
else:
    print("Fail")

# Check if the score is even or odd using modulo operator
if score % 2 == 0:
    print("Score is even!")
else:
    print("Score is odd!")
