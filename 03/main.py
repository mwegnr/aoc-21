from statistics import mode

test_input = [x.removesuffix('\n') for x in open("test_input", 'r').readlines()]
input = [x.removesuffix('\n') for x in open("input", 'r').readlines()]


def calculate_gamma(data: list[str]) -> str:
    diagnostic_length = len(data[0])
    bit_lists = [[] for _ in range(diagnostic_length)]
    for line in data:
        for i in range(len(line)):
            bit_lists[i].append(line[i])
    gamma = ''.join([mode(sublist) for sublist in bit_lists])
    return gamma


def calculate_epsilon(gamma: str) -> str:
    return ''.join('1' if x == '0' else '0' for x in gamma)


def calculate_power_consumption(gamma: str, epsilon: str) -> int:
    gamma_int = int(gamma, 2)
    epsilon_int = int(epsilon, 2)
    return gamma_int * epsilon_int


gamma = calculate_gamma(input)
epsilon = calculate_epsilon(gamma)
print(calculate_power_consumption(gamma, epsilon))
