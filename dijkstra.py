def find_lowest_cost_node(costs, processed: set[str]):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def dijkstra(graph, costs, parents):
    processed: set[str] = set()
    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            # If it's cheaper to get to this neighbor by going through this node...
            if costs[n] > new_cost:
                # update the cost for this node.
                costs[n] = new_cost
                # This node becomes the new parent for this neighbor.
                parents[n] = node
        processed.add(node)
        node = find_lowest_cost_node(costs, processed)


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
    infinity = float("inf")
    costs = {node: infinity for node in graph.keys()}
    costs["A"] = 0
    parents = {node: None for node in graph.keys()}
    dijkstra(graph=graph, costs=costs, parents=parents)