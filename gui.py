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
        self.root.geometry("300x380")
        self.root.configure(bg="#33363B")

        self.label = tk.Label(
            root, 
            text="Choose your move!", 
            bg="#33363B", 
            fg="#FFFFFF", 
            font=("Segoe UI", 14, "bold")
        )
        self.label.pack(pady=(20, 15))

        for move in ['rock', 'paper', 'scissors']:
            btn = tk.Button(
                root, 
                text=move.capitalize(), 
                width=15, 
                bg="#5A6068", 
                fg="#FFFFFF", 
                activebackground="#78808A", 
                activeforeground="#FFFFFF", 
                relief="raised", 
                bd=6,
                font=("Segoe UI", 12, "bold"), 
                command=lambda m=move: self.play(m)
            )
            btn.pack(pady=6)

        self.score_label = tk.Label(
            root, 
            text="Score - Player: 0 | AI: 0 | Ties: 0", 
            bg="#1A1C1E", 
            fg="#00FF41", 
            relief="sunken",
            bd=4,
            width=26,
            font=("Courier New", 11, "bold")
        )
        self.score_label.pack(pady=(25, 10))

        self.refresh_btn = tk.Button(
            root, 
            text="Refresh Score", 
            width=15, 
            bg="#A83232", 
            fg="#FFFFFF", 
            activebackground="#D14747", 
            activeforeground="#FFFFFF", 
            relief="raised", 
            bd=5,
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
        popup.configure(bg="#40444B")
        popup.resizable(False, False)
        
        popup_width = 220
        popup_height = 160
        x = self.root.winfo_x() + (self.root.winfo_width() - popup_width) // 2
        y = self.root.winfo_y() + (self.root.winfo_height() - popup_height) // 2
        popup.geometry(f"{popup_width}x{popup_height}+{math.floor(x)}+{math.floor(y)}")
        
        popup.grab_set() 
        popup.transient(self.root)

        frame = tk.Frame(popup, bg="#40444B", relief="ridge", bd=4)
        frame.pack(expand=True, fill="both", padx=5, pady=5)

        title_label = tk.Label(
            frame, 
            text="Round Complete", 
            bg="#40444B", 
            fg="#FFFFFF", 
            font=("Segoe UI", 12, "bold")
        )
        title_label.pack(pady=(10, 5))
        
        info_text = f"AI chose: {ai_move}\nResult: {winner}"
        info_label = tk.Label(
            frame, 
            text=info_text, 
            bg="#1A1C1E", 
            fg="#00FF41", 
            relief="sunken",
            bd=3,
            width=18,
            font=("Courier New", 10, "bold"),
            justify="center"
        )
        info_label.pack(pady=5)

        ok_btn = tk.Button(
            frame, 
            text="OK", 
            width=10,
            bg="#4A8FCA", 
            fg="#FFFFFF", 
            activebackground="#63A5DD", 
            activeforeground="#FFFFFF", 
            relief="raised", 
            bd=4,
            font=("Segoe UI", 10, "bold"), 
            command=popup.destroy
        )
        ok_btn.pack(pady=(10, 10))

if __name__ == "__main__":
    root = tk.Tk()
    game = RPSGame(root)
    root.mainloop()