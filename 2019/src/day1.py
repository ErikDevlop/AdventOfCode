import math
import os


def calculateFuelRequired(mass: int) -> int:
    return math.floor(mass / 3) - 2


def solution():
    filepath = os.path.join(os.path.dirname(__file__), '../resource/input1.txt')
    with open(filepath) as fp:
        line = fp.readline()
        fuel_required = list()
        while line:
            fuel_required.append(calculateFuelRequired(int(line.strip())))
            line = fp.readline()
        return sum(fuel_required)


print('The fuel required is {}'.format(solution()))
