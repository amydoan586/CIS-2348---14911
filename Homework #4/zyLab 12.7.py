# Amy Doan ID: 1895125
def fat_burning_heart_rate(Age):
    if 18 < Age < 75:
        Heart_Rate = (220 - Age) * .70
        print("Fat burning heart rate for a",Age, "year-old:",Heart_Rate)
    else:
        print("Invalid age.")
        print("Could not calculate heart rate info.")
if __name__ == '__main__':
    age = int(input("Enter age: \n"))
    fat_burning_heart_rate(age)