def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def player_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid move. Please choose a number between 1 and 9.")
                continue
            
            row, col = divmod(move - 1, 3)  # Convert 1-9 into row and column
            if board[row][col] != " ":
                print("This spot is already taken. Choose another spot.")
            else:
                board[row][col] = player
                break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def check_win(board, player):
    for i in range(3):
        # Check rows and columns
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False

def check_tie(board):
    for row in board:
        if " " in row:
            return False
    return True

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        player_move(board, current_player)

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break
        
        current_player = "O" if current_player == "X" else "X"  # Alternate players

if __name__ == "__main__":
    play_game()


