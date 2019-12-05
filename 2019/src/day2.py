import os


def get_list() -> list:
    filepath = os.path.join(os.path.dirname(__file__), '../resource/input2.txt')
    with open(filepath) as fp:
        line = fp.readline()
        input_list = list()
        while line:
            input_list.extend(line.split(","))
            line = fp.readline()
        return [int(i) for i in input_list]


def calculate(memory) -> list:
    address = 0
    while address < len(memory):
        instruction = memory[address:address+4]
        opcode = instruction[0]
        if opcode in [1, 2, 99]:
            if opcode == 99:
                return memory
            if opcode == 1:
                memory[instruction[3]] = memory[instruction[1]] + memory[instruction[2]]
            if opcode == 2:
                memory[instruction[3]] = memory[instruction[1]] * memory[instruction[2]]
        address = address + 4


def solution(the_list: list, noun: int, verb: int) -> int:
    the_list[1] = noun
    the_list[2] = verb
    return calculate(the_list)[0]


# part one
print('The answer is {}'.format(solution(get_list(), 12, 2)))


def part_two_solution(the_list: list) -> int:
    for noun in range(0, 100):
        for verb in range(0, 100):
            if solution(the_list.copy(), noun, verb) == 19690720:
                return 100 * noun + verb


# part two
print('The answer is {}'.format(part_two_solution(get_list())))
