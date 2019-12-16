from enum import Enum
from intcode_computer import IntcodeComputer
from util import read_input


def get_program():
    program = list()
    for line in read_input('input13.txt'):
        program.extend(line.split(","))
    return [int(i) for i in program]


X = 0
Y = 1
DATA = 2


class Game(object):

    def __init__(self, initial_memory: list):
        self.program = initial_memory
        self.x_pos_paddle = [-1]
        self.x_pos_ball = [-1]
        self.given_inputs = [-1]
        self.score = 0
        grid_width = 36
        grid_height = 25
        self.grid = [[0] * grid_width for _ in range(grid_height)]
        self.paddle_must_change = False

    def run_game(self, inputs: list):
        game_mode = self.program[0] == 2
        section = list()
        for output in IntcodeComputer(self.program).calculate(inputs):
            section.append(output)
            if len(section) == 3:
                if section[X] == -1 and section[Y] == 0:
                    self.score = section[DATA]
                else:
                    self.grid[section[Y]][section[X]] = section[DATA]
                if game_mode:
                    print()
                    print('Your score is: {}'.format(self.score))
                    print_grid(self.grid)
                    self.send_instruction(inputs)
                section = list()
        return self.grid

    def send_instruction(self, inputs):
        x_pos_ball = -1
        x_pos_paddle = -1
        for grid_row in self.grid:
            if Tile.BALL.value in grid_row:
                x_pos_ball = grid_row.index(Tile.BALL.value)
            if Tile.PADDLE.value in grid_row:
                x_pos_paddle = grid_row.index(Tile.PADDLE.value)
        instruction = 0
        if x_pos_ball < x_pos_paddle:
            instruction = -1
        elif x_pos_ball > x_pos_paddle:
            instruction = 1
        elif x_pos_ball == x_pos_paddle:
            instruction = 0
        if self.x_pos_ball[-1] != x_pos_ball and x_pos_ball > 0 and ((self.x_pos_paddle[-1] != x_pos_paddle and x_pos_paddle > 0) or self.given_inputs[-1] == 0):
            inputs.append(instruction)
            self.given_inputs.append(instruction)
            self.x_pos_ball.append(x_pos_ball)
            self.x_pos_paddle.append(x_pos_paddle)


def solution_part_one(initial_memory: list, inputs: list):
    grid = Game(initial_memory).run_game(inputs)
    return sum([grid_row.count(2) for grid_row in grid])


def solution_part_two(initial_memory: list, inputs: list):
    Game(initial_memory).run_game(inputs)


def print_grid(grid):
    for row in grid:
        print(''.join([set_tile_color(r) for r in row]))


def set_tile_color(tile: int):
    if tile == Tile.EMPTY.value:
        return "░"
    elif tile == Tile.WALL.value:
        return "▓"
    elif tile == Tile.BLOCK.value:
        return "█"
    elif tile == Tile.PADDLE.value:
        return "_"
    elif tile == Tile.BALL.value:
        return "■"


class Tile(Enum):
    EMPTY = 0  # is an empty tile. No game object appears in this tile.
    WALL = 1  # is a wall tile. Walls are indestructible barriers.
    BLOCK = 2  # is a block tile. Blocks can be broken by the ball.
    PADDLE = 3  # is a horizontal paddle tile. The paddle is indestructible.
    BALL = 4  # is a ball tile. The ball moves diagonally and bounces off objects.


the_program = get_program()
print(solution_part_one(the_program.copy(), []))
the_program[0] = 2
solution_part_two(the_program, [])
