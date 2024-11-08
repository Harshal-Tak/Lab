def is_valid(graph, node, color, assignment):
    for neighbor in graph[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(graph, colors, assignment):
    if len(assignment) == len(graph):
        return assignment
    
    node = [node for node in graph if node not in assignment][0]
    
    for color in colors:
        if is_valid(graph, node, color, assignment):
            assignment[node] = color
            result = backtrack(graph, colors, assignment)
            if result is not None:
                return result
            del assignment[node]
    
    return None

def graph_coloring(graph, colors):
    return backtrack(graph, colors, {})

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = ['Red', 'Green', 'Blue']

result = graph_coloring(graph, colors)
if result is not None:
    print("Graph coloring successful:")
    for node, color in result.items():
        print(f"Node {node} is colored {color}")
else:
    print("No solution found.")
