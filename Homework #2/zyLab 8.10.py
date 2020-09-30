#Amy Doan ID:1895125
string = str(input()) # User input string
if string == string[::-1]: # Compare string with reverse string
    print(string,"is a palindrome")
else:
    print(string,"is not a palindrome")