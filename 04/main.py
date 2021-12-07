import numpy as np

test_input = [x.removesuffix('\n') for x in open("test_input", "r").readlines() if x.removesuffix('\n') != '']
input = [x.removesuffix('\n') for x in open("input", "r").readlines() if x.removesuffix('\n') != '']


class Board:
    def __init__(self, values: np.array):
        self.won = False
        self.values = values
        self.marks = np.full((5, 5), False)

    def __repr__(self) -> str:
        return f"{self.won}\n{self.values}\n{self.marks}"

    def mark(self, number):
        self.marks[np.where(self.values == number)] = True

    def has_won(self) -> bool:
        return any([all(row) for row in self.marks]) or \
               any([all(column) for column in self.marks.T])

    def get_score(self, number) -> int:
        unmarked = np.where(self.marks == False)
        sum_unmarked = sum(self.values[unmarked])
        return sum_unmarked * number


def parse_drawings(drawing_input) -> list[int]:
    return [int(x) for x in drawing_input.split(',')]


def parse_boards(board_input) -> list[Board]:
    np_boards = np.array([[int(x) for x in y.split(' ') if x != ""] for y in board_input])
    boards_cnt = int(len(np_boards) / 5)
    boards = []
    for board in np.split(np_boards, boards_cnt):
        boards.append(Board(board))
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

# # part 2
#
# def check_bingo_number(strikes: list[np.array], boards: list[np.array], number: int):
#     for i in range(len(strikes)):
#         for j in range(len(strikes[i])):
#             if all(strikes[i][j]) and number in boards[i][j]:
#                 return i
#         for j in range(len(strikes[i].T)):
#             if all(strikes[i].T[j]) and number in boards[i].T[j]:
#                 return i
#     return -1
#
#
# def process_drawings_full(drawings: list[int], boards: np.array([[int]]), strikes: np.array([[bool]])) \
#         -> (int, list[[int]], list[[bool]]):
#     winning_board_indexes = []
#     winning_boards = []
#     winning_strike_boards = []
#     winning_numbers = []
#     for number in drawings:
#         for i in range(len(boards)):
#             index = np.where(boards[i] == number)
#             if index[0].size > 0:
#                 strikes[i][index] = True
#         bingo_board = check_bingo(strikes)
#         if bingo_board != -1:
#             winning_boards.append(boards[bingo_board])
#             winning_strike_boards.append(strikes[bingo_board])
#             winning_numbers.append(number)
#             del boards[bingo_board]
#             del strikes[bingo_board]
#     print(winning_boards[-1])
#     return winning_numbers[-1], winning_boards[-1], winning_strike_boards[-1]
#
#
# parsed_drawings = parse_drawings(input[0])
# parsed_boards = parse_boards(input[1:])
# initial_strikes = [np.full((5, 5), False) for board in parsed_boards]
# winning_number, winning_board, winning_strikes = process_drawings_full(parsed_drawings, parsed_boards, initial_strikes)
# print(calculate_score(winning_number, winning_board, winning_strikes))
