from collections import Counter

import numpy as np

test_input = np.array([[int(y) for y in x.removesuffix('\n')] for x in open("test_input", 'r').readlines()])
input = np.array([[int(y) for y in x.removesuffix('\n')] for x in open("input", 'r').readlines()])


# part one

def mode(data: iter, default: object = 1, least_common=False) -> object:
    cnt = Counter(data).most_common()
    if cnt[0][1] == cnt[1][1]:
        return default
    if least_common:
        return cnt[1][0]
    return cnt[0][0]


def calculate_gamma(data: np.array) -> str:
    return ''.join([str(mode(i)) for i in data.T])


def calculate_epsilon(gamma: str) -> str:
    return ''.join('1' if x == '0' else '0' for x in gamma)


def calculate_power_consumption(gamma: str, epsilon: str) -> int:
    return int(gamma, 2) * int(epsilon, 2)


#
# print(test_input)
# gamma = calculate_gamma(test_input)
# epsilon = calculate_epsilon(gamma)
# print(calculate_power_consumption(gamma, epsilon))
#

#
# part two

def calculate_oxygen_gen_rating(data: np.array) -> int:
    for i in range(data.shape[1]):
        current_mode = mode(data.T[i])
        data = data[np.where(data.T[i] == current_mode)]
        if data.shape[0] == 1:
            break
    return int(''.join(map(str, data[0])), 2)


def calculate_co2_scrubber_rating(data: np.array) -> int:
    for i in range(data.shape[1]):
        current_mode = mode(data.T[i], default=0, least_common=True)
        data = data[np.where(data.T[i] == current_mode)]
        if data.shape[0] == 1:
            break
    return int(''.join(map(str, data[0])), 2)


print(calculate_oxygen_gen_rating(input) * calculate_co2_scrubber_rating(input))
