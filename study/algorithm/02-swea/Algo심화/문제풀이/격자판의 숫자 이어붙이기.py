def dfs(y, x):
    if len(path) == 7:
        ans.add(tuple(path[:]))
        return

    for dy, dx in zip(dys, dxs):
        ny = y + dy
        nx = x + dx
        if 0 <= ny < 4 and 0 <= nx < 4:
            path.append((grid[ny][nx]))
            dfs(ny, nx)
            path.pop()




t = int(input())

for tc in range(1, t+1):
    grid = [list(map(int, input().split())) for _ in range(4)]
    path = []
    ans = set()
    dys, dxs = [0,0,-1,1], [1,-1,0,0]
    for y in range(4):
        for x in range(4):
            path.append(grid[y][x])
            dfs(y, x)
            path.pop()

    print(f'#{tc}', len(ans))