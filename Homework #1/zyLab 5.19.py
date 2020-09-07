#Amy Doan ID:1895125
print("Davy's auto shop services") #Menu Display
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12")
print()
First_Service = input("Select first service:\n") #User inputs first service
Second_Service = input("Select second service:\n") #User inputs second service
print()
print("Davy's auto shop invoice\n")
if First_Service == "Oil change": #If statements to find the first service to calculate total
    print("Service 1:", First_Service + ", $35")
    Service_Price1 = 35 #Assign price for first service
if First_Service == "Tire rotation":
    print("Service 1:", First_Service + ", $19")
    Service_Price1 = 19
if First_Service == "Car wash":
    print("Service 1:", First_Service + ", $7")
    Service_Price1 = 7
if First_Service == "Car wax":
    print("Service 1:", First_Service + ", $12")
    Service_Price1 = 12
if First_Service == "-":
    print("Service 1: No service")
    Service_Price1 = 0
if Second_Service == "Oil change": #If statements to find the second service to calculate total
    print("Service 2:", Second_Service + ", $35\n")
    Service_Price2 = 35 #Assign price for second service
if Second_Service == "Tire rotation":
    print("Service 2:", Second_Service +", $19\n")
    Service_Price2 = 19
if Second_Service == "Car wash":
    print("Service 2:", Second_Service + ", $7\n")
    Service_Price2 = 7
if Second_Service == "Car wax":
    print("Service 2:", Second_Service + ", $12\n")
    Service_Price2 = 12
if Second_Service == "-":
    print("Service 2: No service\n")
    Service_Price2 = 0
Total = int(Service_Price1 + Service_Price2) #Calculate Total for both service
print("Total: $" + str(Total))