def dijkstra(graph, start):
    # Distance dictionary to store the shortest path to each node
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    # List to act as the priority queue
    queue = [(0, start)]
    
    while queue:
        # Find the node with the smallest distance
        queue.sort()
        current_distance, current_node = queue.pop(0)
        
        # Iterate over neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # If a shorter path to the neighbor is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                queue.append((distance, neighbor))
    
    return distances

# Example usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
distances = dijkstra(graph, start_node)
print(distances)
