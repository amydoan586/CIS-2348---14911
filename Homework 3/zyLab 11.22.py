#Amy Doan ID:1895125
frequent = {} # Dictionart
list = input() # Input words
list = list.split() # Split the words
for line in list: # Loop each words to see the frequents
    if line in frequent:
        frequent[line] += 1
    else:
        frequent[line] = 1
for word in list: # Print how many the words repeated
    print(word + " " + str(frequent[word]))