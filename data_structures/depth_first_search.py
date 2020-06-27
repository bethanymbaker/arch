# Using a Python dictionary to act as an adjacency list

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


# visited = set()

def depth_first(node, visited=set()):
    visited.add(node)
    print(f'node = {node}')
    children = [child for child in graph[node] if child not in visited]
    for child in children:
        depth_first(child, visited)


depth_first('A')
