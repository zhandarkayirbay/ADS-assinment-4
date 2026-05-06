def dfs(candidates, target, index, path, result):

    if target == 0:
        result.append(path[:])
        return

    if target < 0:
        return

    for i in range(index, len(candidates)):

        path.append(candidates[i])

        dfs(
            candidates,
            target - candidates[i],
            i,
            path,
            result
        )

        path.pop()


def combination_sum(candidates, target):

    result = []

    dfs(candidates, target, 0, [], result)

    return result


candidates = eval(input("candidates = "))
target = int(input("T = "))

print(combination_sum(candidates, target))
