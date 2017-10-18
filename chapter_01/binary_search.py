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


def binary_search_recursive(arr, number, low, high):
    if len(arr) > 1:
        low = low
        high = high
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == number:
            print(mid)
        elif guess > number:
            binary_search_recursive(arr, number, low, mid - 1)
        else:
            binary_search_recursive(arr, number, mid + 1, high)


binary_search_recursive(arr, 20, 0, len(arr) - 1)