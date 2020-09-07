#Amy Doan ID:1895125
print("Birthday Calculator")
print("Current Day") #User is asked to input current month,day, and year
C_Month = int(input("Month: "))
C_Day = int(input("Day: "))
C_Year = int(input("Year: "))
print("Birthday") #User is asked to to input birth moneth,day and year
B_Month = int(input("Month: "))
B_Day = int(input("Day: "))
B_Year = int(input("Year: "))
if B_Month < C_Month: #Current month is greater than birth month
    Age = C_Year - B_Year #If birthday is passed, birth year is subtracted from current year to get age
    print("You are", Age, "years old.")
elif B_Month == C_Month: #If current month and birth month is the same
    if B_Day <= C_Day: #If birthday is passed, birth year is subtracted from current year to get age
        Age = C_Year - B_Year
        print("You are", Age, "years old.")
    else: #If birthday has not passed, birth year is subtracted from current year (age after birthday) and minus 1 to get current age before birthday
        Age = (C_Year - B_Year) - 1
        print("You are", Age, "years old.")
else:
    Age =( C_Year - B_Year) - 1
    print("You are", Age, "years old.")
if B_Month == C_Month and B_Day == C_Day: #If current month and day is the same as birthday
    print("Happy Birthday!")