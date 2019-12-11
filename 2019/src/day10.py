import itertools
import os
import math


def get_list() -> list:
    filepath = os.path.join(os.path.dirname(__file__), '../resource/input10.txt')
    with open(filepath) as fp:
        line = fp.readline()
        input_row = list()
        while line:
            input_row.append([char for char in line])
            line = fp.readline()
        return input_row


def get_angle(p1, p2):
    angle = math.degrees(math.atan2(p2[0] - p1[0], -(p2[1] - p1[1])))
    if angle < 0:
        angle += 360
    return angle


def get_distance(p1, p2):
    return math.sqrt((p2[1] - p1[1]) ** 2 + (p2[0] - p1[0]) ** 2)


def get_coordinates_for_all_asteroids(row_maps: list):
    coordinates = list()
    row = 0
    for row_map in row_maps:
        col = 0
        for column in row_map:
            if column == '#':
                coordinates.append((col, row))
            col += 1
        row += 1
    return coordinates


def get_monitoring_station_info():
    coordinates = get_coordinates_for_all_asteroids(get_list())
    result = dict()
    for current_coordinate in coordinates:
        angles = set()
        for coordinate in coordinates:
            if current_coordinate != coordinate:
                angles.add(get_angle(current_coordinate, coordinate))
        result[current_coordinate] = angles
    return sorted(result.items(), key=lambda x: len(x[1]))[-1]


def solution_part_one():
    return len(get_monitoring_station_info()[1])


def get_number_to_vaporize(informations: list, number: int):
    all_angles = sorted(set([information[1] for information in informations]))
    all_to_vaporize = sorted(informations, key=lambda x: (x[1], x[2]))
    current_number = 1
    for angle in itertools.cycle(all_angles):
        all_processed = True
        for index, a in enumerate(all_to_vaporize):
            if len(a) == 3:
                all_processed = False
            if angle == a[1] and len(a) == 3:
                all_to_vaporize[index] = a[0], a[1], a[2], current_number
                current_number += 1
                break
        if all_processed:
            break
    return sorted(all_to_vaporize, key=lambda x: x[3])[number - 1]


def solution_part_two():
    coordinates = get_coordinates_for_all_asteroids(get_list())
    current_coordinate = get_monitoring_station_info()[0]
    information = list()
    for coordinate in coordinates:
        if current_coordinate != coordinate:
            info = coordinate, get_angle(current_coordinate, coordinate), get_distance(current_coordinate, coordinate)
            information.append(info)
    coordinates_for_200th = get_number_to_vaporize(information, 200)[0]
    return coordinates_for_200th[0] * 100 + coordinates_for_200th[1]


print('Solution for part one is: {}'.format(solution_part_one()))
print('Solution for part two is: {}'.format(solution_part_two()))
