from src.game.game import Game
from src.computer.computer import Computer
from src.board.board import Board

def main():
    board = Board()
    computer = Computer(board)
    game = Game(computer,board)
    game.controller1()

main()