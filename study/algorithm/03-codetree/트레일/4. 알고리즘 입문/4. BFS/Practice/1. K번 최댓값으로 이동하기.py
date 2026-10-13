n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r -= 1
c -= 1
# Please write your code here.
from collections import deque


def bfs(sy, sx):
    visited = [[False] * n for _ in range(n)]
    visited[sy][sx] = True
    q = deque([(sy, sx)])

    max_val = -1
    pos = []

    while q:
        y, x = q.popleft()

        for dy, dx in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            ny = y + dy
            nx = x + dx

            if 0 <= ny < n and 0 <= nx < n:
                if not visited[ny][nx] and grid[ny][nx] < grid[sy][sx]:
                    visited[ny][nx] = True
                    q.append((ny, nx))
                    if grid[ny][nx] > max_val:
                        max_val = grid[ny][nx]
                        pos = [(ny, nx)]
                    elif grid[ny][nx] == max_val:
                        pos.append((ny, nx))

                        # 이동 불가할 경우 현재 위치 반환
    if not pos:
        return sy, sx
    pos.sort()
    return pos[0]


y, x = r, c

for _ in range(k):
    y, x = bfs(y, x)

print(y + 1, x + 1)