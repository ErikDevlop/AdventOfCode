import os


def read_input() -> dict:
    filepath = os.path.join(os.path.dirname(__file__), '../resource/input6.txt')
    with open(filepath) as fp:
        line = fp.readline()
        orbits_map = dict()
        while line:
            key_value = line.strip().split(')')
            orbits_map[key_value[1]] = key_value[0]
            line = fp.readline()
        return orbits_map


def calculate_orbits(orbits_map: dict, orbital_object: str, number_orbits: int) -> int:
    return number_orbits if orbital_object == 'COM' else calculate_orbits(orbits_map, orbits_map[orbital_object], number_orbits + 1)


def solution_part_one(orbits_map):
    orbital_objects = set(list(orbits_map.keys()) + list(orbits_map.values()))
    return sum([calculate_orbits(orbits_map, orbital_object, 0) for orbital_object in orbital_objects])


def get_path_to_com(orbits_map: dict, orbital_object: str, path: list) -> list:
    if orbital_object == 'COM':
        return path
    else:
        return get_path_to_com(orbits_map, orbits_map[orbital_object], path + [orbits_map[orbital_object]])


def find_path_meeting_point(path1: list, path2: list) -> str:
    for orbital_object in path1:
        if orbital_object in path2:
            return orbital_object


def solution_part_two(orbits_map):
    path_you_to_com = get_path_to_com(orbits_map, 'YOU', list())
    path_san_to_com = get_path_to_com(orbits_map, 'SAN', list())
    orbital_meeting_point = find_path_meeting_point(path_san_to_com, path_you_to_com)
    return path_you_to_com.index(orbital_meeting_point) + path_san_to_com.index(orbital_meeting_point)


input_orbits_map = read_input()
print('Solution part one is {}'.format(solution_part_one(input_orbits_map)))
print('Solution part two is {}'.format(solution_part_two(input_orbits_map)))
