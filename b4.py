from collections import deque


def bfs(N, start, target):

    moves = [
        (-2, -1), (-2, 1),
        (-1, -2), (-1, 2),
        (1, -2), (1, 2),
        (2, -1), (2, 1)
    ]

    visited = [[False] * N for _ in range(N)]

    queue = deque()

    sx, sy = start
    tx, ty = target

    queue.append((sx, sy, 0))

    visited[sx][sy] = True

    while queue:

        x, y, steps = queue.popleft()

        if (x, y) == (tx, ty):
            return steps

        for dx, dy in moves:

            nx = x + dx
            ny = y + dy

            if 0 <= nx < N and 0 <= ny < N:

                if not visited[nx][ny]:

                    visited[nx][ny] = True

                    queue.append((nx, ny, steps + 1))

    return "-1 (unreachable)"


N = int(input("N = "))
start = eval(input("start = "))
target = eval(input("target = "))

print(bfs(N, start, target))
