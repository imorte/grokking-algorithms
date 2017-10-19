from PIL import Image, ImageDraw

WIDTH = 'width'
HEIGHT = 'height'

init_width = 1680
init_height = 640


def check_sides(width, height, side):
    if width % height == 0:
        return width // 2
    else:
        if side == WIDTH:
            return height % width
        else:
            return width % height


def draw_visual(width, height, side):
    im = Image.new('RGB', (init_width, init_height), (255, 255, 255))
    im.save('hopper.png')
    im = Image.open('hopper.png')
    draw = ImageDraw.Draw(im)

    draw.line((0, 0) + (0, 0), fill=0)

    del draw
    im.save('hopper.png', "PNG")


def find_smallest_area(width=init_width, height=init_height):
    if width % height == 0:
        print('Result is', height, height)
        return
    else:
        if width > height:
            smallest_width = width % height
            smallest_height = height
            tail_width = width - smallest_width
            tail_height = height
        else:
            smallest_width = width
            smallest_height = height % width
            tail_width = width
            tail_height = height - smallest_height

        current_state = {
            'smallest': [smallest_width, smallest_height],
            'tail': [tail_width, tail_height]
        }

        find_smallest_area(smallest_width, smallest_height)


print(find_smallest_area(init_width, init_height))
