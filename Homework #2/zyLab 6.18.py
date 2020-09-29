# Amy Doan ID:1895125
First = int(input()) # User enter first integer
Second = int(input()) # User enter second integer
if First <= Second: # Second integer must be bigger than first integer
    while First <= Second:
        print(First,end=" ")
        First += 10
    print("")
else: # When Second integer is not bigger than first integer
    print("Second integer can't be less than the first.")
