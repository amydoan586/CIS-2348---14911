#Amy Doan ID: 1895125
Team ={}
for i in range(1,6): # Let user input jersey and rating 5 times
    Jersey = int(input("Enter player " + str(i) + "'s jersey number:\n"))
    Rating = int(input("Enter player " + str(i) + "'s rating:\n"))
    Team.update({Jersey: Rating}) # Update into Team dictionary
    print()
print("ROSTER")
for i in sorted(Team.keys()): # Loop to sort in order by jersey number
    print("Jersey number:",str(i) + "," + " Rating:",Team[i])
print()
while True: #Loop until it is false
    print("MENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")
    print()
    x = input("Choose an option:\n") # Input an option
    if x == 'o': # Output roster
        print("ROSTER")
        for i in sorted(Team.keys()):
            print("Jersey number:", str(i) + "," + " Rating:", Team[i])
        print()
    if x == 'a': # Add player
        Jersey = int(input("Enter a new player's jersey number:\n"))
        Rating = int(input("Enter a new player's rating:\n"))
        Team[Jersey] = Rating
        print()
    if x == 'd': # Remove player
        remove = int(input("Enter a jersey number:\n"))
        del Team[remove]
        print()
    if x == 'u': # Update player rating
        Jersey = int(input("Enter a new player's jersey number:"))
        Rating = int(input("Enter a new rating for player:\n"))
        Team.update({Jersey: Rating})
        print()
    if x == 'r': #Output player rating that is above the input number
        Above = int(input("Enter a rating:\n"))
        print()
        print("ABOVE",Above)
        for i in sorted(Team.keys()): # Loop in the dictionary when the rating is above the input number
            if Team[i] > Above:
                print("Jersey number:", str(i) + "," + " Rating:", Team[i])
        print()
    if x == 'q': # Quit
        exit()

