import os


def get_list() -> list:
    filepath = os.path.join(os.path.dirname(__file__), '../resource/input8.txt')
    with open(filepath) as fp:
        line = fp.readline()
        input_list = list()
        while line:
            input_list.extend([int(char) for char in line])
            line = fp.readline()
        return input_list


def get_layers(digits, pixels_per_layer):
    layers = list()
    start = 0
    while start < len(digits):
        layers.append(digits[start:start + pixels_per_layer])
        start += pixels_per_layer
    return layers


def solution_part_one(digits, width, height):
    pixels_per_layer = width * height
    layers = get_layers(digits, pixels_per_layer)
    the_layer = layers[0]
    for layer in layers:
        if layer.count(0) < the_layer.count(0):
            the_layer = layer
    return the_layer.count(1) * the_layer.count(2)


def solution_part_two(digits, width, height):
    pixels_per_layer = width * height
    layers = get_layers(digits, pixels_per_layer)
    picture_digits = layers[0]
    pixels = range(pixels_per_layer)
    for layer in layers:
        for pixel in pixels:
            picture_digits[pixel] = check_color(picture_digits[pixel], layer[pixel])
    start = 0
    while start < len(picture_digits):
        print(''.join([" " if i == 0 else "█" for i in picture_digits[start:start + width]]))
        start += width


def check_color(last_pixel, next_pixel):
    if last_pixel in [BLACK, WHITE]:
        return last_pixel
    else:
        return next_pixel


BLACK = 0
WHITE = 1
TRANSPARENT = 2

pixel_width = 25
pixel_height = 6
the_list = get_list()
print('Solution for part one is: {}'.format(solution_part_one(the_list, pixel_width, pixel_height)))
print('Solution for part two is:')
solution_part_two(the_list, pixel_width, pixel_height)