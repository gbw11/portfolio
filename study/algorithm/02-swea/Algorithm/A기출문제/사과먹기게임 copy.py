from collections import deque
 
T = int(input())
 
for tc in range(1, T+1):
     
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    apples = {}
 
    dy= [-1, 0, 1, 0]
    dx= [0, 1, 0, -1]
 
    for y in range(N):
        for x in range(N):
            if arr[y][x] > 0:
                apples[arr[y][x]] = (y, x)
 
    cy, cx, cd = 0, 0, 1
    ans = 0
 
    for target in range(len(apples)):
        ty, tx = apples[target]
 
        dist = [[[float('inf')] * 4 for _ in range(N)] for _ in range(N)]
 
        q = deque()
        q.append((cy, cx, cd))
        dist[cy][cx][cd] = 0
 
        while q:
            y, x, d = q.popleft()
 
            if (ty, tx) == (y, x):
                ans += dist[y][x][d]
                cy, cx, cd = y, x, d
                break
 
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < N and 0 <= nx < N:
                if dist[ny][nx][d] > dist[y][x][d]:
                    dist[ny][nx][d] = dist[y][x][d]
                    q.appendleft((ny, nx, d))
 
            nd = (d + 1) % 4
            if dist[y][x][nd] > dist[y][x][d] + 1:
                dist[y][x][nd] = dist[y][x][d] + 1
                q.append((y,x,nd))
 
    print(f'#{tc} {ans}')