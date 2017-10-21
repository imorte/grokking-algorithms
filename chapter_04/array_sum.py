arr = [2, 4, 8, 6]


def array_sum(arr):
    total = 0
    for x in arr:
        total += x

    return total


print(array_sum(arr))


def array_sum_recursive(arr):
    if len(arr) <= 1:
        return arr[0]
    else:
        return arr[0] + array_sum_recursive(arr[1:])


print(array_sum_recursive(arr))


def array_count_recursive(arr):
    if len(arr) == 1:
        return 1
    else:
        return 1 + array_count_recursive(arr[1:])


print(array_count_recursive(arr))
