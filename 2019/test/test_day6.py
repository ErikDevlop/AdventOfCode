import day6


def fake_input_data() -> dict:
    input_file = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L', 'K)YOU', 'I)SAN']
    orbits_map = dict()
    for line in input_file:
        key_value = line.strip().split(')')
        orbits_map[key_value[1]] = key_value[0]
    return orbits_map


def test_solution_part_two():
    assert day6.solution_part_two(fake_input_data()) == 4
