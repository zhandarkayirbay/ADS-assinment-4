def dfs(node, graph, visited, component):

    visited.add(node)

    component.append(node)

    for neighbor in graph[node]:

        if neighbor not in visited:
            dfs(neighbor, graph, visited, component)


def connected_components(n, edges):

    if n == 0:
        return "0 components"

    graph = {}

    for i in range(n):
        graph[i] = []

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    components = []

    for node in range(n):

        if node not in visited:

            component = []

            dfs(node, graph, visited, component)

            components.append(component)

    result = str(len(components)) + " components: "

    parts = []

    for component in components:
        parts.append(str(set(component)))

    result += ", ".join(parts)

    return result


n = int(input("n = "))
edges = eval(input("edges = "))

print(connected_components(n, edges))
