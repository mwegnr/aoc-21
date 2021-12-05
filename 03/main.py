from statistics import mode
import numpy as np

test_input = [[int(y) for y in x.removesuffix('\n')] for x in open("test_input", 'r').readlines()]
input = [x.removesuffix('\n') for x in open("input", 'r').readlines()]


# part one

def calculate_gamma(data: list[str]) -> str:
    array = np.array(data)
    gamma = ''.join([str(mode(i)) for i in array.T])
    return gamma


def calculate_epsilon(gamma: str) -> str:
    return ''.join('1' if x == '0' else '0' for x in gamma)


def calculate_power_consumption(gamma: str, epsilon: str) -> int:
    gamma_int = int(gamma, 2)
    epsilon_int = int(epsilon, 2)
    return gamma_int * epsilon_int


# print(test_input)
gamma = calculate_gamma(test_input)
epsilon = calculate_epsilon(gamma)
print(calculate_power_consumption(gamma, epsilon))

# part two

# def calculate_oxygen_gen_rating(data: list[str], gamma: str):
