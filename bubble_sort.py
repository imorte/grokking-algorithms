data = [12, 3, 2, 6, 5, 7]


def bubble_sort(data):
    for i in range(0, len(data) - 1):
        for j in range(0, len(data) - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

    return data


print(bubble_sort(data))
