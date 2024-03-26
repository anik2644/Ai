from collections import namedtuple
from random import choice
from abc import ABC, abstractmethod
from collections import defaultdict
import math
import time

_TTTB = namedtuple("TicTacToeBoard", "tup turn winner terminal")

# Global variable to count the nodes visited
node_counter = 0

class MCTS:
    def __init__(self, exploration_weight=1):
        self.Q = defaultdict(int)
        self.N = defaultdict(int)
        self.children = dict()
        self.exploration_weight = exploration_weight

    def choose(self, node):
        if node.is_terminal():
            raise RuntimeError(f"choose called on terminal node {node}")
        if node not in self.children:
            return node.find_random_child()
        def score(n):
            if self.N[n] == 0:
                return float("-inf")
            return self.Q[n] / self.N[n]
        return max(self.children[node], key=score)

    def do_rollout(self, node):
        global node_counter  # Access the global node_counter variable
        path = self._select(node)
        leaf = path[-1]
        self._expand(leaf)
        reward = self._simulate(leaf)
        self._backpropagate(path, reward)
        # Increment node counter after each rollout
        node_counter += len(path)

    def _select(self, node):
        path = []
        while True:
            path.append(node)
            if node not in self.children or not self.children[node]:
                return path
            unexplored = self.children[node] - self.children.keys()
            if unexplored:
                n = unexplored.pop()
                path.append(n)
                return path
            node = self._uct_select(node)
    def _expand(self, node):
        if node in self.children:
            return
        self.children[node] = node.find_children()

    def _simulate(self, node):
        invert_reward = True
        while True:
            if node.is_terminal():
                reward = node.reward()
                return 1 - reward if invert_reward else reward
            node = node.find_random_child()
            invert_reward = not invert_reward

    def _backpropagate(self, path, reward):
        for node in reversed(path):
            self.N[node] += 1
            self.Q[node] += reward
            reward = 1 - reward

    def _uct_select(self, node):
        assert all(n in self.children for n in self.children[node])
        log_N_vertex = math.log(self.N[node])
        def uct(n):
            return self.Q[n] / self.N[n] + self.exploration_weight * math.sqrt(
                log_N_vertex / self.N[n]
            )
        return max(self.children[node], key=uct)

class Node(ABC):
    @abstractmethod
    def find_children(self):
        return set()

    @abstractmethod
    def find_random_child(self):
        return None

    @abstractmethod
    def is_terminal(self):
        return True

    @abstractmethod
    def reward(self):
        return 0

    @abstractmethod
    def __hash__(self):
        return 123456789

    @abstractmethod
    def __eq__(node1, node2):
        return True

class TicTacToeBoard(_TTTB, Node):
    def find_children(board):
        if board.terminal:
            return set()
        return {
            board.make_move(i) for i, value in enumerate(board.tup) if value is None
        }

    def find_random_child(board):
        if board.terminal:
            return None
        empty_spots = [i for i, value in enumerate(board.tup) if value is None]
        return board.make_move(choice(empty_spots))

    def reward(board):
        if not board.terminal:
            raise RuntimeError(f"reward called on nonterminal board {board}")
        if board.winner is board.turn:
            return 1
        if board.winner is None:
            return 0.5
        return 0

    def is_terminal(board):
        return board.terminal

    def make_move(board, index):
        tup = board.tup[:index] + (board.turn,) + board.tup[index + 1 :]
        turn = not board.turn
        winner = _find_winner(tup)
        is_terminal = (winner is not None) or not any(v is None for v in tup)
        return TicTacToeBoard(tup, turn, winner, is_terminal)

    def to_pretty_string(board):
        to_char = lambda v: ("X" if v is True else ("O" if v is False else " "))
        rows = [
            [to_char(board.tup[3 * row + col]) for col in range(3)] for row in range(3)
        ]
        result = ""
        for i, row in enumerate(rows):
            result += " | ".join(row) + "\n"
            if i < 2:
                result += "-" * 9 + "\n"
        return result

def play_game():
    global node_counter  # Access the global node_counter variable
    tree_x = MCTS()  # MCTS for player X
    tree_o = MCTS()  # MCTS for player O
    board = new_tic_tac_toe_board()
    print(board.to_pretty_string())
    while True:
        # Player X's turn
        print("Player X's turn:")
        for _ in range(50):
            tree_x.do_rollout(board)
        board = tree_x.choose(board)
        print(board.to_pretty_string())
        print(f"Player X moves: {move_to_row_col(board.tup)}")
        if board.terminal:
            if board.winner is not None:
                print("Player X wins!")
            else:
                print("It's a tie!")
            break
        
        # Player O's turn
        print("Player O's turn:")
        for _ in range(50):
            tree_o.do_rollout(board)
        board = tree_o.choose(board)
        print(board.to_pretty_string())
        print(f"Player O moves: {move_to_row_col(board.tup)}")
        if board.terminal:
            if board.winner is not None:
                print("Player O wins!")
            else:
                print("It's a tie!")
            break

    print("Nodes visited:", node_counter)  # Print node count after the game finishes

def move_to_row_col(tup):
    moves = [(i // 3 + 1, i % 3 + 1) for i, value in enumerate(tup) if value is not None]
    return moves[-1]


# Remaining code stays the same...

def _winning_combos():
    for start in range(0, 9, 3):
        yield (start, start + 1, start + 2)
    for start in range(3):
        yield (start, start + 3, start + 6)
    yield (0, 4, 8)
    yield (2, 4, 6)

def _find_winner(tup):
    for i1, i2, i3 in _winning_combos():
        v1, v2, v3 = tup[i1], tup[i2], tup[i3]
        if False is v1 is v2 is v3:
            return False
        if True is v1 is v2 is v3:
            return True
    return None

def new_tic_tac_toe_board():
    return TicTacToeBoard(tup=(None,) * 9, turn=True, winner=None, terminal=False)


start_time = time.time()  # Record the start time


if __name__ == "__main__":
    play_game()


end_time =  time.time()
elapsed_time = end_time - start_time  # Calculate elapsed time
print("MCTS time: {:.7f} seconds".format(elapsed_time))
# Save algorithm name and time data to a file
with open("time.txt", "a") as file:
    file.write("MCTS: {:.7f} seconds \n".format(elapsed_time))

with open("space.txt", "a") as file:
    file.write("MCTS: {} nodes\n".format(node_counter))