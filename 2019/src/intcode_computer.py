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

    def calculate(self, inputs: list):
        while True:
            third_mode, second_mode, first_mode, opcode = self.get_mode_and_opcode(self.get(self.instruction_pointer))
            if opcode not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 99]:
                print('Opcode {} is not supported'.format(opcode))
                break
            if opcode == 99:
                break
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
                if len(inputs) != 0:
                    self.memory[pointer1] = inputs.pop(0)
                    self.instruction_pointer += 2
            elif opcode == 4:
                yield self.get(pointer1)
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
