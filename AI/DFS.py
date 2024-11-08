no_of_nodes = int(input("Enter number of nodes: "))

graph = {}

for i in range(no_of_nodes):
    node = input("Enter node name: ")
    graph[node] = []
    no_of_neighb = int(input("Enter number of neighbours: "))
    lst = []
    for j in range(no_of_neighb):
        neighbour = input("Enter neighbour: ")
        lst.append(neighbour)
    graph[node] = lst
    
print(graph)

visited = set()

def dfs(graph,vertex,visited):
    if vertex not in visited:
        visited.add(vertex)
        print(vertex)
        for neighbour in graph[vertex]:
            dfs(graph,neighbour,visited)
            
v = input("Enter vertex name: ")

if v in graph:
    dfs(graph,v,visited)
