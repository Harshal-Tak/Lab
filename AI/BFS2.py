no_of_vertices = int(input("Enter no. of vertices: "))
graph = {}

# Input nodes and their neighbors to construct the graph
for i in range(0,no_of_vertices):
    node = input("Enter node: ")
    neighbours = int(input("No of neighbours: "))
    adj = []
    for j in range(0,neighbours):
        neighbour = input("Neighbour: ")
        adj.append(neighbour)
    graph[node] = adj


def bfs_with_end_state(graph, start, end):
    visited = set()
    queue = [[start]]
    
    while queue:
        path = queue.pop(0)
        node = path[-1]
        
        if node == end:
            return path
        
        if node not in visited:
            for neighbour in graph[node]:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
            visited.add(node)
    return None

start_state = input("Enter start state: ")
end_state = input("Enter end state: ")

path = bfs_with_end_state(graph, start_state, end_state)

if path:
    print(f"Shortest path from {start_state} to {end_state}: {path}")
else:
    print(f"No path found from {start_state} to {end_state}")
