#Amy Doan ID:1895125
import math #Add math functions
Height = int(input("Enter wall height (feet):\n")) #User is asked to input height
Width = int(input("Enter wall width (feet):\n")) #User is asked to input width
Wall_Area = Height * Width #Calculate area of given height and width
print("Wall area:", Wall_Area, "square feet")
Paint_Needed = Wall_Area/350 #Area is divided by 130 to get paint needed
print("Paint needed:",'{:.2f}'.format(Paint_Needed),"gallons") #Two decimal places is needed for Paint_Needed
Cans = math.ceil(Paint_Needed/1) #Calucating how many cans is needed and is rounded up to an integer
print("Cans needed:",Cans, "can(s)\n")
Color = input("Choose a color to paint the wall:\n") #User is asked to input color
if Color == "red": #Using if statements to calculate cost for red, blue, or green
    Cost = Cans * 35
    print("Cost of purchasing", Color, "paint: $"+ str(Cost))
if Color == "blue":
    Cost = Cans * 25
    print("Cost of purchasing", Color, "paint: $"+ str(Cost))
if Color == "green":
    Cost = Cans * 23
    print("Cost of purchasing", Color, "paint: $"+ str(Cost))

