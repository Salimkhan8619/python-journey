# List of items
items=["apples", 34, "bananas", "oranges"]

# Loop through each item in the list and print it
for item in items:
    print(item)

    # Nested loop: print even numbers from 0 to 100
    for i in range(0,100,2):

        print(i)

# Loop through each character in the string "Salim"
for Name in "Salim":
    print(Name)


# While loop: print numbers from 1 to 5
count=1
while count<=5:
    print(count)
    count+=1

# For loop with break: print numbers until we reach 9
for i in range (10):
        if (i==9):
         break
        print(i)
        

# For loop with continue: skip the number 11 and print all numbers from 0 to 24
for a in range(25):
    if (a==11):
        continue
    print(a)