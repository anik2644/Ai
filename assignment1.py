import osmnx as ox
import random
import networkx as nx
import heapq
import random
import time
import matplotlib.pyplot as plt
from tabulate import tabulate

list1 = []
list2 = []
list3 = []
# Define the heuristic function (straight-line distance + random value as risk function)
def hstd(node1, node2):
    # Calculate the Euclidean distance between node1 and node2
    hstd_value = ox.distance.euclidean_dist_vec(graph.nodes[node1]['y'], graph.nodes[node1]['x'],
                                                 graph.nodes[node2]['y'], graph.nodes[node2]['x'])
    # Get the random value associated with the edge (node1, node2)
    risk_value = random.uniform(0, 500)  # Generate a random value between 0 and 500
    
    # Return the heuristic value as the sum of hstd and random_value
    return hstd_value + risk_value

# Implement Dijkstra's algorithm to calculate actual cost
def dijkstra(graph, start_node):
    # Initialize dictionaries to store distances and predecessors
    dist = {node: float('inf') for node in graph.nodes}
    dist[start_node] = 0
    predecessors = {}
    # Priority queue to store nodes to visit
    pq = [(0, start_node)]
    # Main loop
    while pq:
        # Pop the node with the smallest distance from the priority queue
        current_dist, current_node = heapq.heappop(pq)
        # Check if this is a shorter path to current_node
        if current_dist > dist[current_node]:
            continue
        # Iterate over neighbors of current_node
        for neighbor, edge in graph[current_node].items():
            weight = edge.get('weight', 1)  # Default weight is 1 if not specified
            # Calculate the new distance
            new_dist = dist[current_node] + weight
            # Update distance and predecessor if shorter path is found
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                predecessors[neighbor] = current_node
                # Add neighbor to priority queue
                heapq.heappush(pq, (new_dist, neighbor))
    return dist, predecessors

# Define the evaluation function (actual cost + heuristic)
def evaluation_function(node, target_node, actual_cost, heuristic,weight):
    return actual_cost[node] + weight * heuristic(node, target_node)

# Implement Greedy Best First Search algorithm
def greedy_best_first_search(graph, start_node, target_node, heuristic):
    visited = set()
    pq = [(heuristic(start_node, target_node), start_node)]
    while pq:
  #      list1.append(current_node)

        _, current_node = heapq.heappop(pq)
        list1.append(current_node)  # Append the visited node to lis
        if current_node == target_node:
            return visited
        visited.add(current_node)
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                heapq.heappush(pq, (heuristic(neighbor, target_node), neighbor))
    return visited

# Implement A* algorithm
def a_star(graph, start_node, target_node, actual_cost, heuristic):
    visited = set()
    pq = [(evaluation_function(start_node, target_node, actual_cost, heuristic,1), start_node)]
    while pq:
  #      list2.append(current_node)
        _, current_node = heapq.heappop(pq)
        list2.append(current_node) 
        if current_node == target_node:
            return visited
        visited.add(current_node)
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                heapq.heappush(pq, (evaluation_function(neighbor, target_node, actual_cost, heuristic,1), neighbor))
    return visited

# Implement Weighted A* algorithm
def weighted_a_star(graph, start_node, target_node, actual_cost, heuristic, weight):
    visited = set()
    pq = [(evaluation_function(start_node, target_node, actual_cost, heuristic,weight), start_node)]
    while pq:
    #    list3.append(current_node)
        _, current_node = heapq.heappop(pq)
        list3.append(current_node) 
        if current_node == target_node:
            return visited
        visited.add(current_node)
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                heapq.heappush(pq, (evaluation_function(neighbor, target_node, actual_cost, heuristic,weight), neighbor))
    return visited


# Download OSM data for Lake Placid, NY
city_name = "Lake Placid, New York"
graph = ox.graph_from_place(city_name, network_type='all')
# Visualize the city map with a custom background color



# Access nodes and edges
nodes = graph.nodes
edges = graph.edges

# Open a file in write mode
with open("node.txt", "w") as file:
    # Iterate over nodes and write them to the file
    for node, data in nodes(data=True):
        file.write(f"{node}: {data}\n")



# Get list of all nodes in the graph
all_nodes = list(graph.nodes)



# Choose random start and target nodes
#start_node = random.choice(all_nodes)
#target_node = random.choice(all_nodes)

start_node= 8922966682
target_node= 8922966471
#start_location = ox.geocode_to_gdf("Lake Placid, New York")  # Provide a meaningful location query
#start_city = start_location['place_name'].iloc[0]


# Define fixed start and target nodes
'''start_node = YOUR_START_NODE_ID
target_node = YOUR_TARGET_NODE_ID
'''
# Get the name of the city for the start node
# start_city = ox.geocode_to_gdf(graph.nodes[start_node])['place_name'].iloc[0]

# Get the name of the city for the target node
# target_city = ox.geocode_to_gdf(graph.nodes[target_node])['place_name'].iloc[0]

# Print the names of the cities
print("City for Start Node:", start_node)
print("City for Target Node:", target_node)



# Run Dijkstra's algorithm
start_time = time.time()
actual_cost, _ = dijkstra(graph, start_node)
dijkstra_time = time.time() - start_time

# Run Greedy Best First Search
start_time = time.time()
gbfs_visited = greedy_best_first_search(graph, start_node, target_node, hstd)
gbfs_time = time.time() - start_time

# Run A*
start_time = time.time()
a_star_visited = a_star(graph, start_node, target_node, actual_cost, hstd)
a_star_time = time.time() - start_time

# Run Weighted A* (with weight = 4)
start_time = time.time()
weight = 4
weighted_a_star_visited = weighted_a_star(graph, start_node, target_node, actual_cost, hstd, weight)
weighted_a_star_time = time.time() - start_time

# Print chosen start and target nodes
print("Start Node:", start_node)
print("Target Node:", target_node)

# Convert time to milliseconds
gbfs_time_ms = gbfs_time * 1000
a_star_time_ms = a_star_time * 1000
weighted_a_star_time_ms = weighted_a_star_time * 1000

# Store the results in a list of tuples
results = [
    ("Greedy Best First Search", len(gbfs_visited)*8, gbfs_time_ms, len(gbfs_visited)),
    ("A*", len(a_star_visited)*8, a_star_time_ms, len(a_star_visited)),
    ("Weighted A*", len(weighted_a_star_visited)*8, weighted_a_star_time_ms, len(weighted_a_star_visited))
]


'''
print("List 1:", list1)
print("List 2:", list2)
print("List 3:", list3)
'''

print("Size of List 1:", len(list1))
print("Size of List 2:", len(list2))
print("Size of List 3:", len(list3))

# Print the results in a tabular format
print(tabulate(results, headers=["Algorithm", "Memory (Bytes)", "Time (ms)", "Search Space"], tablefmt="grid"))

# Visualize the city map with a custom title

ox.plot_graph(ox.project_graph(graph), bgcolor='yellow', node_size=20,node_color='black',)
