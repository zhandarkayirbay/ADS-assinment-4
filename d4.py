def dfs(current, open_count, close_count, n, result):

    if len(current) == 2 * n:
        result.append(current)
        return

    if open_count < n:
        dfs(
            current + "(",
            open_count + 1,
            close_count,
            n,
            result
        )

    if close_count < open_count:
        dfs(
            current + ")",
            open_count,
            close_count + 1,
            n,
            result
        )


def generate_parentheses(n):

    if n < 0:
        return []

    result = []

    dfs("", 0, 0, n, result)

    return result


n = int(input("n = "))

print(generate_parentheses(n))
