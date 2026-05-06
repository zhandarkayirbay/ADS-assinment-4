from collections import deque


def multi_source_bfs(n, edges, sources):
    graph = {}

    for i in range(n):
        graph[i] = []

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    dist = [-1] * n
    queue = deque()

    for s in sources:
        dist[s] = 0
        queue.append(s)

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)

    return dist


n = int(input("n = "))
edges = eval(input("edges = "))
sources = eval(input("S = "))

dist = multi_source_bfs(n, edges, sources)

if -1 in dist:
    print("dist =", dist, "(-1 unreachable)")
else:
    print("dist =", dist)
