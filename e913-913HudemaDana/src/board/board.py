import texttables


class Board:
    def __init__(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    @property
    def get_board(self):
        return self.board

    def verify_place(self, row, column, value):
        """
        verifica celalalt loc
        :param row:
        :param column:
        :param value:
        :return:
        """
        if self.board[row][column] == " ":
            self.board[row][column] = value
        else:
            raise ValueError("Invalid input. Try again")

    def verify_place1(self, row, column, a, b):
        """
        verifica locul
        :param row:
        :param column:
        :param a:
        :param b:
        :return:
        """
        if self.board[row][column] != "X":
            raise ValueError("Incorrect input. Try again")
        if (row == a - 1 or row == a or row == a + 1) and (column == b - 1 or column == b or column == b + 1):
            self.board[a][b] = 'X'
            return row, column
        else:
            raise ValueError("Invalid input. You cannot move that piece")

    def verify_diagonal(self):
        """
        testeaza diagonala
        :return:
        """
        row, column = -1, -1
        if self.board[0][0] == self.board[1][1] and self.board[0][0] == 'X':
            row = 2
            column = 2
        elif self.board[0][0] == self.board[2][2] and self.board[0][0] == 'X':
            row = 1
            column = 1
        elif self.board[1][1] == self.board[2][2] and self.board[2][2] == 'X':
            row = 0
            column = 0

        elif self.board[0][2] == self.board[1][1] and self.board[0][2] == 'X':
            row = 2
            column = 0
        elif self.board[0][2] == self.board[2][0] and self.board[0][2] == 'X':
            row = 1
            column = 1
        elif self.board[1][1] == self.board[2][0] and self.board[2][0] == 'X':
            row = 0
            column = 2

        if self.board[row][column] == ' ' and row != -1:
            return row, column
        return -1, -1

    def verify_column(self):
        """

        testeaza coloana
        :return:
        """
        row, column = -1, -1
        if self.board[0][0] == self.board[1][0] and self.board[0][0] == 'X':
            row = 0
            column = 2
        elif self.board[0][1] == self.board[1][1] and self.board[0][1] == 'X':
            row = 1
            column = 2
        elif self.board[0][2] == self.board[1][2] and self.board[0][2] == 'X':
            row = 2
            column = 2

        elif self.board[0][0] == self.board[2][0] and self.board[0][0] == 'X':
            row = 0
            column = 1
        elif self.board[0][1] == self.board[2][1] and self.board[0][1] == 'X':
            row = 1
            column = 1
        elif self.board[0][2] == self.board[2][2] and self.board[0][2] == 'X':
            row = 2
            column = 1

        elif self.board[1][0] == self.board[2][0] and self.board[1][0] == 'X':
            row = 0
            column = 0
        elif self.board[1][1] == self.board[2][1] and self.board[1][1] == 'X':
            row = 1
            column = 0
        elif self.board[1][2] == self.board[2][2] and self.board[1][2] == 'X':
            row = 2
            column = 0

        if self.board[column][row] == ' ' and row != -1:
            return column,row
        return -1, -1

    def verify_line(self):
        """
        testeaza linia
        :return:
        """
        row, column = -1, -1
        if self.board[0][0] == self.board[0][1] and self.board[0][0] == 'X':
            row = 0
            column = 2
        elif self.board[1][0] == self.board[1][1] and self.board[1][0] == 'X':
            row = 1
            column = 2
        elif self.board[2][0] == self.board[2][1] and self.board[2][0] == 'X':
            row = 2
            column = 2

        elif self.board[0][0] == self.board[0][2] and self.board[0][0] == 'X':
            row = 0
            column = 1
        elif self.board[1][0] == self.board[1][2] and self.board[1][0] == 'X':
            row = 1
            column = 1
        elif self.board[2][0] == self.board[2][2] and self.board[2][0] == 'X':
            row = 2
            column = 1

        elif self.board[0][1] == self.board[0][2] and self.board[0][1] == 'X':
            row = 0
            column = 0
        elif self.board[1][1] == self.board[1][2] and self.board[1][1] == 'X':
            row = 1
            column = 0
        elif self.board[2][1] == self.board[2][2] and self.board[2][1] == 'X':
            row = 2
            column = 0

        if self.board[row][column] == ' ' and row !=-1:
            return row, column
        return -1,-1

    def win(self):
        """
        testeaza daca castiga
        :return:
        """
        for i in range(0, 3):
            if self.board[i][0] == self.board[i][1] and self.board[i][1] == \
                    self.board[i][2] and self.board[i][0] == "X":
                return True
            if self.board[0][i] == self.board[1][i] and self.board[1][i] == \
                    self.board[2][i] and self.board[0][i] == "X":
                return True
        if self.board[1][1] == self.board[0][0] and self.board[1][1] == \
                self.board[2][2] == 'X':
            return True
        if self.board[0][2] == self.board[1][1] and self.board[1][1] == \
                self.board[2][0] == 'X':
            return True

        return False


def test_line():
    b = Board()
    b.get_board[0][0], b.get_board[0][1] = 'X', 'X'
    assert b.verify_line() == (0, 2)

    b.get_board[1][0] = 'X'
    assert b.verify_column() == (2, 0)


test_line()
