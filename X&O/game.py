import math
import time
from player import Human, RandomComputer, SmartComputer


class TicTacToe():
    def __init__(self):
        self.board = self.create_board()
        self.current_winner = None

    @staticmethod
    def create_board():
        return [' ' for _ in range(9)]

    def print_board(self):
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def board_nums():
        num_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in num_board:
            print('| ' + ' | '.join(row) + ' |')

    def take_turn(self, square, symbol):
        if self.board[square] == ' ':
            self.board[square] = symbol
            if self.winner(square, symbol):
                self.current_winner = symbol
            return True
        return False

    def winner(self, square, symbol):
        row_ind = math.floor(square / 3)
        row = self.board[row_ind * 3:(row_ind + 1) * 3]
        if all([s == symbol for s in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([s == symbol for s in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == symbol for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == symbol for s in diagonal2]):
                return True
        return False

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.board_nums()

    symbol = 'X'
    while game.empty_squares():
        if symbol == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.take_turn(square, symbol):
            if print_game:
                print(symbol + ' takes square {}'.format(square))
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(symbol + ' wins!')
                return symbol
            symbol = 'O' if symbol == 'X' else 'X'

        time.sleep(.6)

    if print_game:
        print('It\'s a tie!')


def choose_mode_players():
    num_games = None
    print_check = None
    x_player = input(
"""
Choose X player (1-3):
1. Human
2. Smart Computer
3. Random Computer
Choice: """)
    o_player = input(
"""
Choose O player (1-3):
1. Human
2. Smart Computer
3. Random Computer
Choice: """)
    mode = input(
"""
Choose game mode: (1 or 2):
1. Normal
2. Auto
Choice: """)
    if mode == '2':
        num_games = int(input("Specify number of games: "))
        print_check = int(input("Print game (Yes = 1 or No = 0): "))
    if x_player == '1':
        x_player = Human('X')
    elif x_player == '2':
        x_player = SmartComputer('X')
    else:
        x_player = RandomComputer('X')

    if o_player == '1':
        o_player = Human('O')
    elif o_player == '2':
        o_player = SmartComputer('O')
    else:
        o_player = RandomComputer('O')
    return x_player, o_player, mode, num_games, print_check


def auto_play(rounds, x_player, o_player, print_check):
    xWins = 0
    oWins = 0
    ties = 0

    for _ in range(rounds):
        t = TicTacToe()
        result = play(t, x_player, o_player, print_game=print_check)
        if result == 'X':
            xWins += 1
        elif result == 'O':
            oWins += 1
        else:
            ties += 1

    print(f'X wins = {xWins}----ties={ties}----O Wins = {oWins}')


if __name__ == '__main__':
    xPlayer, oPlayer, mode, num_games, print_check = choose_mode_players()
    game = TicTacToe()
    if mode == "1":
        play(game, xPlayer, oPlayer)
    else:
        auto_play(num_games, xPlayer, oPlayer, print_check=print_check)
