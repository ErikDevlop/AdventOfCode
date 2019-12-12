import re
from util import read_input
from functools import reduce
from math import gcd


def lcm(a, b):
    return int(a * b / gcd(a, b))


def lcms(numbers: list):
    return reduce(lcm, numbers)


X = 0
Y = 1
Z = 2


def get_moons():
    moons = list()
    for line in read_input('input12.txt'):
        moons.append(Moon([find('x', line), find('y', line), find('z', line)]))
    return moons


def find(key, string: str) -> int:
    return int(re.search(r'^.*?\b{}=([-+]?[0-9]+)'.format(key), string).group(1))


def compute_gravity_affect(position, other_position):
    if position == other_position:
        return 0
    elif position < other_position:
        return 1
    else:
        return -1


class Moon(object):

    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.velocity_vector = [0, 0, 0]

    def apply_gravity(self, other_moon):
        self.velocity_vector[X] += compute_gravity_affect(self.coordinates[X], other_moon.coordinates[X])
        self.velocity_vector[Y] += compute_gravity_affect(self.coordinates[Y], other_moon.coordinates[Y])
        self.velocity_vector[Z] += compute_gravity_affect(self.coordinates[Z], other_moon.coordinates[Z])

    def apply_velocity(self):
        self.coordinates = [x + y for x, y in zip(self.coordinates, self.velocity_vector)]

    def get_potential_energy(self):
        return sum(map(abs, self.coordinates))

    def get_kinetic_energy(self):
        return sum(map(abs, self.velocity_vector))

    def __str__(self):
        output = self.coordinates.copy()
        output.extend(self.velocity_vector)
        return 'pos=<x={0: >5}, y={1: >5}, z={2: >5}>, vel=<x={3: >5}, y={4: >5}, z={5: >5}>'.format(*output)


def compute_system_energy(moons: list):
    energy = 0
    for moon in moons:
        energy += moon.get_potential_energy() * moon.get_kinetic_energy()
    return energy


def apply_physics(moons):
    for moon in moons:
        for other_moon in moons.copy():
            moon.apply_gravity(other_moon)
    for moon in moons:
        moon.apply_velocity()


def print_step(time, moons):
    print('After {} steps:'.format(time))
    for moon in moons:
        print(moon)
    print()


def solution_part_one(steps):
    moons = get_moons()
    time_steps = range(steps)
    # print_step(0, moons)
    for time in time_steps:
        apply_physics(moons)
        # print_step(time, moons)
    return compute_system_energy(moons)


def state_to_string(moons, dimension: int) -> str:
    return str(dimension) + ','.join([str(moon.coordinates[dimension]) + str(moon.velocity_vector[dimension]) for moon in moons])


def solution_part_two():
    moons = get_moons()
    states = set()
    states.add(state_to_string(moons, X))
    states.add(state_to_string(moons, Y))
    states.add(state_to_string(moons, Z))
    result = dict()
    for time in range(1, 10000000000):
        if len(result) == 3:
            break
        apply_physics(moons)
        check_state_for_dimension(moons, result, states, time, X)
        check_state_for_dimension(moons, result, states, time, Y)
        check_state_for_dimension(moons, result, states, time, Z)
    return lcms(result.values())


def check_state_for_dimension(moons, result, states, time, dimension: int):
    state = state_to_string(moons, dimension)
    if dimension not in result.keys() and state in states:
        result[dimension] = time
    states.add(state)


number_steps = 1000
print('Total energy in the system after {} steps: {}'.format(number_steps, solution_part_one(number_steps)))
print('Time steps to reach same state again: {}'.format(solution_part_two()))
