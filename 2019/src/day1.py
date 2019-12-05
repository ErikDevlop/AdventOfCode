import math
import os


def calculateFuelRequired(mass: int) -> int:
    return math.floor(mass / 3) - 2


def calculateFuelRequiredRecursive(mass: int) -> int:
    fuel_required = list()
    fuel_required_mass = calculateFuelRequired(mass)
    while fuel_required_mass > 0:
        fuel_required.append(fuel_required_mass)
        fuel_required_mass = calculateFuelRequired(fuel_required_mass)
    return sum(fuel_required)


def solution(func):
    filepath = os.path.join(os.path.dirname(__file__), '../resource/input1.txt')
    with open(filepath) as fp:
        line = fp.readline()
        fuel_required = list()
        while line:
            fuel_required.append(func(int(line.strip())))
            line = fp.readline()
        return sum(fuel_required)


print('The fuel required is {}'.format(solution(calculateFuelRequired)))

print('The fuel required for all fuel is {}'.format(solution(calculateFuelRequiredRecursive)))
