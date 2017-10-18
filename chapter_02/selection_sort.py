arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]


def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    
    return smallest_index


def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))

    return new_arr


# print(selection_sort(arr))


def selection_sort_combined(arr):
    new_arr = []
    while len(arr) > 1:
        smallest_value = arr[0]
        smallest_index = 0
        for i in range(1, len(arr)):
            if arr[i] < smallest_value:
                smallest_value = arr[i]
                smallest_index = i
        new_arr.append(arr.pop(smallest_index))

    return new_arr


print(selection_sort_combined(arr))
