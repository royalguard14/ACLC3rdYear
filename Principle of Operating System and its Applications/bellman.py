def bellman_ford(graph, start):
    # Distance dictionary to store the shortest path to each node
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    # Step 2: Relax edges repeatedly
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    # Step 3: Check for negative weight cycles
    for node in graph:
        for neighbor, weight in graph[node].items():
            if distances[node] + weight < distances[neighbor]:
                print("Graph contains a negative weight cycle")
                return None

    return distances

# Example usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': -3, 'D': 2},
    'C': {'D': 3},
    'D': {'A': -1}
}

start_node = 'A'
distances = bellman_ford(graph, start_node)
print(distances)
