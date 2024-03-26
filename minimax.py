import numpy as np
import random
import time

node_counter = 0  # Global variable to count nodes visited

def create_board():
    return np.zeros((3, 3))

def possibilities(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == 0]

def evaluate(board):
    for player in [1, 2]:
        if (row_win(board, player) or
            col_win(board, player) or
            diag_win(board, player)):
            return player
    if np.all(board != 0):
        return -1
    return 0

def row_win(board, player):
    return any(np.all(row == player) for row in board)

def col_win(board, player):
    return any(np.all(col == player) for col in board.T)

def diag_win(board, player):
    return np.all(np.diag(board) == player) or np.all(np.diag(np.fliplr(board)) == player)

def minimax(board, depth, player):
    global node_counter  # Access the global node_counter variable
    node_counter += 1  # Increment node counter
    if player == 2:
        best = [-1, -1, -float('inf')]
    else:
        best = [-1, -1, float('inf')]
    
    if depth == 0 or evaluate(board) != 0:
        score = evaluate(board)
        return [-1, -1, score]
    
    for move in possibilities(board):
        x, y = move
        board[x][y] = player
        score = minimax(board, depth - 1, 3 - player)
        board[x][y] = 0
        score[0], score[1] = x, y
        
        if player == 2:
            if score[2] > best[2]:
                best = score
        else:
            if score[2] < best[2]:
                best = score
    
    return best

def play_game():
    global node_counter  # Access the global node_counter variable
    board, winner, counter = create_board(), 0, 1
    node_counter = 0  # Reset node counter
    print(board)

    while winner == 0:
        for player in [1, 2]:
            x, y, _ = minimax(board, 2, player)
            print(f"Player {player} moves to ({x}, {y})")
            board[x][y] = player
            print(board)
            winner = evaluate(board)
            if winner != 0:
                break
    return winner

if __name__ == "__main__":
    start_time = time.time()  # Record the start time
    print("Winner is:", play_game())
    print("Nodes visited:", node_counter)
    end_time =  time.time()
    elapsed_time = end_time - start_time  # Calculate elapsed time
    print("MINIMAX time: {:.7f} seconds".format(elapsed_time))
    # Save algorithm name and time data to a file
    with open("time.txt", "a") as file:
        file.write("MINIMAX: {:.7f} seconds \n".format(elapsed_time))

    with open("space.txt", "a") as file:
        file.write("MINIMAX: {} nodes\n".format(node_counter))