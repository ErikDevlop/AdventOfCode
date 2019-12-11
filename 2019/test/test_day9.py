import day9


def test_output_program():
    program = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
    assert day9.solution_part_one(program, []) == program


def test_16_digits_output():
    program = [1102, 34915192, 34915192, 7, 4, 7, 99, 0]
    assert len(str(day9.solution_part_one(program, [])[0])) == 16


def test_middle_output():
    program = [104, 1125899906842624, 99]
    assert day9.solution_part_one(program, [])[0] == program[1]
