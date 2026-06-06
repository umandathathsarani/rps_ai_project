import random

class SimpleAI:
    def __init__(self):
        self.player_history = {'rock': 0, 'paper': 0, 'scissors': 0}

    def get_move(self):
        total_moves = sum(self.player_history.values())
        
        if total_moves == 0:
            return random.choice(['rock', 'paper', 'scissors'])

        most_frequent_move = max(self.player_history, key=self.player_history.get)

        if most_frequent_move == 'rock':
            return 'paper'
        elif most_frequent_move == 'paper':
            return 'scissors'
        else:
            return 'rock'

    def update_history(self, player_move):
        if player_move in self.player_history:
            self.player_history[player_move] += 1