def to_direction_map(directions: str):
    direction, steps = directions.split(" ")
    return direction, int(steps)


test_input = list(map(to_direction_map, [x for x in open("test_input", 'r').readlines()]))
input = list(map(to_direction_map, [x for x in open("input", 'r').readlines()]))


# idea: sum all forward, up and down command, substract up from down and multiply
def get_position_a(data: list[(str, int)]) -> (int, int):
    forward_sum = sum([x[1] for x in data if x[0] == "forward"])
    down_sum = sum([x[1] for x in data if x[0] == "down"])
    up_sum = sum([x[1] for x in data if x[0] == "up"])

    return forward_sum, down_sum - up_sum


def get_position_b(data: list[(str, int)]) -> (int, int):
    horizontal, depth, aim = (0, 0, 0)
    for inst in data:
        if inst[0] == "forward":
            horizontal += inst[1]
            depth += aim * inst[1]
        elif inst[0] == "up":
            aim -= inst[1]
        elif inst[0] == "down":
            aim += inst[1]

    return horizontal, depth


pos_a = get_position_a(input)
print(f"Position: {pos_a}, Result: {pos_a[0] * pos_a[1]}")

pos_b = get_position_b(input)
print(f"Position: {pos_b}, Result: {pos_b[0] * pos_b[1]}")
