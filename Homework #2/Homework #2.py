#Amy Doan ID:1895125
month_list = {"January" : "1", "February" : "2", "March" : "3", "April" : "4", "May" : "5", "June" : "6", "July" : "7", "August" : "8", "September" : "9", "October" : "10", "November" : "11", "December" : "12"} # List of the month
dates = ""
date_list =[]
while dates != "-1":
    dates = input() # User input dates until -1
    date_list.append(dates) # Adds to date_list
print(date_list)
for dates in date_list: #Loop dates from the date_list
    date_parse = dates.find(',') #Finding dates that contains ,
    date_period = dates.find('.') #Finding dates with period
    if date_parse != -1 and date_period == -1: # True if there is a comma and no period
        dates = dates.split() # Splits into 3 part
        dates[1] = dates[1].replace(',','/') #replacing comma with /
        dates = month_list[dates[0]] + '/' + dates[1] + dates[2] # Adding month, day and yea with /
        print(dates)
