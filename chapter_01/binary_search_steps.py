array_items = 256


def binary_search_steps(items):
    steps = 0

    while items > 1:
        items = items // 2
        steps += 1

    return steps


print(binary_search_steps(array_items))
