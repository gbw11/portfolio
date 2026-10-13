from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# 0 존재 x , 1 귤, 2 상한 귤

visited = [[False] * n for _ in range(n)]

temp = [[0] * n for _ in range(n)]

starts = []

for y in range(n):
    for x in range(n):
        if grid[y][x] == 0:
            # 귤없는 구간을 방문처리함으로써 아래에서 따로 처리 안해도 된다.
            visited[y][x] = True
            temp[y][x] = -1
        elif grid[y][x] == 2:
            starts.append((y, x))

def in_range(y, x):
    return 0 <= y < n and 0 <= x < n

dys, dxs = [0, 0, 1, -1], [1, -1, 0, 0]

def bfs():
    q = deque()
    # 초기 상한 귤을 다 넣어주고
    for sy, sx in starts:
        visited[sy][sx] = True
        q.append((sy, sx))

    while q:
        y, x = q.popleft()

        for dy, dx in zip(dys, dxs):
            ny = y + dy
            nx = x + dx
            if in_range(ny, nx) and not visited[ny][nx]:
                temp[ny][nx] = temp[y][x] + 1
                visited[ny][nx] = True
                q.append((ny, nx))

bfs()
# 마지막까지 상하지 않은 귤 처리
for y in range(n):
    for x in range(n):
        if grid[y][x]==1 and temp[y][x]==0:
            temp[y][x] = -2

for rows in temp:
    print(*rows)