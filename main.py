from ai import SimpleAI

def determine_winner(player_move, ai_move):
    if player_move == ai_move:
        return "tie"
    elif (player_move == 'rock' and ai_move == 'scissors') or \
         (player_move == 'paper' and ai_move == 'rock') or \
         (player_move == 'scissors' and ai_move == 'paper'):
        return "player"
    else:
        return "ai"

def play_game():
    ai = SimpleAI()
    valid_moves = ['rock', 'paper', 'scissors']

    print("Welcome to Rock-Paper-Scissors AI!")

    while True:
        player_move = input("Enter rock, paper, or scissors (or 'quit'): ").lower()

        if player_move == 'quit':
            print("Thanks for playing!")
            break

        if player_move not in valid_moves:
            print("Invalid move. Try again.")
            continue

        ai_move = ai.get_move()
        print(f"AI chose: {ai_move}")

        winner = determine_winner(player_move, ai_move)

        if winner == "tie":
            print("It's a tie!")
        elif winner == "player":
            print("You win!")
        else:
            print("AI wins!")

        ai.update_history(player_move)
        print("-" * 20)

if __name__ == "__main__":
    play_game()