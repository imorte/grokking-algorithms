init_width = 1680
init_height = 640


def find_smallest_area(width=init_width, height=init_height):
    if width % height == 0:
        print('Result is', height, height)
        return
    else:
        if width > height:
            smallest_width = width % height
            smallest_height = height
            # tail_width = width - smallest_width
            # tail_height = height
        else:
            smallest_width = width
            smallest_height = height % width
            # tail_width = width
            # tail_height = height - smallest_height

        find_smallest_area(smallest_width, smallest_height)


print(find_smallest_area(init_width, init_height))
