import random


class Computer:
    def __init__(self, board):
        self.board = board

    def first_place_O_for_computer(self):
        row = random.randint(0, 2)
        column = random.randint(0, 2)
        while self.board.get_board[row][column] == "X" or self.board.get_board[row][column] == 'O':
            row = random.randint(0, 2)
            column = random.randint(0, 2)

        return row, column

    def place_to_not_win(self):
        row, column = self.board.verify_line()
        if row == column and row == -1:
            row, column = self.board.verify_column()
            if row == column and row == -1:
                row, column = self.board.verify_diagonal()
                if row == column and row == -1:
                    row, column = self.first_place_O_for_computer()

        return row, column

    def move_computer(self, a, b):
        row = random.randint(0, 2)
        column = random.randint(0, 2)
        while self.board.get_board[row][column] != 'O' and not (
                (row == a - 1 or row == a or row == a + 1) and (column == b - 1 or column == b or column == b + 1)):
            row = random.randint(0, 2)
            column = random.randint(0, 2)
        self.board.get_board[a][b] = 'O'
        self.board.get_board[row][column] = " "
        return row, column

    def win_computer(self):
        for i in range(0, 3):
            if self.board.get_board[i][0] == self.board.get_board[i][1] and self.board.get_board[i][1] == \
                    self.board.get_board[i][2] and self.board.get_board[i][0] == 'O':
                return True
            if self.board.get_board[0][i] == self.board.get_board[1][i] and self.board.get_board[1][i] == \
                    self.board.get_board[2][i] and self.board.get_board[0][i] == 'O':
                return True
        if self.board.get_board[1][1] == self.board.get_board[0][0] and self.board.get_board[1][1] == \
                self.board.get_board[2][2] == 'O':
            return True
        if self.board.get_board[0][2] == self.board.get_board[1][1] and self.board.get_board[1][1] == \
                self.board.get_board[2][0] == 'O':
            return True

        return False
