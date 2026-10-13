t = int(input())

def dfs(y, x):
    visited = [[False]*n for _ in range(n)]
    global cnt
    visited[y][x] = True
    cnt += 1
    path = []
    for dy, dx in zip(dys, dxs):
        ny = y + dy
        nx = x + dx
        if 0 <= ny < n and 0 <= nx < n:
            if not visited[ny][nx] and grid[ny][nx] < grid[y][x]:
                path.append((grid[ny][nx],ny, nx))
    if not path:
        return
    path.sort()
    d, cy, cx = path.pop(0)
    dfs(cy, cx)
    

for tc in range(1, t+1):
    n = int(input())

    grid = [list(map(int, input().split())) for _ in range(n)]


    dys, dxs = [0,0,1,-1], [1,-1,0,0]
    ans = 0
    for y in range(n):
        for x in range(n):
            cnt = 0
            dfs(y, x)
            ans = max(ans, cnt)
    print(f'#{tc}', ans)