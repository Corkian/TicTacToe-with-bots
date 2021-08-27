import math
import random


class Player():
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self, game):
        pass


class Human(Player):
    def __init__(self, symbol):
        super().__init__(symbol)

    def get_move(self, game):
        empty_square = False
        value = None
        while not empty_square:
            square = input(self.symbol + ' turn. Specify move (0-9): ')
            try:
                value = int(square)
                if value not in game.available_moves():
                    raise ValueError
                empty_square = True
            except ValueError:
                print('Square is not empty. Choose another.')
        return value


class RandomComputer(Player):
    def __init__(self, symbol):
        super().__init__(symbol)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class SmartComputer(Player):
    def __init__(self, symbol):
        super().__init__(symbol)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.symbol)['position']
        return square

    def minimax(self, state, player):
        max_player = self.symbol
        other_player = 'O' if player == 'X' else 'X'

        if state.current_winner == other_player:
            return {'position': None,
                    'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                            state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}
        for possible_move in state.available_moves():
            state.take_turn(possible_move, player)
            sim_score = self.minimax(state, other_player)

            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best
