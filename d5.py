def dfs(node, parent, graph, visited):

    visited.add(node)

    for neighbor in graph[node]:

        if neighbor not in visited:

            if dfs(neighbor, node, graph, visited):
                return True

        elif neighbor != parent:
            return True

    return False


def has_cycle(n, edges):

    graph = {}

    for i in range(n):
        graph[i] = []

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    for node in range(n):

        if node not in visited:

            if dfs(node, -1, graph, visited):
                return "YES"

    return "NO"


n = int(input("n = "))
edges = eval(input("edges = "))

print(has_cycle(n, edges))
