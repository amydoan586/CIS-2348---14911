import math
Height = int(input("Enter wall height (feet):\n"))
Width = int(input("Enter wall width (feet):\n"))
Wall_Area = Height * Width
print("Wall area:", Wall_Area, "square feet")
Paint_Needed = Wall_Area/350
print("Paint needed:",'{:.2f}'.format(Paint_Needed),"gallons")
Cans = math.ceil(Paint_Needed/1)
print("Cans needed:",Cans, "can(s)\n")
Color = input("Choose a color to paint the wall:\n")
if Color == "red":
    Cost = Cans * 35
    print("Cost of purchasing", Color, "paint: $"+ str(Cost))
if Color == "blue":
    Cost = Cans * 25
    print("Cost of purchasing", Color, "paint: $",str(Cost))
if Color == "green":
    Cost = Cans * 23
    print("Cost of purchasing", Color, "paint: $",str(Cost))

