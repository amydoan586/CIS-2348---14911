#Amy Doan ID:1895125
Lemon_Amount = float(input("Enter amount of lemon juice (in cups):\n")) #User is asked to input Lemon amount in cups
Water_Amount = float(input("Enter amount of water (in cups):\n")) #User is asked to input water amount in cups
Nectar_Amount = float(input("Enter amount of agave nectar (in cups):\n")) #User is asked to input agave nectar amount in cups
Servings = float(input("How many servings does this make?\n")) #User is asked to input serving
print()
print("Lemonade ingredients - yields", '{:.2f}'.format(Servings),"servings") #Number is converted with 2 decimals
print('{:.2f}'.format(Lemon_Amount), "cup(s) lemon juice")
print('{:.2f}'.format(Water_Amount), "cup(s) water")
print('{:.2f}'.format(Nectar_Amount), "cup(s) agave nectar\n")
Asked_Servings = float(input("How many servings would you like to make?\n")) #User is asked to input how many servings
print()
Lemon_Amount = Lemon_Amount * (Asked_Servings/Servings) #Program takes Asked_serving and divide with serving to get hpw much is needed to multiple with Lemon_Amount
Water_Amount = Water_Amount * (Asked_Servings/Servings) #Program takes Asked_serving and divide with serving to get hpw much is needed to multiple with Water_Amount
Nectar_Amount = Nectar_Amount * (Asked_Servings/Servings) #Program takes Asked_serving and divide with serving to get hpw much is needed to multiple with Nectar_Amount
print("Lemonade ingredients - yields", '{:.2f}'.format(Asked_Servings),"servings")
print('{:.2f}'.format(Lemon_Amount), "cup(s) lemon juice")
print('{:.2f}'.format(Water_Amount), "cup(s) water")
print('{:.2f}'.format(Nectar_Amount), "cup(s) agave nectar\n")
Lemon_Amount = Lemon_Amount /16 #Lemon_Amount is divided by 16 to convert cups to gallons
Water_Amount = Water_Amount /16 #Water_Amount is divided by 16 to convert cups to gallons
Nectar_Amount = Nectar_Amount /16 #Nectar_Amount is divided by 16 to convert cups to gallons
print("Lemonade ingredients - yields", '{:.2f}'.format(Asked_Servings),"servings")
print('{:.2f}'.format(Lemon_Amount), "gallon(s) lemon juice")
print('{:.2f}'.format(Water_Amount), "gallon(s) water")
print('{:.2f}'.format(Nectar_Amount), "gallon(s) agave nectar")