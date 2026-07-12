from collections import deque

def bfs(graph, start):
    visited, queue = set(), deque([start])
    while queue:
        vertex = queue.popleft()

        if vertex in visited:
            continue

        visited.add(vertex)
        queue.extend(neighbor for neighbor in graph.get(vertex, ()) if neighbor not in visited)
    return visited

# A -- B -- D
#   \- C
#       \- E
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D'},
    'C': {'A', 'E'},
    'D': {'B'},
    'E': {'C'},
}
print(bfs(graph, 'A'))