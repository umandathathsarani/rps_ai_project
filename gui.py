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
        self.root.geometry("300x350")
        self.root.configure(bg="#2C3E50")

        self.label = tk.Label(root, text="Choose your move!", bg="#2C3E50", fg="#ECF0F1", font=("Segoe UI", 14, "bold"))
        self.label.pack(pady=(20, 15))

        for move in ['rock', 'paper', 'scissors']:
            btn = tk.Button(
                root, 
                text=move.capitalize(), 
                width=15, 
                bg="#34495E", 
                fg="#ECF0F1", 
                activebackground="#2980B9", 
                activeforeground="#ECF0F1", 
                relief="flat", 
                font=("Segoe UI", 12), 
                command=lambda m=move: self.play(m)
            )
            btn.pack(pady=6)

        self.score_label = tk.Label(
            root, 
            text="Score - Player: 0 | AI: 0 | Ties: 0", 
            bg="#2C3E50", 
            fg="#F1C40F", 
            font=("Segoe UI", 12, "bold")
        )
        self.score_label.pack(pady=(25, 10))

        self.refresh_btn = tk.Button(
            root, 
            text="Refresh Score", 
            width=15, 
            bg="#E74C3C", 
            fg="#ECF0F1", 
            activebackground="#C0392B", 
            activeforeground="#ECF0F1", 
            relief="flat", 
            font=("Segoe UI", 10, "bold"), 
            command=self.reset_scores
        )
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