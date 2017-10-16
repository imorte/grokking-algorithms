arr = [1, 6, 8, 20, 53, 65, 77, 87, 95]


def binary_search(arr, number):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == number:
            return mid
        if guess > number:
            high = mid - 1
        else:
            low = mid + 1

    return None


print(binary_search(arr, 20))