grid = [[0]*5 for _ in range(5)]

y, x = map(int, input().split())

from collections import deque

def bfs(sy,sx):
    grid[sy][sx] = 1
    q = deque([(sy,sx)])

    while q:
        y, x = q.popleft()

        for dy, dx in [(0,1),(0,-1),(1,0),(-1,0)]:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < 5 and 0 <= nx < 5:
                if grid[ny][nx] == 0:
                    grid[ny][nx] = grid[y][x] + 1
                    q.append((ny, nx))
bfs(y,x)

for rows in grid:
    print(*rows)