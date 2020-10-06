#Amy Doan ID:1895125
import csv
frequent = {} #List of frequents
file_name = input()
with open(file_name,'r') as csvfile:
    my_file = csv.reader(csvfile)
    for line in my_file: # Loop words
        for word in line: # Loop how many there are
            if word not in frequent:
                frequent[word] = 1
            else:
                frequent[word] += 1
for word in frequent: # Print how many the words repeated
    print(word + " " + str(frequent[word]))