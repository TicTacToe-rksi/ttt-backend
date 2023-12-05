class TicTacToe:
    def __init__(self, _area: list):
        self.area = _area
        self.size = len(area)

    def __str__(self):
        board = ""
        for line in self.area:
            board += f"{line}\n"
        return board

    @classmethod
    def create(cls, size: int):
        board = []
        for _ in range(size):
            line = []
            for _ in range(size):
                line.append(None)
            board.append(line)

        return board

    @property
    def finished(self):
        return not self.winner is None or self.filled

    @property
    def winner(self):
        # Проверка по горизонтали
        for row in self.area:
            if all([cell == 0 for cell in row]):
                return 0
            elif all([cell == 1 for cell in row]):
                return 1

        # Проверка по вертикали
        for col in range(3):
            if all([self.area[row][col] == 0 for row in range(3)]):
                return 0
            if all([self.area[row][col] == 1 for row in range(3)]):
                return 1

        # Проверка по диагоналям
        if all([self.area[i][i] == 0 for i in range(3)]) or all([self.area[i][2 - i] == 0 for i in range(3)]):
            return 0
        elif all([self.area[i][i] == 1 for i in range(3)]) or all([self.area[i][2 - i] == 1 for i in range(3)]):
            return 1
        return None

    @property
    def filled(self):
        if all([cell is not None for row in self.area for cell in row]):
            return True
        return False

    def is_move_of(self, cross_zero: int) -> bool:
        cross_zero = int(bool(cross_zero))
        cross, zero = 0, 0

        for line in self.area:
            for col in line:
                if col == 0:
                    zero += 1
                elif col == 1:
                    cross += 1

        if cross <= zero and cross_zero == 1:
            return True
        elif zero < cross and cross_zero == 0:
            return True
        return False

    def can_move(self, cross_zero: int, line: int, column: int) -> bool:
        if not self.is_move_of(cross_zero):
            return False
        elif not self.area[line][column] is None:
            return False
        elif self.filled or self.finished:
            return False
        return True

    def move(self, cross_zero: int, line: int, column: int):
        if not self.can_move(cross_zero, line, column):
            return None

        self.area[line][column] = int(bool(cross_zero))
        return self.area


# area = TicTacToe.create(3)
# game = TicTacToe(area)
# print(game.move(1, 1, 1))
# print(game.move(0, 2, 2))
#
# print(game.move(1, 0, 1))
# print(game.move(0, 0, 2))
#
# print(game.move(1, 2, 1))
# print(game.move(0, 1, 2))
#
# print(game)
#
#
# print(game.finished, game.winner, game.filled)
