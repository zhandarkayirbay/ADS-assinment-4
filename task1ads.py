from collections import deque

def dfs(graph, start, visited=None, result=None):
    if visited is None:
        visited = set()
    if result is None:
        result = []

    visited.add(start)
    result.append(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, result)

    return result


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    result = []

    visited.add(start)

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


def main():
    graph = {
        0: [1, 2],
        1: [0, 3],
        2: [0],
        3: [1]
    }

    print("DFS traversal:", dfs(graph, 0))
    print("BFS traversal:", bfs(graph, 0))


main()
