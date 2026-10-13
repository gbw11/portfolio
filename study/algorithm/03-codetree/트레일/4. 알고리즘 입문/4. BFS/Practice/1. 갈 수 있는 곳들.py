n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.

from collections import deque

visited = [[False] * n for _ in range(n)]

cnt = 0


def bfs(sy, sx):
    global cnt
    # 시작점이 이미 다른 곳에서 방문했다면 굳이 할 필요없기 때문에
    if visited[sy][sx]:
        return
    # 시작점도 세야하기 때문에
    cnt += 1
    queue = deque()
    visited[sy][sx] = True
    queue.append((sy, sx))

    while queue:
        y, x = queue.popleft()

        for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < n and 0 <= nx < n:
                if not visited[ny][nx] and grid[ny][nx] == 0:
                    cnt += 1
                    visited[ny][nx] = True
                    queue.append((ny, nx))

    return cnt


for y, x in points:
    # 행과 열 0부터 시작하기 위해서 -1씩 해준다.
    bfs(y - 1, x - 1)

print(cnt)