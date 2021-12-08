import numpy as np
import math

input = [int(x) for x in open("input", "r").readlines()[0].split(",")]
test_input = [int(x) for x in open("test_input", "r").readlines()[0].split(",")]


# part 1
def get_fuel_consumption_linear(values: list[int]):
    med = np.median(values)
    differences = [abs(x - med) for x in values]
    return sum(differences)


print(get_fuel_consumption_linear(input))


# part 2
def triangular_number(n):
    return n * (n + 1) / 2


def get_fuel_consumption_part_2(values: list[int]):
    # after looking at other solutions i found out, that the optimal point is between mean(values) +- 0.5
    # while using the lower and upper quantile works, this would have been a much more efficient solution
    lower = math.floor(np.quantile(values, 0.25))
    upper = math.ceil(np.quantile(values, 0.75))
    fuel_consumptions = [sum([triangular_number(abs(x - i)) for x in values]) for i in range(lower, upper + 1)]
    return min(fuel_consumptions)


print(get_fuel_consumption_part_2(input))
