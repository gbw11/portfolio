
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

from collections import deque


visited = [[False ] *m for _ in range(n)]

def bfs(sy, sx):
    queue = deque()
    queue.append((sy, sx))
    visited[sy][sx] = True


    while queue:
        y, x = queue.popleft()
        if y== n - 1 and x == m - 1:
            return 1

        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < n and 0 <= nx < m:
                if not visited[ny][nx] and arr[ny][nx] == 1:
                    visited[ny][nx] = True
                    queue.append((ny, nx))

    return 0

result = bfs(0, 0)
print(result)