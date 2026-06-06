import random

class SimpleAI:
    def __init__(self):
        self.transitions = {
            'rock': {'rock': 0, 'paper': 0, 'scissors': 0},
            'paper': {'rock': 0, 'paper': 0, 'scissors': 0},
            'scissors': {'rock': 0, 'paper': 0, 'scissors': 0}
        }
        self.last_move = None

    def get_move(self):
        if self.last_move is None:
            return random.choice(['rock', 'paper', 'scissors'])

        counts = self.transitions[self.last_move]
        predicted_next = max(counts, key=counts.get)
        
        if counts[predicted_next] == 0:
            return random.choice(['rock', 'paper', 'scissors'])

        if predicted_next == 'rock':
            return 'paper'
        elif predicted_next == 'paper':
            return 'scissors'
        else:
            return 'rock'

    def update_history(self, player_move):
        if self.last_move:
            self.transitions[self.last_move][player_move] += 1
        self.last_move = player_move