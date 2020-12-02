# Amy Doan ID: 1895125
# Global variable
num_calls = 0
def partition(user_ids, i, k):
    #Taken from textbook
    midpoint = i + (k - i) // 2
    pivot = user_ids[midpoint]
    done = False
    while not done:
        while user_ids[i] < pivot:
            i += 1
        while pivot < user_ids[k]:
            k -= 1
        if i >= k:
            done = True
        else:
            temp = user_ids[i]
            user_ids[i] = user_ids[k]
            user_ids[k] = temp
            i += 1
            k -= 1
    return k
def quicksort(user_ids, i, k):
    global num_calls
    num_calls = num_calls + 1
    j = 0
    if i >= k:
        return
    j = partition(user_ids, i, k)
    quicksort(user_ids, i, j)
    quicksort(user_ids, j + 1, k)
    return
if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()
    quicksort(user_ids, 0, len(user_ids) - 1)
    print(num_calls)
    for user_id in user_ids:
        print(user_id)