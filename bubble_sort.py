data = [12, 3, 2, 6, 5, 7]


def bubble_sort(data):
    for i in range(0, len(data) - 1):
        for j in range(0, len(data) - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

    return data


# print(bubble_sort(data))


def bubble_sort_new(data):
    for i in range(0, len(data)):
        for j in range(i + 1, len(data)):
            if data[j] < data[i]:
                data[j], data[i] = data[i], data[j]

    return data


print(bubble_sort_new(data))
