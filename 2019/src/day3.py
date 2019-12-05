import os


def get_lists() -> (list, list):
    filepath = os.path.join(os.path.dirname(__file__), '../resource/input3.txt')
    with open(filepath) as fp:
        return fp.readline().split(","), fp.readline().split(",")


def get_path_to_next_intersection(last_intersection, direction, distance):
    intersection_x_position = last_intersection[0]
    intersection_y_position = last_intersection[1]
    positions = list()
    for i in range(1, distance + 1):
        if direction == 'U':
            positions.append((intersection_x_position, intersection_y_position + i))
        if direction == 'D':
            positions.append((intersection_x_position, intersection_y_position - i))
        if direction == 'L':
            positions.append((intersection_x_position - i, intersection_y_position))
        if direction == 'R':
            positions.append((intersection_x_position + i, intersection_y_position))
    return positions


def calculate_path(wire: list) -> list:
    path = list()
    path.append((0, 0))
    for instruction in wire:
        direction = instruction[0]
        distance = int(instruction[1:])
        path = path + get_path_to_next_intersection(path[-1], direction, distance)
    return path


def solution_closest(wire1: list, wire2: list) -> int:
    path_wire1 = calculate_path(wire1)
    path_wire2 = calculate_path(wire2)
    wire_crosses = list(set(path_wire1) & set(path_wire2))
    intersections_distances = [abs(cross[0]) + abs(cross[1]) for cross in wire_crosses]
    intersections_distances.sort()
    return intersections_distances[1]


def solution_shortest(wire1: list, wire2: list) -> int:
    path_wire1 = calculate_path(wire1)
    path_wire2 = calculate_path(wire2)
    wire_crosses = list(set(path_wire1) & set(path_wire2))
    intersections_distances = [path_wire1.index(cross) + path_wire2.index(cross) for cross in wire_crosses]
    intersections_distances.sort()
    return intersections_distances[1]


wire1, wire2 = get_lists()
print('The answer for part one is {}'.format(solution_closest(wire1, wire2)))

print('The answer for part two is {}'.format(solution_shortest(wire1, wire2)))
