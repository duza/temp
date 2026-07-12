from math import inf
from collections import deque


def find_lowest_cost_node(costs, processed: set[str]):
    lowest_cost = inf
    lowest_cost_node = None
    for node, cost in costs.items():
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def calculate_the_cheapest_way(finish, parents, costs):
    finish_cost = costs[finish]
    if finish_cost == inf:
        return finish_cost, None # the finish node is unreachable

    parent = finish
    cheapest_way = deque()
    while parent:
        cheapest_way.appendleft(parent)
        parent = parents[parent]
    
    return finish_cost, "->".join(cheapest_way)


def dijkstra(graph, costs, parents, finish):
    """
    Current implementation has O(V^2) complexity because we traverse all nodes in costs loop
    (find_lowest_cost_node). Also we go through all nodes in while loop -> looks like n^2
    """
    processed: set[str] = set()
    node = find_lowest_cost_node(costs, processed)

    while node is not None:
        cost = costs[node]
        for neighbor, weight in graph[node].items():
            new_cost = cost + weight
            # If it's cheaper to get to this neighbor by going through this node...
            if costs[neighbor] > new_cost:
                # update the cost for this node.
                costs[neighbor] = new_cost
                # This node becomes the new parent for this neighbor.
                parents[neighbor] = node

        processed.add(node)
        node = find_lowest_cost_node(costs, processed)
    
    return calculate_the_cheapest_way("D", parents, costs)


if __name__ == "__main__":
    # A --> B -> E --> D 
    #  \-> C <---|     ^
    #       \----------|
    graph = {
        "A": {"B": 6, "C": 2},
        "B": {"E": 3},
        "E": {"C": 5, "D": 1},
        "C": {"D": 4},
        "D": {},
    }
    costs = {node: inf for node in graph.keys()}
    costs["A"] = 0
    parents = {node: None for node in graph.keys()}
    print(dijkstra(graph=graph, costs=costs, parents=parents, finish="D"))
    # check unreachable finish node case
    graph2 = {"A": {"B": 2}, "B":{}, "C": {}}
    costs = {node: inf for node in graph.keys()}
    costs["A"] = 0
    parents = {node: None for node in graph.keys()}
    print(dijkstra(graph=graph2, costs=costs, parents=parents, finish="C"))