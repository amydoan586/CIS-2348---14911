# Amy Doan ID: 1895125
def selection_sort_descend_trace(numbers):
    #Taken from textbook
    for i in range(len(numbers) - 1):
        index_largest = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] > numbers[index_largest]:
                index_largest = j
        temp = numbers[i]
        numbers[i] = numbers[index_largest]
        numbers[index_largest] = temp
        for i in range(len(numbers)):
            print(str(numbers[i]), end=" ")
        print()

if __name__ == "__main__":
    numbers = []
    x = input()
    numbers = x.split()
    selection_sort_descend_trace(numbers)