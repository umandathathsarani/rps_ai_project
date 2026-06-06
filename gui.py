import tkinter as tk
from tkinter import messagebox
from ai import SimpleAI
from score import ScoreBoard
import math

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
        
        self.show_custom_result_popup(ai_move, winner)

    def determine_winner(self, p, a):
        if p == a: return "tie"
        if (p=='rock' and a=='scissors') or (p=='paper' and a=='rock') or (p=='scissors' and a=='paper'): return "player"
        return "ai"

    def reset_scores(self):
        self.scoreboard.player_wins = 0
        self.scoreboard.ai_wins = 0
        self.scoreboard.ties = 0
        self.score_label.config(text="Score - Player: 0 | AI: 0 | Ties: 0")

    def show_custom_result_popup(self, ai_move, winner):
        popup = tk.Toplevel(self.root)
        popup.title("Game Outcome")
        popup.configure(bg="#2C3E50")
        popup.resizable(False, False)
        
        popup_width = 200
        popup_height = 150
        x = self.root.winfo_x() + (self.root.winfo_width() - popup_width) // 2
        y = self.root.winfo_y() + (self.root.winfo_height() - popup_height) // 2
        popup.geometry(f"{popup_width}x{popup_height}+{math.floor(x)}+{math.floor(y)}")

        popup.grab_set() 
        popup.transient(self.root) 

        title_label = tk.Label(
            popup, 
            text="Round Complete", 
            bg="#2C3E50", 
            fg="#ECF0F1", 
            font=("Segoe UI", 12, "bold")
        )
        title_label.pack(pady=(15, 5))
        
        info_text = f"AI chose: {ai_move}\nResult: {winner}"
        info_label = tk.Label(
            popup, 
            text=info_text, 
            bg="#2C3E50", 
            fg="#ECF0F1", 
            font=("Segoe UI", 10),
            justify="center" 
        )
        info_label.pack(pady=5)

        ok_btn = tk.Button(
            popup, 
            text="OK", 
            width=10,
            bg="#34495E", 
            fg="#ECF0F1", 
            activebackground="#2980B9", 
            activeforeground="#ECF0F1", 
            relief="flat", 
            font=("Segoe UI", 10), 
            command=popup.destroy 
        )
        ok_btn.pack(pady=(10, 15))

if __name__ == "__main__":
    root = tk.Tk()
    game = RPSGame(root)
    root.mainloop()