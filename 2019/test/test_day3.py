import day3


def test_day3_closest_1():
    assert day3.solution_closest(['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'],
                         ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']) == 159


def test_day3_closest_2():
    assert day3.solution_closest(['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'],
                         ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']) == 135


def test_day3_shortest_1():
    assert day3.solution_shortest(['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'],
                         ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']) == 610


def test_day3_shortest_2():
    assert day3.solution_shortest(['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'],
                         ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']) == 410
