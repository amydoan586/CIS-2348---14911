#Amy Doan ID: 1895125
x = input() # Input numbers
x = x.split() # Split the numbers
list = []
for i in x: # Loop to check if number meet the requirement
    if int(i) >= 0:
        list.append(int(i)) # Add the numbers to the list that meet the requirement
list.sort() # Sort the numbers in order
for n in list: # Print each number with a space
    print(n, end=" ")
