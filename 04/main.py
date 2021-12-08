import numpy as np

test_input = [x.removesuffix('\n') for x in open("test_input", "r").readlines() if x.removesuffix('\n') != '']
input = [x.removesuffix('\n') for x in open("input", "r").readlines() if x.removesuffix('\n') != '']


class Board:
    def __init__(self, values: np.array):
        self.won = False
        self.values = values
        self.marks = np.full((5, 5), False)
        self.last_number = -1

    def __repr__(self) -> str:
        return f"{self.won}\n{self.values}\n{self.marks}"

    def mark(self, number: int):
        self.marks[np.where(self.values == number)] = True

    def set_last_number(self, number: int):
        self.last_number = number

    def has_won(self) -> bool:
        if not self.won:
            self.won = \
                any([all(row) for row in self.marks]) or \
                any([all(column) for column in self.marks.T])
        return self.won

    def get_score(self, number: int = -1) -> int:
        if number == -1:
            number = self.last_number

        unmarked = np.where(self.marks == False)
        sum_unmarked = sum(self.values[unmarked])
        return sum_unmarked * number


def parse_drawings(drawing_input: str) -> list[int]:
    return [int(x) for x in drawing_input.split(',')]


def parse_boards(board_input: list[str]) -> list[Board]:
    np_boards = np.array([[int(x) for x in y.split(' ') if x != ""] for y in board_input])
    boards_cnt = int(len(np_boards) / 5)

    boards = [Board(x) for x in np.split(np_boards, boards_cnt)]
    return boards


def get_first_won_score(drawings: list[int], boards: [Board]) -> int:
    for number in drawings:
        for board in boards:
            board.mark(number)
            if board.has_won():
                return board.get_score(number)
    return -1


parsed_drawings = parse_drawings(input[0])
parsed_boards = parse_boards(input[1:])

print(get_first_won_score(parsed_drawings, parsed_boards))


# part 2
def get_last_won_score(drawings: list[int], boards: [Board]) -> int:
    won_boards = []
    for number in drawings:
        for board in boards:
            if board not in won_boards:
                board.mark(number)
                if board.has_won():
                    board.set_last_number(number)
                    won_boards.append(board)
    return won_boards[-1].get_score()


parsed_drawings = parse_drawings(input[0])
parsed_boards = parse_boards(input[1:])

print(get_last_won_score(parsed_drawings, parsed_boards))
