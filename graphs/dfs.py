dfs = {
    'a' : ['b', 'c'],
    'b' : ['a', 'd', 'e'],
    'c' : ['a', 'f'],
    'd' : ['b'],
    'e' : ['b', 'f'],
    'f' : ['c', 'e']
}

def dfs_traversal(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)

    print("Visited:", visited)
    for graph_node in graph[start]:
        if graph_node not in visited:
            dfs_traversal(graph, graph_node, visited)


dfs_traversal(dfs, 'a')