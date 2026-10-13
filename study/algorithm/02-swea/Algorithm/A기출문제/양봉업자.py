T = int(input())

def check_t(y,x):
    center = grid[y][x]

    wings = []
    for dy, dx in (EVEN_SPEC if x % 2 == 0 else ODD_SPEC):

        for k in range(3):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < n and 0 <= nx < m:
                wings.append(grid[ny][nx])

        if len(wings) >= 3:
            wings.sort(reverse = True)
            costs.append(center + wings[0] + wings[1]+wings[2])

def dfs(y, x, lev, cost):
    if lev == 4:
        costs.append(cost)
        return
    visited[y][x] = True



    dy, dx = EVEN_NEXT if x % 2 == 0 else ODD_NEXT

    for k in range(6):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
            dfs(ny, nx, lev+1, cost+grid[ny][nx])

    visited[y][x] = False

for tc in range(1, T+1):
    n, m = map(int, input().split())

    grid = [list(map(int, input().split())) for _ in range(n)]

    max_val = max(map(max, grid))

    EVEN_NEXT = ([0, -1, 0, 1, -1, -1], [1, 0, -1, 0, -1, 1])
    ODD_NEXT = ([0, -1, 0, 1, 1, 1], [1, 0, -1, 0, 1, -1])

    EVEN_SPEC = (
        ([0, -1, 0], [1, 0, -1]),
        ([1, -1, -1], [0, -1, 1]),
    )
    ODD_SPEC = (
        ([-1, 1, 1], [0, 1, -1]),
        ([0, 0, 1], [1, -1, 0]),
    )

    costs = []
    visited = [[False]*m for _ in range(n)]

    for y in range(n):
        for x in range(m):
            dfs(y, x, 1, grid[y][x])
            check_t(y,x)

    print(f'#{tc}', max(costs))