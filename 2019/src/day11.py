import os
from intcode_computer import IntcodeComputer
from enum import Enum


def get_list() -> list:
    filepath = os.path.join(os.path.dirname(__file__), '../resource/input11.txt')
    with open(filepath) as fp:
        line = fp.readline()
        input_list = list()
        while line:
            input_list.extend(line.split(","))
            line = fp.readline()
        return [int(i) for i in input_list]


def solution(initial_memory: list, initial_color: int):
    inputs = [initial_color]
    grid_size = 100
    grid = [[0] * grid_size for _ in range(grid_size)]
    grid_position = int(grid_size / 2), int(grid_size / 2)
    panels_painted = set([grid_position])
    is_color_output = True
    direction = Direction.UP
    for output in IntcodeComputer(initial_memory).calculate(inputs):
        if is_color_output:
            grid[grid_position[1]][grid_position[0]] = output
            is_color_output = False
        else:
            grid_position, direction = get_next_grid_point_and_direction(direction, grid_position, output)
            is_color_output = True
            panels_painted.add(grid_position)
            inputs.append(grid[grid_position[1]][grid_position[0]])
    print_grid(grid)
    return len(panels_painted)


def get_next_grid_point_and_direction(direction, grid_position, output):
    x_position = grid_position[0]
    y_position = grid_position[1]
    if direction == Direction.UP:
        if output == Direction.LEFT.value:
            grid_position = x_position - 1, y_position
            direction = Direction.LEFT
        elif output == Direction.RIGHT.value:
            grid_position = x_position + 1, y_position
            direction = Direction.RIGHT
    elif direction == Direction.DOWN:
        if output == Direction.LEFT.value:
            grid_position = x_position + 1, y_position
            direction = Direction.RIGHT
        elif output == Direction.RIGHT.value:
            grid_position = x_position - 1, y_position
            direction = Direction.LEFT
    elif direction == Direction.RIGHT:
        if output == Direction.LEFT.value:
            grid_position = x_position, y_position - 1
            direction = Direction.UP
        elif output == Direction.RIGHT.value:
            grid_position = x_position, y_position + 1
            direction = Direction.DOWN
    elif direction == Direction.LEFT:
        if output == Direction.LEFT.value:
            grid_position = x_position, y_position + 1
            direction = Direction.DOWN
        elif output == Direction.RIGHT.value:
            grid_position = x_position, y_position - 1
            direction = Direction.UP
    return grid_position, direction


def print_grid(grid):
    for row in grid:
        print(''.join(["░" if r == Color.BLACK.value else "█" for r in row]))


class Direction(Enum):
    LEFT = 0
    RIGHT = 1
    UP = 3
    DOWN = 4


class Color(Enum):
    BLACK = 0
    WHITE = 1


program = get_list()
print('Solution for part one is: {}'.format(solution(program.copy(), Color.BLACK.value)))
print('Solution for part two is: {}'.format(solution(program.copy(), Color.WHITE.value)))
