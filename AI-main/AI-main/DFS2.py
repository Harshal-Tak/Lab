no_of_v = int(input("Enter no of vertices: "))
graph = {}
for i in range(0, no_of_v):
    node = int(input("Enter node: "))
    neighbours = int(input("Enter number of neighbours: "))
    adj = []
    for j in range(0, neighbours):
        neighbour = int(input("Enter neighbour: "))
        adj.append(neighbour)
    graph[node] = adj

print(graph)

visited = set()

def dfs_with_goal_and_path(graph, visited, path, start, goal):
    if start not in visited:
        visited.add(start)
        path.append(start)
        
        if start == goal:
            return True, path
        
        for neighbour in graph[start]:
            result, new_path = dfs_with_goal_and_path(graph, visited, path.copy(), neighbour, goal)
            if result:
                return True, new_path
                
    return False, []

start_state = int(input("Enter start state: "))
goal_state = int(input("Enter goal state: "))

if start_state in graph and goal_state in graph:
    result, path = dfs_with_goal_and_path(graph, visited, [], start_state, goal_state)
    if result:
        print(f"Goal state {goal_state} found from start state {start_state}")
        print(f"Path: {path}")
    else:
        print(f"Goal state {goal_state} not found from start state {start_state}")
else:
    print("Start state or goal state not found in graph")
