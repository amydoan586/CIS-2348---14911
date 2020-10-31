#Amy Doan ID: 1895125
class ItemToPurchase:
    def __init__(self,item_name = "none", item_price = 0, item_quantity = 0, item_description = "none"):
        self.item_name = str(item_name)
        self.item_price = int(item_price)
        self.item_quantity = int(item_quantity)
        self.item_description = str(item_description)
    def print_item_cost(self):
        print(self.item_name, str(self.item_quantity), "@", "$" + str(self.item_price), "=", "$" + str(self.item_price * self.item_quantity))
    def print_item_description(self):
        print(self.item_name + ":", self.item_description)
class ShoppingCart:
    def __init__(self,customer_name = "none", current_date = 0,):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
    def add_items(self): # Add Method
        print("ADD ITEM TO CART")
        item_name = str(input("Enter the item name:\n")) #Inputs item name
        item_description = str(input("Enter the item description:\n")) # Inputs desc
        item_price = int(input("Enter the item price:\n")) # Input price
        item_quantity = int(input("Enter the item quantity:\n")) # Input quantity
        self.cart_items.append(ItemToPurchase(item_name,item_price,item_quantity,item_description)) # Adds into a list
    def remove_items(self,Remove): # Remove Method
        for i in self.cart_items: # Loop items
            if (i.item_name == Remove): # If Item match to user's input it removes the item
                self.cart_items.remove(i)
                break # Loop stops
        else:
            print("Item not found in cart. Nothing removed.") # Prints if the item is not in the list
    def modify_item(self,Modify):
        Quantity = int(input("Enter the new quantity:\n")) # Inputs quantity of new item
        for i in self.cart_items: # Loop each item in list
            if(i.item_name == Modify): # If item match to user's input it changes the quantity
                i.item_quantity = Quantity
                break
        else:
            print("Item not found in cart. Nothing modified.")
    def get_num_items_in_cart(self): # Method for number of items in the cart
        num_items = 0
        for i in self.cart_items: # Loop the item in the list
            num_items = num_items + i.item_quantity # Adds all items in the list
        return num_items
    def get_cost_of_cart(self): # Total cost
        totalcost = 0
        for i in self.cart_items: # Loop each item to get the total cost
            totalcost = totalcost + (i.item_quantity * i.item_price)
        return totalcost
    def print_total(self): # Print total
        print(self.customer_name + "'s" + "Shopping Cart -",self.current_date)
        print("Number of Items:",ShoppingCart.get_num_items_in_cart())
        print()
        if self.cart_items == 0: # If there nothing in the list, the cart is empty
            print("SHOPPING CART IS EMPTY")
            print()
        else:
            for i in self.cart_items: # Loop to display each item in the list with pice and quantity
                print(i,i.item_quantity,"@",i.item_price,"=","$",(i.item_quantity * i.item_price))
            print("Total:",ShoppingCart.get_cost_of_cart()) # Prints the total for all item

    def print_description(self): # Print the description for each item
        print("OUTPUT ITEMS' DESCRIPTIONS")
        print(self.customer_name + "'s " + "Shopping Cart -", self.current_date)
        print()
        print("Item Descriptions")
        for i in self.cart_items:
            print(i.item_name + ": " + i.item_description)
def menu(): # Display the menu
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
    print()
def print_menu(ShoppingCart):
    menu() # Call the menu
    while True:
        x = input("Choose an option:\n")
        if x == 'a':
            ShoppingCart.add_items() # Call to add item
            print()
            menu()
        if x == 'r':
            print("REMOVE ITEM FROM CART")
            Remove_item = input("Enter name of item to remove:\n") # Input item to remove
            ShoppingCart.remove_items(Remove_item) # Call to remove item
            print()
            menu()
        if x == 'c':
            print("CHANGE ITEM QUANTITY")
            Modify = input("Enter the item name:\n") # Input item name to change the quantity
            ShoppingCart.modify_item(Modify) # Call to modify
            print()
            menu()
        if x == 'i':
            ShoppingCart.print_description() # Call to get descriptions
            print()
            menu()
        if x == 'o':
            print("OUTPUT SHOPPING CART") # Print out the shopping cart with its total
            print(ShoppingCart.customer_name + "'s" + " Shopping Cart -", ShoppingCart.current_date)
            print("Number of Items:", ShoppingCart.get_num_items_in_cart())
            print()
            if ShoppingCart.get_num_items_in_cart() == 0: # If there is nothing in the cart, is display that it is empty
                print("SHOPPING CART IS EMPTY")
                print()
                print("Total:", "$" + str(ShoppingCart.get_cost_of_cart()))
            else:
                for i in ShoppingCart.cart_items: # Loop to display the items with tis price and quantity
                    print(i.item_name, i.item_quantity, "@", "$" + str(i.item_price), "=", "$" + str(i.item_quantity * i.item_price))
                print()
                print("Total:", "$" + str(ShoppingCart.get_cost_of_cart())) # Display total
            print()
            menu()
        if x == 'q':
            exit() # Exit
if __name__ == '__main__':
    ShoppingDesc = ShoppingCart() #Assign a variable with a class
    ShoppingDesc.customer_name = input("Enter customer's name:\n") # Input name and stores ir
    ShoppingDesc.current_date = input("Enter today's date:\n") # Input date and stores it
    print()
    print("Customer name:",ShoppingDesc.customer_name)
    print("Today's date:",ShoppingDesc.current_date)
    print()
    print_menu(ShoppingDesc) #Print out the menu
