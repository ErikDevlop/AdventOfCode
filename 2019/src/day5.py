import os


def get_list() -> list:
    filepath = os.path.join(os.path.dirname(__file__), '../resource/input5.txt')
    with open(filepath) as fp:
        line = fp.readline()
        input_list = list()
        while line:
            input_list.extend(line.split(","))
            line = fp.readline()
        return [int(i) for i in input_list]


def get_mode_and_opcode(instruction_input: int) -> (int, int, int, int):
    string_input = str(instruction_input)
    if len(string_input) == 5:
        return int(string_input[-5:-4]), int(string_input[-4:-3]), int(string_input[-3:-2]), int(string_input[-2:])
    if len(string_input) == 4:
        return 0, int(string_input[-4:-3]), int(string_input[-3:-2]), int(string_input[-2:])
    if len(string_input) == 3:
        return 0, 0, int(string_input[-3:-2]), int(string_input[-2:])
    if len(string_input) == 2:
        return 0, 0, 0, int(string_input[-2:])
    if len(string_input) == 1:
        return 0, 0, 0, int(string_input[-1:])
    return 0, 0, 0, 0


def is_immediate_mode(mode: int) -> bool:
    return mode == 1


def get_according_to_mode(memory: list, pointer: int, mode: int):
    length = len(memory)
    if is_immediate_mode(mode) and pointer < length:
        return memory[pointer]
    elif memory[pointer] < length:
        return memory[memory[pointer]]
    else:
        print('error')
        return 0


def solution(memory) -> int:
    instruction_pointer = 0
    while True:
        third_mode, second_mode, first_mode, opcode = get_mode_and_opcode(memory[instruction_pointer])
        if opcode == 99:
            break
        param1 = get_according_to_mode(memory, instruction_pointer + 1, first_mode)
        param2 = get_according_to_mode(memory, instruction_pointer + 2, second_mode)
        if opcode == 1:
            memory[memory[instruction_pointer + 3]] = param1 + param2
            instruction_pointer += 4
        if opcode == 2:
            memory[memory[instruction_pointer + 3]] = param1 * param2
            instruction_pointer += 4
        if opcode == 3:
            memory[memory[instruction_pointer + 1]] = int(input("Please enter a number: "))
            instruction_pointer += 2
        if opcode == 4:
            print(memory[memory[instruction_pointer + 1]])
            instruction_pointer += 2
        if opcode == 5:
            instruction_pointer = param2 if param1 != 0 else instruction_pointer + 3
        if opcode == 6:
            instruction_pointer = param2 if param1 == 0 else instruction_pointer + 3
        if opcode == 7:
            memory[memory[instruction_pointer + 3]] = 1 if param1 < param2 else 0
            instruction_pointer += 4
        if opcode == 8:
            memory[memory[instruction_pointer + 3]] = 1 if param1 == param2 else 0
            instruction_pointer += 4


solution(get_list())
