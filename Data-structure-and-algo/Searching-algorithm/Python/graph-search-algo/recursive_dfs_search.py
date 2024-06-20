# DFS algorithm
def recursive_dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)

    print("vertex visit at: ", start)

    for move in graph[start] - visited:
        recursive_dfs(graph, move, visited)
    return visited


g = {'0': set(['1', '2']),
     '1': set(['0', '3', '4']),
     '2': set(['0']),
     '3': set(['1']),
     '4': set(['2', '3'])}

recursive_dfs(g, '0')
