import json
from typing import Any
from collections import defaultdict


def create_graph(data_json: list[dict[str, Any]]) -> defaultdict[str, set[str]]:
    """Build an adjacency map where each parent points to its child nodes."""
    graph: defaultdict[str, set[str]] = defaultdict(set)
    for entry in data_json:
        name = entry["name"]
        for parent in entry.get("parents", ()):
            graph[parent].add(name)
    return graph


def dfs(graph: dict[str, set[str]], start: str) -> set[str]:
    """Return all nodes reachable from start using depth-first search."""
    visited: set[str] = set()
    stack: list[str] = [start]

    while stack:
        vertex = stack.pop()
        if vertex in visited:
            continue

        visited.add(vertex)
        stack.extend(
            neighbor for neighbor in graph.get(vertex, ()) if neighbor not in visited
        )

    return visited


if __name__ == "__main__":
    data_json = json.loads(input())
    graph = create_graph(data_json)
    data_json.sort(key=lambda x: x["name"])
    for entry in data_json:
        print(f"{entry['name']} : {len(dfs(graph, entry['name']))}")
