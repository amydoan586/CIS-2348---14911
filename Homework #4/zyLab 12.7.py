# Amy Doan ID: 1895125
def fat_burning_heart_rate(age):
    Heart_Rate = (220 - age) * .70
    print("Fat burning heart rate for a",age, "year-old:",Heart_Rate,"bpm")
    return Heart_Rate
def get_age():
    Age = int(input())
    if 18 < Age < 75:
        fat_burning_heart_rate(Age)
    else:
        raise ValueError("Invalid age.")
if __name__ == '__main__':
    try:
        get_age()
    except ValueError as Error:
        print(Error)
        print("Could not calculate heart rate info.\n")