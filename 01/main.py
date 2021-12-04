test_input = [int(x) for x in open("testinput", 'r').readlines()]
input = [int(x) for x in open("input", 'r').readlines()]


def count_increases(data: list[int]) -> int:
    counter = 0
    for i in range(len(data) - 1):
        if data[i] < data[i + 1]:
            counter += 1
    return counter


def count_increases_steps(data: list[int], step_size: int = 3) -> int:
    counter = 0
    for i in range(len(data) - step_size):
        i_sum = sum(data[i:i + step_size])
        j_sum = sum(data[i + 1:i + 1 + step_size])
        if i_sum < j_sum:
            counter += 1
    return counter


# print(count_increases(input))
print(count_increases_steps(input))
