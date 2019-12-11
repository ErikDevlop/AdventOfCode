import os


def get_list() -> list:
    filepath = os.path.join(os.path.dirname(__file__), '../resource/input9.txt')
    with open(filepath) as fp:
        line = fp.readline()
        input_list = list()
        while line:
            input_list.extend(line.split(","))
            line = fp.readline()
        return [int(i) for i in input_list]


class IntcodeComputer(object):

    def __init__(self, memory: list):
        self.memory = memory + [0 for _ in range(1000)]
        self.instruction_pointer = 0
        self.relative_base = 0

    @staticmethod
    def get_mode_and_opcode(instruction_input: int) -> (int, int, int, int):
        string_input = str(instruction_input).zfill(5)
        return int(string_input[0]), int(string_input[1]), int(string_input[2]), int(string_input[-2:])

    @staticmethod
    def is_position_mode(mode: int) -> bool:
        return mode == 0

    @staticmethod
    def is_immediate_mode(mode: int) -> bool:
        return mode == 1

    @staticmethod
    def is_relative_mode(mode: int) -> bool:
        return mode == 2

    def get_pointer(self, offset: int, mode: int):
        pointer = self.instruction_pointer + offset
        if self.is_position_mode(mode):
            return self.get(pointer)
        elif self.is_immediate_mode(mode):
            return pointer
        elif self.is_relative_mode(mode):
            return self.relative_base + self.get(pointer)

    def get(self, pointer: int) -> int:
        length = len(self.memory)
        if pointer < length:
            return self.memory[pointer]
        else:
            print('Error: Length was {}, wanted to access {}'.format(length, pointer))
            return 0

    def calculate(self, input_list):
        outputs = list()
        while True:
            third_mode, second_mode, first_mode, opcode = self.get_mode_and_opcode(self.get(self.instruction_pointer))
            if opcode not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 99]:
                print('Opcode {} is not supported'.format(opcode))
                break
            if opcode == 99:
                return outputs
            pointer1 = self.get_pointer(1, first_mode)
            pointer2 = self.get_pointer(2, second_mode)
            pointer3 = self.get_pointer(3, third_mode)
            if opcode == 1:
                self.memory[pointer3] = self.get(pointer1) + self.get(pointer2)
                self.instruction_pointer += 4
            elif opcode == 2:
                self.memory[pointer3] = self.get(pointer1) * self.get(pointer2)
                self.instruction_pointer += 4
            elif opcode == 3:
                self.memory[pointer1] = input_list.pop(0)
                self.instruction_pointer += 2
            elif opcode == 4:
                outputs.append(self.get(pointer1))
                self.instruction_pointer += 2
            elif opcode == 5:
                self.instruction_pointer = self.get(pointer2) if self.get(pointer1) != 0 else self.instruction_pointer + 3
            elif opcode == 6:
                self.instruction_pointer = self.get(pointer2) if self.get(pointer1) == 0 else self.instruction_pointer + 3
            elif opcode == 7:
                self.memory[pointer3] = 1 if self.get(pointer1) < self.get(pointer2) else 0
                self.instruction_pointer += 4
            elif opcode == 8:
                self.memory[pointer3] = 1 if self.get(pointer1) == self.get(pointer2) else 0
                self.instruction_pointer += 4
            elif opcode == 9:
                self.relative_base += self.get(pointer1)
                self.instruction_pointer += 2


def solution(initial_memory: list, input_list: list):
    return IntcodeComputer(initial_memory).calculate(input_list)


program = get_list()
print('Solution for part one is: {}'.format(solution(program, [1])))
print('Solution for part two is: {}'.format(solution(program, [2])))
