from collections import deque
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# grid 내부에서 1 이동 가능, 0 이동불가

visited = [[False] * m for _ in range(n)]

step = [[-1] * m for _ in range(n)]

dys, dxs = [0 ,0, 1 ,-1], [1, -1, 0, 0]

def in_range(y, x):
    return 0<= y < n and 0<= x <m

def bfs(sy, sx):
    q = deque()
    visited[sy][sx] = True
    q.append((sy, sx))
    step[sy][sx] = 0
    

    while q:
        y, x = q.popleft()

        for dy, dx in zip(dys, dxs):
            ny = y + dy
            nx = x + dx
            if in_range(ny, nx) and not visited[ny][nx] and grid[ny][nx] == 1:
                step[ny][nx] = step[y][x] + 1
                visited[ny][nx] = True
                q.append((ny, nx))

step[0][0] = 0
bfs(0, 0)
print(step[n-1][m-1])

## 아래는 최적화한 코드 - visited 배열 삭제하고 step 안에서 visited 까지 관리해버리기
from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 이동 방향
dirs = [(0,1), (0,-1), (1,0), (-1,0)]

# 거리 배열 (-1 = 방문 안함)
step = [[-1] * m for _ in range(n)]

def bfs():
    if grid[0][0] == 0:
        return -1

    q = deque([(0, 0)])
    step[0][0] = 0

    while q:
        y, x = q.popleft()

        # 도착하면 바로 종료 (조기 종료 최적화)
        if (y, x) == (n-1, m-1):
            return step[y][x]

        for dy, dx in dirs:
            ny, nx = y + dy, x + dx

            if 0 <= ny < n and 0 <= nx < m:
                if grid[ny][nx] == 1 and step[ny][nx] == -1:
                    step[ny][nx] = step[y][x] + 1
                    q.append((ny, nx))

    return -1  # 도달 불가능

print(bfs())