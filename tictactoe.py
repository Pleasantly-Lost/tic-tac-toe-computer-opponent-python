

def display_board(board):
    print("/n")
    for row in [board[i:i+3] for i in range(0,9,3)]:
        print(" | ".join(row))

    print("/n")

def win_check(board):
    # Bingos

    win_cond = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]

    for combo in win_cond:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != "[   ]":
            return board[combo[0]] # Return X or O

    if "[   ]" not in board:
        return "Draw"

    return None

def player_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, choose position (1-9): ")) - 1
            if board[move] == "[   ]":
                board[move] = player
                break
            else:
                print("Spot already taken, try again.")
        except (ValueError, IndexError):
            print("Invalid input. Choose between 1 and 9")

def play_game():
    board = ["[   ]" for _ in range(9)]
    current_player = "[ X ]"
    winner = None

    while winner is None:
        display_board(board)
        player_move(board, current_player)
        winner = win_check(board)

        # Switch players
        current_player = "[ O ]" if current_player == "[ X ]" else "[ X ]"

    display_board(board)
    if winner == "Draw":
        print("Game is a draw")
    else:
        print(f"The winner is: {winner}!")

# Running the game

if __name__ == "__main__":
    play_game()