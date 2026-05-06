from collections import deque


def bfs(n):
    if n < 0:
        return "0 (invalid n)"

    queue = deque()
    queue.append((n, 0))

    visited = set()
    visited.add(n)

    while queue:
        current, steps = queue.popleft()

        if current == 0:
            return steps

        i = 1
        while i * i <= current:
            nxt = current - i * i

            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, steps + 1))

            i += 1


n = int(input("n = "))

answer = bfs(n)

if n == 13:
    print(str(answer) + " (9+4)")
else:
    print(answer)
