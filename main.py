from os import system
from random import choice


class GameBoard:
    def __init__(self):
        self.squares = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.turn = choice(['X', 'O'])
        self.game_over = None

    def make_move(self, square: int):
        try:
            move = self.squares.index(int(square))
        except ValueError:
            print("Bad move!")
        else:
            self.squares[move] = self.turn

    def toggle_turn(self):
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

    def check_for_win(self):
        winners = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for combo in winners:
            win = self.check_squares(combo[0], combo[1], combo[2])
            if win:
                return True
        return False

    def check_squares(self, x, y, z):
        if self.squares[x] == self.squares[y] == self.squares[z]:
            return self.squares[0]

    def display(self):
        clear_console()
        print()
        print(self.squares[0], self.squares[1], self.squares[2], sep=" | ")
        print("--+---+--")
        print(self.squares[3], self.squares[4], self.squares[5], sep=" | ")
        print("--+---+--")
        print(self.squares[6], self.squares[7], self.squares[8], sep=" | ")
        print()


def clear_console():
    system('clear')


board = GameBoard()
board.display()

while not board.game_over:
    print(board.turn + "'s turn...")
    try:
        move = int(input("Which space would you like to go? [1-9] "))
    except ValueError:
        print("Invalid input. Lose a turn")
        board.toggle_turn()
    else:
        board.make_move(move)
        board.display()
        if board.check_for_win():
            print(board.turn, "wins!")
            board.game_over = 1
        else:
            board.toggle_turn()
