import random

data = [4, 2, 55, 12]


def qsort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[random.randint(0, len(array) - 1)]
        less = [i for i in array if i < pivot]
        middle = [i for i in array if i == pivot]
        greater = [i for i in array if i > pivot]

        return qsort(less) + middle + qsort(greater)


print(qsort(data))
