import numpy as np
import random
from time import sleep

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.visits = 0
        self.value = 0

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

def random_place(board, player):
    selection = possibilities(board)
    if selection:
        return random.choice(selection)
    else:
        return None

def rollout(board, player):
    while evaluate(board) == 0:
        move = random_place(board, player)
        if move:
            board[move] = player
            player = 3 - player
    return evaluate(board)

def select_best_child(node):
    return max(node.children, key=lambda c: c.value / c.visits + (2 * np.sqrt(np.log(node.visits) / c.visits)) if c.visits > 0 else float('inf'))

def expand_node(node):
    move = random_place(node.state, 2)  # Assuming computer always plays as player 2
    if move:
        new_state = np.copy(node.state)
        new_state[move] = 2
        child_node = Node(new_state, parent=node)
        node.children.append(child_node)
        return child_node
    else:
        return None

def simulate(node):
    if not node.children:
        return rollout(node.state, 2)
    else:
        child_node = select_best_child(node)
        value = simulate(child_node)
        return value

def backpropagate(node, value):
    node.visits += 1
    node.value += value
    if node.parent:
        backpropagate(node.parent, value)

def mcts(board, iterations):
    root = Node(board)
    for _ in range(iterations):
        leaf = root
        while leaf.children:
            leaf = select_best_child(leaf)
        if evaluate(leaf.state) == 0:
            child_node = expand_node(leaf)
            if child_node:
                value = simulate(child_node)
                backpropagate(child_node, value)
    return select_best_child(root).state

def play_game():
    board, winner, counter = create_board(), 0, 1
    print(board)
    sleep(2)

    while winner == 0:
        if counter % 2 == 0:
            board = mcts(board, 1000)  # Adjust iterations as needed for complexity
            print("Computer's move:")
        else:
            move = random_place(board, 1)
            print(f"Player 1 moves to {move}")
            board[move] = 1
        print("Board after " + str(counter) + " move")
        print(board)
        sleep(2)
        counter += 1
        winner = evaluate(board)
        if winner != 0:
            break
    return winner

print("Winner is: " + str(play_game()))