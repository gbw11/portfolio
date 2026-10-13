n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.


visited = [[False]*m for _ in range(n)]

def in_range(y, x):
    return 0 <= y < n and 0 <= x < m

def can_go(y, x):
    if not in_range(y, x):
        return False

    if visited[y][x] or grid[y][x] == 0:
        return False
    return True

dys, dxs = [1, 0], [0, 1]

valid = False
def dfs(y, x):
    global valid
    if valid:
        return
    if y == n - 1 and x == m - 1:
        valid = True
        return

    visited[y][x] = True

    for dy, dx in zip(dys, dxs):
        ny = y + dy
        nx = x + dx
        if can_go(ny, nx):
            dfs(ny, nx)

dfs(0, 0)
print(1 if valid else 0)