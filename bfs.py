import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def bfs(graph, start_node, visited, branch_factor):
    queue = deque([(start_node, 0)])  # Use a queue for BFS, with tuple (node, depth)

    while queue:
        current_node, depth = queue.popleft()

        if current_node not in visited:
            print(f"Visiting node: {current_node} at depth {depth}")
            visited.add(current_node)

            if depth < branch_factor:
                queue.extend((neighbor, depth + 1) for neighbor in graph[current_node])

# Example usage:
larger_graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['I', 'J'],
    'F': ['K'],
    'G': [],
    'H': [],
    'I': [],
    'J': [],
    'K': []
} 

G = nx.DiGraph(larger_graph)



start_node = 'A'
visited_nodes = set()
branch_factor = 8  # Specify the branch factor

print(f"BFS starting from node {start_node}, with branch factor {branch_factor}:")
bfs(larger_graph, start_node, visited_nodes, branch_factor)


# Draw the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_color="black", font_weight="bold", edge_color="gray", linewidths=0.5, arrowsize=10)

# Show the graph
plt.show()