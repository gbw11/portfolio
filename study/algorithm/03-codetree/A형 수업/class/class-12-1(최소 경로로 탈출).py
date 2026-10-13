from collections import deque
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.


dist = [[-1]*m for _ in range(n)]

def bfs(sy, sx):
    q = deque()
    dist[sy][sx] = 0
    q.append((sy,sx))

    while q:
        y, x = q.popleft()

        for dy, dx in [(0,1),(0,-1),(-1,0),(1,0)]:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < n and 0 <= nx < m :
                if dist[ny][nx]==-1 and a[ny][nx]==1:
                    dist[ny][nx] = dist[y][x] + 1
                    q.append((ny, nx))

bfs(0, 0)

print(dist[n-1][m-1])