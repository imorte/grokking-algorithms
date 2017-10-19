from PIL import Image, ImageDraw

WIDTH = 'width'
HEIGHT = 'height'

init_width = 1680
init_height = 640


def draw_lines(width, height, side, draw):
    padding_width = init_height - width
    padding_height = init_height - height

    if side == WIDTH:
        one_side = height
        while one_side <= width:
            draw.line((one_side, 0) + (one_side, one_side), fill=0)
            one_side += height
    else:
        one_side = width
        while one_side <= height:
            draw.line((init_width, one_side) + (0 + (init_width - one_side), one_side), fill=0)
            one_side += width


im = Image.new('RGB', (init_width, init_height), (255, 255, 255))
im.save('hopper.png')


def find_smallest_area(width=init_width, height=init_height):
    im = Image.open('hopper.png')
    draw = ImageDraw.Draw(im)

    if width % height == 0:
        print('Result is', height, height)
        return
    else:
        if width > height:
            smallest_width = width % height
            smallest_height = height
            tail_width = width - smallest_width
            tail_height = height

            draw_lines(tail_width, tail_height, WIDTH, draw)

        else:
            smallest_width = width
            smallest_height = height % width
            tail_width = width
            tail_height = height - smallest_height

            draw_lines(tail_width, tail_height, HEIGHT, draw)

        del draw
        im.save('hopper.png', "PNG")

        find_smallest_area(smallest_width, smallest_height)


print(find_smallest_area(init_width, init_height))
