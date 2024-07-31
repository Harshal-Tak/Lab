no_of_vertices = int(input("Enter no. of vertices: "))
graph = {}

for i in range(0,no_of_vertices):
    node = input("Enter node: ")
    neighbours = int(input("No of neighbours: "))
    adj = []
    for j in range(0,neighbours):
        neighbour = input("Neighbour: ")
        adj.append(neighbour)
    graph[node] = adj
    
visited = set()

def bfs(graph,visited,queue):
    if not queue:
        return
    
    v = queue.pop(0)
    print(v)
    
    for neighbour in graph[v]:
        if neighbour not in visited:
            visited.add(neighbour)
            queue.append(neighbour)
    bfs(graph,visited,queue)
                
queue = ['1']
visited.add('1')
bfs(graph,visited,queue)
