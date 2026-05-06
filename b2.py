from collections import deque


def bfs(F, S, G, U, D):

    visited = [False] * (F + 1)

    queue = deque()

    queue.append((S, 0))

    visited[S] = True

    while queue:

        floor, presses = queue.popleft()

        if floor == G:
            return presses

        up = floor + U

        if up <= F and not visited[up]:
            visited[up] = True
            queue.append((up, presses + 1))

        down = floor - D

        if down >= 1 and not visited[down]:
            visited[down] = True
            queue.append((down, presses + 1))

    return "IMPOSSIBLE"


F = int(input("F = "))
S = int(input("S = "))
G = int(input("G = "))
U = int(input("U = "))
D = int(input("D = "))

print(bfs(F, S, G, U, D))
