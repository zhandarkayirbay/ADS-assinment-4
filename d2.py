def dfs(s, index, parts, current, result):

    if parts == 4 and index == len(s):
        result.append(current[:-1])
        return

    if parts > 4:
        return

    for length in range(1, 4):

        if index + length > len(s):
            break

        part = s[index:index + length]

        if (part[0] == '0' and len(part) > 1) or int(part) > 255:
            continue

        dfs(
            s,
            index + length,
            parts + 1,
            current + part + ".",
            result
        )


def restore_ip(s):

    result = []

    dfs(s, 0, 0, "", result)

    return result


s = input("s = ")

print(restore_ip(s))
