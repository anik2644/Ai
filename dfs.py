import networkx as nx
import matplotlib.pyplot as plt

def dfs(graph, start_node, visited, depth_limit):
    if start_node not in visited:
        print(f"Visiting node: {start_node}")
        visited.add(start_node)

        if depth_limit > 0:
            for neighbor in graph[start_node]:
                dfs(graph, neighbor, visited, depth_limit - 1)

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

# Draw the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_color="black", font_weight="bold", edge_color="gray", linewidths=0.5, arrowsize=10)

# Show the graph
plt.show()

start_node = 'A'
visited_nodes = set()
max_depth = 2

print(f"DFS starting from node {start_node}, up to depth {max_depth}:")
dfs(larger_graph, start_node, visited_nodes, max_depth)
