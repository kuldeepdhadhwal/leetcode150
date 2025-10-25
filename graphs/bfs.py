bfs = {
    'a' : ['b', 'c'],
    'b' : ['a', 'd', 'e'],
    'c' : ['a', 'f'],
    'd' : ['b'],
    'e' : ['b', 'f'],
    'f' : ['c', 'e']
}

def bfs_traversal(graph, start):
    visited = set([start])
    queue = [start]

    while queue:
        print("Queue:", queue)
        vertex = queue.pop(0)

        for graph_node in bfs[vertex]:
            if graph_node not in visited:
                visited.add(graph_node)
                queue.append(graph_node)
        print("Visited:", visited)


bfs_traversal(bfs, 'a')