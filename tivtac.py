import random
import time

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 7)

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True

    # Check columns
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True

    return False

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def get_available_moves(board):
    available_moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                available_moves.append((i, j))
    return available_moves

def player_move(board, player):
    available_moves = get_available_moves(board)
    if available_moves:
        move = random.choice(available_moves)
        row, col = move
        board[row][col] = player
        print(f"Player {player} moves to row {row + 1}, column {col + 1}")
    else:
        print("No available moves left!")

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Tic Tac Toe Game\n")
    print_board(board)

    player = 'X'
    while not (check_winner(board) or is_board_full(board)):
        time.sleep(1)
        player_move(board, player)
        print_board(board)
        if check_winner(board):
            print(f"Player {player} wins!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break
        player = 'O' if player == 'X' else 'X'

if __name__ == "__main__":
    play_game()
