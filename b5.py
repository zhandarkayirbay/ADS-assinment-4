from collections import deque


def neighbors(word, words):
    result = []

    for w in words:
        diff = 0

        for i in range(len(word)):
            if word[i] != w[i]:
                diff += 1

        if diff == 1:
            result.append(w)

    return result


def bfs(begin, end, words):
    if end not in words:
        return "0 (no solution)"

    queue = deque()
    queue.append((begin, 1))

    visited = set()
    visited.add(begin)

    while queue:
        word, steps = queue.popleft()

        if word == end:
            return steps

        for nxt in neighbors(word, words):
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, steps + 1))

    return "0 (no solution)"


begin = input("begin = ")
end = input("end = ")
words = eval(input("dict = "))

print(bfs(begin, end, words))
