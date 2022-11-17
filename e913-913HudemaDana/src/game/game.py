import texttable


class Game:
    def __init__(self, computer, board):
        self.computer = computer
        self.board_game = board

    def menu_print(self):
        print("-----------------------------")
        print("            ACHI             ")
        print("-----------------------------\n")

        a = input("Press space to start: ")

    def afisare_board(self):
        board = texttable.Texttable()
        board.add_rows([self.board_game.get_board[0], self.board_game.get_board[1], self.board_game.get_board[2]])
        print(board.draw())

    def place_on_the_board(self):
        ok = False
        while ok == False:
            try:
                row = int(input("Choose Row: "))
                column = int(input("Choose Column: "))
                self.board_game.verify_place(row, column, 'X')
                ok = True
            except ValueError as ve:
                print(ve)

    def move_player(self, a, b):
        try:
            row = int(input("Choose Row: "))
            column = int(input("Choose Column: "))
            i, j = self.board_game.verify_place1(row, column, a, b)
            self.board_game.get_board[row][column] = " "
            return i, j
        except ValueError as ve:
            print(ve)

    def find_free_spot(self):
        """
        finds the free spot to start the movement part of the game
        """
        free_row = 0
        free_column = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if self.board_game.get_board[i][j] == " ":
                    free_row = i
                    free_column = j

        return free_row, free_column

    def controller1(self):
        self.menu_print()

        for i in range(1, 5):
            self.afisare_board()
            self.place_on_the_board()
            row, column = self.computer.place_to_not_win()
            print(row,column)
            self.board_game.get_board[row][column] = 'O'

            if self.computer.win_computer() == True:
                print("BOOOOOHOOOO, COMPUTER WOOOOOOOON")
                return

            if self.board_game.win() == True:
                print("YOU ARE AMAIZING. CONGRATS")
                return

        print("-----------------------------")
        print("PART 2 OF THE GAME")
        print("-----------------------------")

        free_row, free_column = self.find_free_spot()

        print(free_row,free_column)

        while self.computer.win_computer() == False and self.board_game.win() == False:
            self.afisare_board()
            free_row, free_column = self.move_player(free_row, free_column)
            if self.board_game.win() == True:
                print("YOU ARE AMAIZING. CONGRATS")
                return
            self.afisare_board()
            free_row, free_column = self.computer.move_computer(free_row, free_column)
            if self.computer.win_computer() == True:
                self.afisare_board()
                print("BOOOOOHOOOO, COMPUTER WOOOOOOOON")
                return
