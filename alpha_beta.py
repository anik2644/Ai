import numpy as np
import random
from time import sleep, time

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

def minimax(board, depth, player, alpha, beta):
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
        score = minimax(board, depth - 1, 3 - player, alpha, beta)
        board[x][y] = 0
        score[0], score[1] = x, y
        
        if player == 2:
            if score[2] > best[2]:
                best = score
            beta = max(beta, best[2])
            if beta <= alpha:
                break
        else:
            if score[2] < best[2]:
                best = score
            alpha = min(alpha, best[2])
            if beta <= alpha:
                break
    
    return best

def play_game():
    board, winner, counter = create_board(), 0, 1
    print(board)
  #  sleep(2)

 

    while winner == 0:
        for player in [1, 2]:
            x, y, _ = minimax(board, 2, player, -float('inf'), float('inf'))
            print(f"Player {player} moves to ({x}, {y})")
            board[x][y] = player
            print("Board after " + str(counter) + " move")
            print(board)
           # sleep(2)
            counter += 1
            winner = evaluate(board)
            if winner != 0:
                break

    return winner




start_time = time()  # Record start time

print("Winner is: " + str(play_game()))
end_time = time()  # Record end time
elapsed_time = end_time - start_time  # Calculate elapsed time
print("ALPHA_BETA time: {:.7f} seconds".format(elapsed_time))
with open("time.txt", "a") as file:
    file.write("ALPHA_BETA: {:.7f} seconds \n".format(elapsed_time))