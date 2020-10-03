#Amy Doan ID:1895125
def exact_change(user_total):
   if user_total == 0: # No change if amount is 0
        print("no change")
   else:
       num_dollars = user_total // 100 # Divide into whole number
       user_total %= 100 # total after change
       num_quarters = user_total // 25
       user_total %= 25
       num_dimes = user_total // 10
       user_total %= 10
       num_nickels = user_total // 5
       user_total %= 5
       num_pennies = user_total // 1
       user_total %= 1
       if num_dollars > 1:
            print(num_dollars,"dollars") # Multiple dollars
       elif num_dollars == 1:
            print(num_dollars,"dollar") # 1 dollar
       if num_quarters > 1:
            print(num_quarters,"quarters") # Multiple quarters
       elif num_quarters == 1:
            print(num_quarters, "quarter") # 1 quarter
       if num_dimes > 1:
            print(num_dimes,"dimes") # Multiple dimes
       elif num_dimes == 1:
            print(num_dimes, "dime") # 1 dime
       if num_nickels > 1:
            print(num_nickels,"nickels") # Multiple nickels
       elif num_nickels == 1:
            print(num_nickels, "nickel") # 1 nickel
       if num_pennies > 1:
            print(num_pennies,"pennies") # Multiple pennies
       elif num_pennies == 1:
            print(num_pennies, "penny") # 1 penny
   return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies
if __name__ == '__main__':
    inputval = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(inputval)
