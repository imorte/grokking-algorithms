array_items = 256


def binary_search_steps(items):
    steps = 0

    while items > 1:
        items = items // 2
        steps = steps + 1

    return steps


def binary_search_steps_recursive(items):
    steps = 0

    return steps


print(binary_search_steps(array_items))
print(binary_search_steps_recursive(array_items))