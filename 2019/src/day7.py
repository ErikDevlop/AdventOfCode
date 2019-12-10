import itertools
import os


def get_list() -> list:
    filepath = os.path.join(os.path.dirname(__file__), '../resource/input7.txt')
    with open(filepath) as fp:
        line = fp.readline()
        input_list = list()
        while line:
            input_list.extend(line.split(","))
            line = fp.readline()
        return [int(i) for i in input_list]


class IntcodeComputer(object):

    def __init__(self, memory: list, instruction_pointer: int):
        self.memory = memory
        self.instruction_pointer = instruction_pointer

    @staticmethod
    def get_mode_and_opcode(instruction_input: int) -> (int, int, int, int):
        string_input = str(instruction_input).zfill(5)
        return int(string_input[0]), int(string_input[1]), int(string_input[2]), int(string_input[-2:])

    @staticmethod
    def is_immediate_mode(mode: int) -> bool:
        return mode == 1

    def get_according_to_mode(self, memory: list, pointer: int, mode: int):
        length = len(memory)
        if self.is_immediate_mode(mode) and pointer < length:
            return memory[pointer]
        elif memory[pointer] < length:
            return memory[memory[pointer]]
        else:
            print('Error: Length was {}, wanted to access {}'.format(length, memory[pointer]))
            return 0

    def calculate(self, input_list):
        while True:
            third_mode, second_mode, first_mode, opcode = self.get_mode_and_opcode(self.memory[self.instruction_pointer])
            if opcode not in [1, 2, 3, 4, 5, 6, 7, 8, 99]:
                print('Opcode {} is not supported'.format(opcode))
                break
            if opcode == 99:
                return None, self
            if opcode == 3:
                self.memory[self.memory[self.instruction_pointer + 1]] = input_list.pop(0)
                self.instruction_pointer += 2
            if opcode == 4:
                value = self.memory[self.memory[self.instruction_pointer + 1]]
                self.instruction_pointer += 2
                return value, self
            param1 = self.get_according_to_mode(self.memory, self.instruction_pointer + 1, first_mode)
            param2 = self.get_according_to_mode(self.memory, self.instruction_pointer + 2, second_mode)
            if opcode == 1:
                self.memory[self.memory[self.instruction_pointer + 3]] = param1 + param2
                self.instruction_pointer += 4
            if opcode == 2:
                self.memory[self.memory[self.instruction_pointer + 3]] = param1 * param2
                self.instruction_pointer += 4
            if opcode == 5:
                self.instruction_pointer = param2 if param1 != 0 else self.instruction_pointer + 3
            if opcode == 6:
                self.instruction_pointer = param2 if param1 == 0 else self.instruction_pointer + 3
            if opcode == 7:
                self.memory[self.memory[self.instruction_pointer + 3]] = 1 if param1 < param2 else 0
                self.instruction_pointer += 4
            if opcode == 8:
                self.memory[self.memory[self.instruction_pointer + 3]] = 1 if param1 == param2 else 0
                self.instruction_pointer += 4


def solution_part_one(input_list: list):
    initial_input = 0
    outputs = list()
    phases = [0, 1, 2, 3, 4]
    permutations = list(itertools.permutations(phases))
    for permutation in permutations:
        outputs.append(amp_software(initial_input, input_list, permutation))
    return max(outputs)


def solution_part_two(input_list: list):
    initial_input = 0
    outputs = list()
    phases = [5, 6, 7, 8, 9]
    permutations = list(itertools.permutations(phases))
    for permutation in permutations:
        outputs.append(amp_software_feedback(initial_input, input_list, permutation))
    return max(outputs)


def amp_software(initial_input, input_list, phases):
    amplifiers = dict()

    amp1_value, amplifiers[1] = IntcodeComputer(input_list.copy(), 0).calculate([phases[0], initial_input])
    amp2_value, amplifiers[2] = IntcodeComputer(input_list.copy(), 0).calculate([phases[1], amp1_value])
    amp3_value, amplifiers[3] = IntcodeComputer(input_list.copy(), 0).calculate([phases[2], amp2_value])
    amp4_value, amplifiers[4] = IntcodeComputer(input_list.copy(), 0).calculate([phases[3], amp3_value])
    amp5_value, amplifiers[5] = IntcodeComputer(input_list.copy(), 0).calculate([phases[4], amp4_value])

    return amp5_value


def amp_software_feedback(initial_input, input_list, phases):
    amplifiers = dict()

    amp1_value, amplifiers[1] = IntcodeComputer(input_list.copy(), 0).calculate([phases[0], initial_input])
    amp2_value, amplifiers[2] = IntcodeComputer(input_list.copy(), 0).calculate([phases[1], amp1_value])
    amp3_value, amplifiers[3] = IntcodeComputer(input_list.copy(), 0).calculate([phases[2], amp2_value])
    amp4_value, amplifiers[4] = IntcodeComputer(input_list.copy(), 0).calculate([phases[3], amp3_value])
    value, amplifiers[5] = IntcodeComputer(input_list.copy(), 0).calculate([phases[4], amp4_value])

    cycle = itertools.cycle(amplifiers.keys())
    while value is not None:
        amplifier_number = next(cycle)
        answer = value
        value, amplifiers[amplifier_number] = amplifiers[amplifier_number].calculate([value])
    return answer


the_list = get_list()
print('Solution for part one is: {}'.format(solution_part_one(the_list)))
print('Solution for part two is: {}'.format(solution_part_two(the_list)))