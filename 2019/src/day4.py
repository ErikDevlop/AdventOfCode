import re


def is_max_six_digits(number: int) -> bool:
    return 1000000 > number > 99999


def two_adjacent_digits_are_the_same(number: int) -> bool:
    last_digit = str(number)[0]
    group_of_digits = list(last_digit)
    for n in str(number)[1:]:
        if last_digit == n:
            group_of_digits[-1] = group_of_digits[-1] + n
        else:
            group_of_digits.append(n)
        last_digit = n
    for group in group_of_digits:
        if len(group) > 1:
            return True
    return False


def have_increasing_digits(number: int) -> bool:
    digits = [int(n) for n in str(number)]
    last_digits = digits[0]
    for d in digits:
        if d < last_digits:
            return False
        last_digits = d
    return True


def solution_one(possible_values):
    number_meeting_criteria = 0
    for value in possible_values:
        if is_max_six_digits(value) and two_adjacent_digits_are_the_same(value) and have_increasing_digits(value):
            number_meeting_criteria += 1
    return number_meeting_criteria


def exactly_two_adjacent_digits_are_the_same(number: int) -> bool:
    last_digit = str(number)[0]
    group_of_digits = list(last_digit)
    for n in str(number)[1:]:
        if last_digit == n:
            group_of_digits[-1] = group_of_digits[-1] + n
        else:
            group_of_digits.append(n)
        last_digit = n
    for group in group_of_digits:
        if len(group) == 2:
            return True
    return False


def solution_two(possible_values):
    number_meeting_criteria = 0
    for value in possible_values:
        if is_max_six_digits(value) and exactly_two_adjacent_digits_are_the_same(value) and have_increasing_digits(value):
            number_meeting_criteria += 1
    return number_meeting_criteria


input_range = range(240920, 789857 + 1)
print('The answer for part one is {}'.format(solution_one(input_range)))

print('The answer for part two is {}'.format(solution_two(input_range)))
