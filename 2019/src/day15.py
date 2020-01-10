import random
from enum import Enum
from intcode_computer import IntcodeComputer
from util import read_input, clear_screen, sleep_ms


def get_program():
    program = list()
    for line in read_input('input15.txt'):
        program.extend(line.split(","))
    return [int(i) for i in program]


class RepairDroid(object):

    def __init__(self, program: list):
        self.computer = IntcodeComputer(program)
        self.droid_position = (0, 0)
        self.grid = {self.droid_position: 'D'}
        self.direction = Direction.NORTH

    def run_droid(self):
        inputs = [self.direction.value]
        for output in self.computer.calculate(inputs):
            if output == Status.WALL.value:
                self.grid[self.coordinate(self.droid_position, self.direction)] = Grid.WALL.value
            if output == Status.MOVED.value:
                self.update_position(self.direction)
            if output == Status.FOUND.value:
                self.update_position(self.direction)
                break
            self.direction = self.get_next_direction()
            inputs.append(self.direction.value)
        self.print_grid()
        return self.grid

    def update_position(self, direction):
        self.grid[self.droid_position] = Grid.PATH.value
        self.droid_position = self.coordinate(self.droid_position, direction)
        self.grid[self.droid_position] = Grid.DROID.value

    @staticmethod
    def coordinate(position, direction):
        if direction == Direction.NORTH:
            return position[0], position[1] + 1
        if direction == Direction.SOUTH:
            return position[0], position[1] - 1
        if direction == Direction.WEST:
            return position[0] - 1, position[1]
        if direction == Direction.EAST:
            return position[0] + 1, position[1]

    def get_next_direction(self):
        right_turn_direction = self.right_turn_direction(self.direction)
        left_turn_direction = self.right_turn_direction(self.right_turn_direction(right_turn_direction))
        if not self.is_wall(self.grid, self.droid_position, right_turn_direction):
            return right_turn_direction
        elif not self.is_wall(self.grid, self.droid_position, self.direction):
            return self.direction
        elif not self.is_wall(self.grid, self.droid_position, left_turn_direction):
            return left_turn_direction
        else:
            return self.right_turn_direction(right_turn_direction)

    @staticmethod
    def is_wall(grid, position, direction):
        return RepairDroid.coordinate(position, direction) in grid and grid[RepairDroid.coordinate(position, direction)] == Grid.WALL.value

    @staticmethod
    def right_turn_direction(direction):
        if direction == Direction.NORTH:
            return Direction.EAST
        if direction == Direction.EAST:
            return Direction.SOUTH
        if direction == Direction.SOUTH:
            return Direction.WEST
        if direction == Direction.WEST:
            return Direction.NORTH

    def print_grid(self):
        sleep_ms(200)
        print('\n' * 80)
        self.grid[(0,0)] = 'X'
        x_coord = sorted([x for x, y in self.grid])
        y_coord = sorted([y for x, y in self.grid])
        for x in range(x_coord[0], x_coord[-1] + 1):
            for y in range(y_coord[0], y_coord[-1] + 1):
                print(self.grid[(x, y)] if (x, y) in self.grid else ' ', end='')
            print()


def solution_part_one(initial_memory: list):
    grid = RepairDroid(initial_memory).run_droid()
    pass
    for k, v in grid.items():
        if v == Grid.DROID.value:
            return quickest_route(grid, (0, 0), k)


def quickest_route(grid, from_pos, to_pos):
    return min([
            shortest_path(grid, to_pos, Direction.NORTH, [from_pos]),
            shortest_path(grid, to_pos, Direction.SOUTH, [from_pos]),
            shortest_path(grid, to_pos, Direction.EAST, [from_pos]),
            shortest_path(grid, to_pos, Direction.WEST, [from_pos])
        ])


def shortest_path(grid, to_pos, direction, path):
    if RepairDroid.is_wall(grid, path[-1], direction):
        return 100000000000
    elif path[-1] == to_pos:
        print(len(path))
        return len(path)
    else:
        coord = RepairDroid.coordinate(path[-1], direction)
        path.append(coord)
        return min([
            shortest_path(grid, to_pos, Direction.NORTH, path.copy()),
            shortest_path(grid, to_pos, Direction.SOUTH, path.copy()),
            shortest_path(grid, to_pos, Direction.EAST, path.copy()),
            shortest_path(grid, to_pos, Direction.WEST, path.copy())
        ])


class Status(Enum):
    WALL = 0
    MOVED = 1
    FOUND = 2


class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    WEST = 3
    EAST = 4


class Grid(Enum):
    DROID = 'D'
    WALL = '#'
    PATH = '.'


the_program = get_program()
print(solution_part_one(the_program.copy()))
