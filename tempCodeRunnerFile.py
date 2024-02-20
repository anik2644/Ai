import osmnx as ox
import random
import networkx as nx
import heapq
import time
from tabulate import tabulate

list1 = []
list2 = []
list3 = []

def hstd(node1, node2):
    hstd_value = ox.distance.euclidean_dist_vec(graph.nodes[node1]['y'], graph.nodes[node1]['x'],
                                                 graph.nodes[node2]['y'], graph.nodes[node2]['x'])
    risk_value = random.uniform(0, 500)
    return hstd_value + risk_value

def dijkstra(graph, start_node):
    dist = {node: float('inf') for node in graph.nodes}
    dist[start_node] = 0
    predecessors = {}
    pq = [(0, start_node)]
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        if current_dist > dist[current_node]:
            continue
        for neighbor, edge in graph[current_node].items():
            weight = edge.get('weight', 1)
            new_dist = dist[current_node] + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                predecessors[neighbor] = current_node
                heapq.heappush(pq, (new_dist, neighbor))
    return dist, predecessors

def evaluation_function(node, target_node, actual_cost, heuristic, weight):
    return actual_cost[node] + weight * heuristic(node, target_node)

def greedy_best_first_search(graph, start_node, target_node, heuristic):
    visited = set()
    pq = [(heuristic(start_node, target_node), start_node)]
    while pq:
        _, current_node = heapq.heappop(pq)
        list1.append(current_node)
        if current_node == target_node:
            return visited
        visited.add(current_node)
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                heapq.heappush(pq, (heuristic(neighbor, target_node), neighbor))
    return visited

def a_star(graph, start_node, target_node, actual_cost, heuristic):
    visited = set()
    pq = [(evaluation_function(start_node, target_node, actual_cost, heuristic, 1), start_node)]
    while pq:
        _, current_node = heapq.heappop(pq)
        list2.append(current_node) 
        if current_node == target_node:
            return visited
        visited.add(current_node)
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                heapq.heappush(pq, (evaluation_function(neighbor, target_node, actual_cost, heuristic, 1), neighbor))
    return visited

def weighted_a_star(graph, start_node, target_node, actual_cost, heuristic, weight):
    visited = set()
    pq = [(evaluation_function(start_node, target_node, actual_cost, heuristic, weight), start_node)]
    while pq:
        _, current_node = heapq.heappop(pq)
        list3.append(current_node) 
        if current_node == target_node:
            return visited
        visited.add(current_node)
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                heapq.heappush(pq, (evaluation_function(neighbor, target_node, actual_cost, heuristic, weight), neighbor))
    return visited

city_name = "Lake Placid, New York"
graph = ox.graph_from_place(city_name, network_type='all')

if graph is not None:
    nodes = graph.nodes
    edges = graph.edges
    all_nodes = list(graph.nodes)
    
    start_node = 8922966682
    target_node = 8922966471

    start_time = time.time()
    actual_cost, _ = dijkstra(graph, start_node)
    dijkstra_time = time.time() - start_time

    start_time = time.time()
    gbfs_visited = greedy_best_first_search(graph, start_node, target_node, hstd)
    gbfs_time = time.time() - start_time

    start_time = time.time()
    a_star_visited = a_star(graph, start_node, target_node, actual_cost, hstd)
    a_star_time = time.time() - start_time

    start_time = time.time()
    weight = 4
    weighted_a_star_visited = weighted_a_star(graph, start_node, target_node, actual_cost, hstd, weight)
    weighted_a_star_time = time.time() - start_time

    print("Start Node:", start_node)
    print("Target Node:", target_node)

    gbfs_time_ms = gbfs_time * 1000
    a_star_time_ms = a_star_time * 1000
    weighted_a_star_time_ms = weighted_a_star_time * 1000

    results = [
        ("Greedy Best First Search", len(gbfs_visited)*8, gbfs_time_ms, len(gbfs_visited)),
        ("A*", len(a_star_visited)*8, a_star_time_ms, len(a_star_visited)),
        ("Weighted A*", len(weighted_a_star_visited)*8, weighted_a_star_time_ms, len(weighted_a_star_visited))
    ]

    print("Size of List 1:", len(list1))
    print("Size of List 2:", len(list2))
    print("Size of List 3:", len(list3))

    print(tabulate(results, headers=["Algorithm", "Memory (Bytes)", "Time (ms)", "Search Space"], tablefmt="grid"))

    if graph is not None and list2:
        try:
            ox.plot_graph_route(graph, list2, route_color='red', bgcolor='yellow', node_size=20, node_color='black')
        except Exception as e:
            print("An error occurred while plotting the route:", e)
    else:
        print("Error: Either the graph is None or list1 is empty.")

    ox.plot_graph(ox.project_graph(graph), bgcolor='yellow', node_size=20, node_color='black')
else:
    print("Error: Failed to retrieve the graph data.")
