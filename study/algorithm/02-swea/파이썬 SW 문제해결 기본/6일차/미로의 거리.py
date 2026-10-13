from collections import deque
t = int(input())

def bfs(sy,sx, ey, ex):
    q = deque()
    dist[sy][sx] = 0
    q.append((sy, sx))

    while q:
        y, x = q.popleft()
        if y == ey and x == ex:
            return dist[y][x]-1
        for dy, dx in [(0,1),(0,-1),(1,0),(-1,0)]:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < n and 0<= nx < n:
                if grid[ny][nx]!=1 and dist[ny][nx] == -1:
                    dist[ny][nx] = dist[y][x] + 1
                    q.append((ny, nx))

    return 0

for tc in range(1, t+1):
    n = int(input())
    grid = [list(map(int, input())) for _ in range(n)]

    dist = [[-1]*n for _ in range(n)]

    for y in range(n):
        for x in range(n):
            if grid[y][x] == 2:
                start=(y,x)
            elif grid[y][x] == 3:
                end = (y,x)

    ans = bfs(start[0], start[1], end[0], end[1])

    print(f"#{tc}", ans)