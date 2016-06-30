import json

def create_graph(data_json):
    graph = {}
    for el in data_json:
        for parent in el['parents']:
            graph[parent] = graph.get(parent) or set()
            graph[parent].add(el['name'])
    return graph

	
def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph.get(vertex,set()) - visited)
    return visited

if __name__ == '__main__':
    data_json = json.loads(input())
    graph = create_graph(data_json)
    data_json.sort(key=lambda x: x['name'])
    for el in data_json:
        print('{} : {}'.format(el['name'], len(dfs(graph,el['name']))))
