import day4


def test_six_digits():
    assert not day4.is_max_six_digits(5000)
    assert not day4.is_max_six_digits(9999)
    assert day4.is_max_six_digits(100000)
    assert not day4.is_max_six_digits(1000000)


def test_two_adjacent_digits_are_the_same():
    assert not day4.two_adjacent_digits_are_the_same(123456)
    assert day4.two_adjacent_digits_are_the_same(123455)


def test_exactly_two_adjacent_digits_are_the_same():
    assert not day4.exactly_two_adjacent_digits_are_the_same(123444)
    assert day4.exactly_two_adjacent_digits_are_the_same(112233)
    assert day4.exactly_two_adjacent_digits_are_the_same(111122)