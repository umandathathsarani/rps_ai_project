class ScoreBoard:
    def __init__(self):
        self.player_wins = 0
        self.ai_wins = 0
        self.ties = 0

    def record_win(self, winner):
        if winner == "player":
            self.player_wins += 1
        elif winner == "ai":
            self.ai_wins += 1
        elif winner == "tie":
            self.ties += 1

    def display_score(self):
        print(f"Score - Player: {self.player_wins} | AI: {self.ai_wins} | Ties: {self.ties}")