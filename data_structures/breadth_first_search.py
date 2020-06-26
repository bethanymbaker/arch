from queue import Queue

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = []
que = Queue()

root_node = 'A'
que.put(root_node)
visited.append(root_node)

while not que.empty():
    node = que.get()
    print(f'node = {node}')
    children = graph[node]
    for child in children:
        if child not in visited:
            visited.append(child)
            que.put(child)

print(f'visited = {visited}')
