import tkinter as tk
from tkinter import messagebox
from ai import SimpleAI
from score import ScoreBoard

class RPSGame:
    def __init__(self, root):
        self.ai = SimpleAI()
        self.scoreboard = ScoreBoard()
        self.root = root
        self.root.title("RPS AI Game")
        self.root.geometry("250x280")

        self.label = tk.Label(root, text="Choose your move!")
        self.label.pack(pady=(10, 5))

        for move in ['rock', 'paper', 'scissors']:
            btn = tk.Button(root, text=move.capitalize(), width=10, command=lambda m=move: self.play(m))
            btn.pack(pady=2)

        self.score_label = tk.Label(root, text="Score - Player: 0 | AI: 0 | Ties: 0")
        self.score_label.pack(pady=(15, 5))

        self.refresh_btn = tk.Button(root, text="Refresh Score", command=self.reset_scores)
        self.refresh_btn.pack(pady=5)

    def play(self, player_move):
        ai_move = self.ai.get_move()
        winner = self.determine_winner(player_move, ai_move)
        self.scoreboard.record_win(winner)
        self.ai.update_history(player_move)
        
        self.score_label.config(text=f"Score - Player: {self.scoreboard.player_wins} | AI: {self.scoreboard.ai_wins} | Ties: {self.scoreboard.ties}")
        messagebox.showinfo("Result", f"AI chose: {ai_move}\nResult: {winner}")

    def determine_winner(self, p, a):
        if p == a: return "tie"
        if (p=='rock' and a=='scissors') or (p=='paper' and a=='rock') or (p=='scissors' and a=='paper'): return "player"
        return "ai"

    def reset_scores(self):
        self.scoreboard.player_wins = 0
        self.scoreboard.ai_wins = 0
        self.scoreboard.ties = 0
        self.score_label.config(text="Score - Player: 0 | AI: 0 | Ties: 0")

if __name__ == "__main__":
    root = tk.Tk()
    game = RPSGame(root)
    root.mainloop()