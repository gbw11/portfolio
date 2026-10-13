from collections import deque
from itertools import combinations

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1

# Please write your code here.

blocks = []
for y in range(n):
    for x in range(n):
        if grid[y][x] == 1:
            blocks.append((y,x))

def bfs(sy,sx):
    dist = [[-1]*n for _ in range(n)]
    dist[sy][sx] = 0
    q = deque([(sy,sx)])

    while q:
        y, x = q.popleft()

        for dy, dx in [(0,1),(0,-1),(1,0),(-1,0)]:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < n and 0 <= nx < n:
                if dist[ny][nx]==-1 and grid[ny][nx]==0:
                    dist[ny][nx] = dist[y][x] + 1
                    q.append((ny,nx))

    return dist[r2][c2]

ans = 10000
for block in combinations(blocks, k):
    for y, x in block:
        grid[y][x] = 0

    tmp = bfs(r1, c1)
    if tmp != -1:
        ans = min(ans, tmp)

    for y, x in block:
        grid[y][x] = 1

print(-1 if ans ==10000 else ans)