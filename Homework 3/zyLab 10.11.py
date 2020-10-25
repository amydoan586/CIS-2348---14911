#Amy Doan ID: 1895125
class FoodItem:
    def __init__(self,name="None",fat=0.0,carbs=0.0,protein=0.0): # Assign constructor with parameters
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein
    def get_calories(self, num_servings): # Get calories
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings;
        return calories

    def print_info(self): #Print information
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))
if __name__ == '__main__':
    Food1 = FoodItem() # Assign class to Food 1
    # Input Food 2 information
    Food2 = FoodItem() # Assign class to Food 2
    Food2.name = input()
    Food2.fat = float(input())
    Food2.carbs = float(input())
    Food2.protein = float(input())
    servings = float(input())
    Food1.print_info() # Print Food 1 "None"
    print("Number of calories for {:.2f}".format(servings), "serving(s): {:.2f}".format(Food1.get_calories(servings))) # Print Calories for food 1
    print()
    Food2.print_info() # Print Food 2
    print("Number of calories for {:.2f}".format(servings), "serving(s): {:.2f}".format(Food2.get_calories(servings))) # Print Calories for food 2
