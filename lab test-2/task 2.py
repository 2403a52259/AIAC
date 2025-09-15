import heapq

def dijkstra(graph, source):
    """
    Compute shortest path distances from a source node to all nodes in a weighted graph.
    
    Algorithm:
    - Initialize distances with infinity, except source=0.
    - Use a priority queue to pick the node with the smallest distance.
    - For each neighbor, perform edge relaxation:
        if dist[u] + weight(u,v) < dist[v], update dist[v].
    - Repeat until all nodes are processed.
    
    Args:
        graph (dict): adjacency dict {node: {neighbor: weight, ...}, ...}
        source (str): starting node
    
    Returns:
        dict: shortest distances from source to each node
    """
    # Initialize distances
    dist = {node: float('inf') for node in graph}
    dist[source] = 0
    
    # Min-heap priority queue (distance, node)
    pq = [(0, source)]
    
    while pq:
        current_dist, u = heapq.heappop(pq)
        
        # Skip if we already found a better path
        if current_dist > dist[u]:
            continue
        
        # Relaxation step
        for v, weight in graph[u].items():
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
    
    return dist

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 1},
    'D': {}
}

print(dijkstra(graph, 'A'))