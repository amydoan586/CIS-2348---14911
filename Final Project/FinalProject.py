# Amy Doan ID: 1895125
import csv
from datetime import date
ManufacturerDict = {}
class Inventory: # Class Inventory
    def __init__(self,Manfacturer = "none", ItemType = "none"):
        self.Manufacturer = Manfacturer
        self.ItemType = ItemType
    def Manufacturer_List(self): # Create a Manufacturer List
        with open("ManufacturerList.csv", 'r') as ManufacturerList:
            Brand = csv.reader(ManufacturerList)
            for Manufacturer in Brand: # Loop to create a dictionary
                ManufacturerDict[Manufacturer[0]] = [Manufacturer[1],Manufacturer[2],Manufacturer[3]]
            return ManufacturerDict
    def Price_List(self): # Add price to manufacturer dicitonary
        PriceDict = {}
        with open("PriceList.csv",'r') as PriceList:
            Price = csv.reader(PriceList)
            for ItemPrice in Price: # Assign the Price to the ID
                PriceDict[ItemPrice[0]] = [ItemPrice[1]]
            for item in ManufacturerDict: # Loop to add prices to the same ID in the dictionary
                if item in PriceDict:
                    ManufacturerDict[item] += PriceDict[item]
            return ManufacturerDict
    def Service_Dates_List(self): # Add service dates to the manufacturer dictionary
        DatesDict = {}
        with open("ServiceDatesList.csv",'r') as ServiceDate:
            Dates = csv.reader(ServiceDate)
            for ItemDate in Dates: # Assign the dates to the ID
                DatesDict[ItemDate[0]] = [ItemDate[1]]
            for item in ManufacturerDict: # Loop to add dates to the same ID in the dictionary
                if item in DatesDict:
                    ManufacturerDict[item] += DatesDict[item]
            return ManufacturerDict
    def Full_Inventory(self): # Create a Full Inventory file with the dictionary
        with open("FullInventory.csv",'w') as OutputFile:
            Inventory = csv.writer(OutputFile)
            for ID, Info in sorted(ManufacturerDict.items(), key = lambda x:x[1]): # Sort by type and loop to output a csv file
                Inventory.writerow([ID, Info[0],Info[1],Info[3],Info[4],Info[2]])
    def Laptop_Inventory(self): # Create Laptop Inventory csv file with the dictionary
        with open("LaptopInventory.csv",'w') as OutputFile:
            Laptop = csv.writer(OutputFile)
            for ID, Info in sorted(ManufacturerDict.items(),key = lambda x:x[0]): # Sort by ID and loop to output a csv file
                if Info[1] == "laptop":
                    Laptop.writerow([ID,Info[0],Info[3],Info[4],Info[2]])
    def Past_Service_Date(self): # Create Past Service Date file with the dictionary
        Current_Date = str(date.today()) # Assign current date
        Current_Date = Current_Date.split('-') # Create a list with the date
        with open("PastServiceDateInventory.csv",'w') as OutputFile:
            PastDate = csv.writer(OutputFile)
            for ID, Info in sorted(ManufacturerDict.items()):
                Past_Date = Info[4]
                Past_Date = Past_Date.split('/') # Split and create a list for past dates
                if int(Current_Date[0]) >= int(Past_Date[2]): # Comapre year
                    if int(Current_Date[1]) > int(Past_Date[0]): # Compare month
                        PastDate.writerow([ID, Info[0], Info[1], Info[3], Info[4], Info[2]])
                    elif int(Current_Date[1]) == int(Past_Date[0]): # If month is the same, it will check the day
                        if int(Current_Date[2]) > int(Past_Date[1]): # Compare days
                            PastDate.writerow([ID, Info[0], Info[1], Info[3], Info[4], Info[2]])
    def Damaged_Inventory(self):
        with open("DamagedInventory.csv",'w') as OutputFile:
            Damaged = csv.writer(OutputFile)
            for ID, Info, in sorted(ManufacturerDict.items()):
                if Info[2] == "damaged":
                    Damaged.writerow([ID,Info[0],Info[1],Info[3],Info[4]])
    def Find_Inventory(self):
        x = 0
        while x != 'q':
            self.Item = input("Enter Manufacturer and Item type:")
            self.Item = self.Item.split()
            ItemList = self.Item
            for ID, Info in ManufacturerDict.items():
                if Info[2] != "damaged":
                    if Info[0] in ItemList:
                        if Info[1] in ItemList:
                            print("Your item is:", ID, Info[0], Info[1], "$" + Info[3])
                            break
            else:
                print("No such item in inventory")
            for ID, Info in ManufacturerDict.items():
                if Info[2] != "damaged":
                    if Info[1] in ItemList and Info[0] not in ItemList:
                        print("You may, also, consider:", ID, Info[0], Info[1], "$" + Info[3])
            print()
            x = input("Type any key to continue or q to quit\n")
#main
ItemInventory = Inventory()
ItemInventory.Manufacturer_List()
ItemInventory.Price_List()
ItemInventory.Service_Dates_List()
ItemInventory.Full_Inventory()
ItemInventory.Laptop_Inventory()
ItemInventory.Past_Service_Date()
ItemInventory.Damaged_Inventory()
ItemInventory.Find_Inventory()