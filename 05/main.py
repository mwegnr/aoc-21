import re
import numpy as np

test_input = [x.removesuffix('\n') for x in open("test_input", "r").readlines() if x.removesuffix('\n') != '']
input = [x.removesuffix('\n') for x in open("input", "r").readlines() if x.removesuffix('\n') != '']


class Line:
    def __init__(self, line):
        self.x1, self.y1, self.x2, self.y2 = map(int, re.search(r"(\d+),(\d+) -> (\d+),(\d+)", line).groups())
        if not self.is_diagonal():
            temp_x1, temp_y1, temp_x2, temp_y2 = (self.x1, self.y1, self.x2, self.y2)
            self.x1 = min(temp_x1, temp_x2)
            self.x2 = max(temp_x1, temp_x2)
            self.y1 = min(temp_y1, temp_y2)
            self.y2 = max(temp_y1, temp_y2)

    def __repr__(self) -> str:
        return f"({self.x1}, {self.y1}) -> ({self.x2}, {self.y2})"

    def is_diagonal(self) -> bool:
        return self.x1 != self.x2 and self.y1 != self.y2

    def is_horizontal(self) -> bool:
        return self.x1 == self.x2 and self.y1 != self.y2

    def is_vertical(self) -> bool:
        return self.x1 != self.x2 and self.y1 == self.y2

    def get_max_x(self) -> int:
        return max(self.x1, self.x2)

    def get_max_y(self) -> int:
        return max(self.y1, self.y2)


def parse_lines(line_input: list[str]) -> list[Line]:
    return [Line(line) for line in line_input]


def get_field(lines: list[Line]) -> np.array:
    max_x = max([line.get_max_x() for line in lines]) + 1
    max_y = max([line.get_max_y() for line in lines]) + 1
    return np.zeros((max_x, max_y))


def draw_lines(lines: list[Line], diagonals: bool = False) -> np.array:
    field = get_field(lines)
    for line in lines:
        if line.is_horizontal():
            field[line.x1, line.y1:line.y2 + 1] += 1
        if line.is_vertical():
            field[line.x1:line.x2 + 1, line.y1] += 1
        if line.is_diagonal() and diagonals:
            if line.x1 < line.x2 and line.y1 < line.y2:
                for i in range(line.x2 - line.x1 + 1):
                    field[line.x1 + i][line.y1 + i] += 1
            elif line.x1 < line.x2 and line.y1 > line.y2:
                for i in range(line.x2 - line.x1 + 1):
                    field[line.x1 + i][line.y1 - i] += 1
            elif line.x1 > line.x2 and line.y1 < line.y2:
                for i in range(line.x1 - line.x2 + 1):
                    field[line.x1 - i][line.y1 + i] += 1
            elif line.x1 > line.x2 and line.y1 > line.y2:
                for i in range(line.x1 - line.x2 + 1):
                    field[line.x1 - i][line.y1 - i] += 1
    print(field.T)
    return field.T


parsed_lines = parse_lines(input)
print([line for line in parsed_lines if line.is_diagonal()])
drawn_field = draw_lines(parsed_lines)
print(np.count_nonzero(drawn_field > 1))

# part 2 - WIP
drawn_field = draw_lines(parsed_lines, diagonals=True)
print(np.count_nonzero(drawn_field > 1))
