n, k = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]


def in_range(y, x):
    return 0 <= y < n and 0 <= x < n


dys, dxs = [0, 0, 1, -1], [1, -1, 0, 0]

visited = [[False]*n for _ in range(n)]


ans = 0
def dfs(y, x, used_k, length):
    global ans, max_height

    visited[y][x] = True
    ans = max(ans, length)

    for dy, dx in zip(dys, dxs):
        ny = y + dy
        nx = x + dx
        if not in_range(ny, nx):
            continue

        if grid[ny][nx] < grid[y][x] and not visited[ny][nx]:
            dfs(ny, nx, used_k, length + 1)

        elif grid[ny][nx] >= grid[y][x] and not visited[ny][nx]:

            needed = grid[ny][nx] - (grid[y][x] - 1)

            if used_k + needed <= k:
                new_height = grid[ny][nx] - needed
                if new_height < 1:
                    continue

                original = grid[ny][nx]
                grid[ny][nx] -= needed
                dfs(ny, nx, used_k + needed, length+1)
                grid[ny][nx] = original

    visited[y][x] = False

    return

max_height = max(max(row) for row in grid)

for y in range(n):
    for x in range(n):
        if grid[y][x] == max_height:
            dfs(y, x, 0, 1)
            
print(ans)