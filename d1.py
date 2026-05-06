def dfs_grid(row, col, grid, visited):
    n = len(grid)
    m = len(grid[0])

    if row < 0 or row >= n or col < 0 or col >= m:
        return False

    if grid[row][col] == 1:
        return False

    if (row, col) in visited:
        return False

    if row == n - 1 and col == m - 1:
        return True

    visited.add((row, col))

    return (
        dfs_grid(row + 1, col, grid, visited) or
        dfs_grid(row - 1, col, grid, visited) or
        dfs_grid(row, col + 1, grid, visited) or
        dfs_grid(row, col - 1, grid, visited)
    )


def can_reach_end(grid):
    visited = set()

    if dfs_grid(0, 0, grid, visited):
        return "YES"

    return "NO"


grid = eval(input("grid = "))

print(can_reach_end(grid))
