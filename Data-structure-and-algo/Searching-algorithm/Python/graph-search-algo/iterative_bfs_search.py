def iterative_bfs(g, node):
    visited = [] # List to keep track of visited nodes.
    queue = []   # Initialize a queue

    visited.append(node)
    queue.append(node)

    while queue:
        vertex = queue.pop(0)
        print(str(vertex) + " -> ", end="")
        for neighbour in g[vertex]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

    return visited


# Driver Code
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}
print("Output of Breadth First Traversal Algo: ")
iterative_bfs(graph, 'A')
