import math
from util import read_input


def get_reactions():
    reactions = dict()
    for line in read_input('input14.txt'):
        input_chemicals, output_chemical = line.split('=>')
        reaction = list()
        for chemicals in input_chemicals.split(','):
            quantity, chemical = chemicals.strip().split(' ')
            reaction.append((int(quantity), chemical))
        quantity, chemical = output_chemical.strip().split(' ')
        reactions[(int(quantity), chemical)] = reaction
    return reactions


def get_input_chemicals(reactions: dict, chemical: str):
    for output_chemicals in reactions.keys():
        if output_chemicals[1] == chemical:
            return reactions[output_chemicals]


def sum_chemicals(reactions):
    summed_elements = list()
    for reaction in reactions:
        if reaction[1] in [element[1] for element in summed_elements]:
            for index, element in enumerate(summed_elements):
                if element[1] == reaction[1]:
                    summed_elements[index] = (reaction[0] + element[0], reaction[1])
        else:
            summed_elements.append(reaction)
    return summed_elements


def get_multiple(reactions: list, component: (int, str)):
    for output_chemicals in reactions.keys():
        if output_chemicals[1] == component[1]:
            return math.ceil(float(component[0]) / float(output_chemicals[0]))


def multiply_list(input_chemicals, multiple):
    return [(input_chemical[0] * multiple, input_chemical[1]) for input_chemical in input_chemicals]


def get_depth(reactions, chemical, depth):
    input_chemicals = get_input_chemicals(reactions, chemical[1])
    if input_chemicals is None:
        return 0
    elif input_chemicals[0][1] == 'ORE':
        return depth
    else:
        return max([get_depth(reactions, input_chemical, depth + 1) for input_chemical in input_chemicals])


def get_max_depth(reactions, input_chemicals):
    depths = dict()
    for input_chemical in input_chemicals:
        depths[get_depth(reactions, input_chemical, 1)] = input_chemical
    return depths[max(depths.keys())]


def cost_of_fuel(number_fuel):
    reactions = get_reactions()
    input_chemicals = multiply_list(reactions[(1, 'FUEL')], number_fuel)
    while True:
        input_chemical = get_max_depth(reactions, input_chemicals)
        input_chemicals.remove(input_chemical)
        input_chemicals.extend(multiply_list(get_input_chemicals(reactions, input_chemical[1]), get_multiple(reactions, input_chemical)))
        input_chemicals = sum_chemicals(input_chemicals)
        if len(input_chemicals) == 1:
            return input_chemicals[0][0]


def find_maximum_under(limit: int):
    low = 0
    high = limit
    while low < high:
        guess = (low + high + 1) // 2
        if cost_of_fuel(guess) <= limit:
            low = guess
        else:
            high = guess - 1
    return guess


NUMBER_OF_ORE = 1000000000000
print('Solution for part one is {}'.format(cost_of_fuel(1)))
print('Solution for part one is {}'.format(find_maximum_under(NUMBER_OF_ORE)))

