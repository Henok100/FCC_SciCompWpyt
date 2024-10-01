# Shortest Path Finder using Dijkstra's Algorithm

# A graph representation where each node has connected nodes and their respective distances.
my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],  # Node 'A' is connected to 'B', 'C', and 'E' with distances 5, 3, and 11, respectively.
    'B': [('A', 5), ('C', 1), ('F', 2)],   # Node 'B' is connected to 'A', 'C', and 'F' with distances 5, 1, and 2, respectively.
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],  # 'C' connects to 'A', 'B', 'D', and 'E' with their distances.
    'D': [('C', 1), ('E', 9), ('F', 3)],   # 'D' connects to 'C', 'E', and 'F' with distances.
    'E': [('A', 11), ('C', 5), ('D', 9)],  # 'E' connects to 'A', 'C', and 'D'.
    'F': [('B', 2), ('D', 3)]              # 'F' connects to 'B' and 'D'.
}

# This function calculates the shortest path in an undirected weighted graph using Dijkstra's algorithm.
def shortest_path(graph, start, target=''):  # Takes in a graph, a start node, and an optional target node to find the shortest path.
    
    # List of all nodes that haven't been visited yet (Initially, it's all nodes).
    unvisited = list(graph)

    # Dictionary to store the shortest distance to each node from the start node. 
    # The distance to the start node is 0, and the rest are set to infinity (float('inf')).
    distances = {node: 0 if node == start else float('inf') for node in graph}
    
    # Dictionary to store the paths to reach each node. The path to the start node is initialized as just the start node itself.
    paths = {node: [] for node in graph}
    paths[start].append(start)  # Start node's path is itself.

    # Main loop to process all unvisited nodes.
    while unvisited:
        
        # Select the node with the smallest distance (greedy choice). This is Dijkstra's key feature.
        current = min(unvisited, key=distances.get)

        # Iterate over the neighbors of the current node.
        for node, distance in graph[current]:
            
            # If a shorter path is found, update the distance and the path.
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]  # Update the shortest distance.
                
                # If the path to the node has been found before and the last element is this node,
                # reset it to the current path.
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                
                # Otherwise, extend the current node's path with the new node.
                else:
                    paths[node].extend(paths[current])
                
                # Add the node to the path.
                paths[node].append(node)
        
        # Remove the node from the unvisited list since it has been processed.
        unvisited.remove(current)

    # If a target is provided, we only print that one. Otherwise, print all nodes' distances and paths.
    targets_to_print = [target] if target else graph

    # For each node, print the distance and path from the start node.
    for node in targets_to_print:
        
        # Skip printing for the start node.
        if node == start:
            continue
        
        # Print the distance and path from the start to the current node.
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')
    
    # Return the distances and paths dictionaries for further use if needed.
    return distances, paths

# Call the function to find the shortest path from node 'A' to node 'F' in the graph.
shortest_path(my_graph, 'A', 'F')
