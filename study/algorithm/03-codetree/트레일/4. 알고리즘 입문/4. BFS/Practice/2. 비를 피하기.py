#수정한 코드(비를 피할 수 있는 곳에서부터 도달 가능한 거리를 다 저장)
# 아래 코드와 비교할 것
from collections import deque

# n 배열, h 사람, m 비 피할 공간
n, h, m = map(int, input().split())

# 0 이동가능 공간, 1 벽, 2 사람, 3 비 피할 수 있는 공간
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

def in_range(y, x):
    return 0 <= y < n and 0 <= x < n

def can_go(y, x):
    if not in_range(y, x) or grid[y][x] == 1:
        return False
    return True

# 피할수 있는 공간 저장
starts = []
for y in range(n):
    for x in range(n):
        if grid[y][x] == 3:
            starts.append((y, x))

result = [[0]*n for _ in range(n)]
# 피할수 있는 공간으로 부터의 거리를 배열에 기록
visited = [[False] * n for _ in range(n)]

def dfs():
    q = deque()
    for y, x in starts:
        visited[y][x] = True
        q.append((y, x))

    while q:
        y, x = q.popleft()

        for dy, dx in [(-1 ,0), (0, 1), (1, 0), (0, -1)]:
            ny = y + dy
            nx = x + dx
            if can_go(ny, nx) and not visited[ny][nx]:
                result[ny][nx] = result[y][x] + 1
                visited[ny][nx] = True
                q.append((ny, nx))

# 실행하면 result에 갈수 있는 곳들의 거리가 나온다.
dfs()

temp = [[0] * n for _ in range(n)]
for y in range(n):
    for x in range(n):
        # 사람이 서있는 곳!
        if grid[y][x] == 2:
            # 도달할 수 있는 거리를 입력하는데 도달하지 못하면 -1을 넣어준다.
            temp[y][x] = result[y][x] if result[y][x] != 0 else -1

for rows in temp:
    print(*rows)

###==========================================================###
## 각 사람에 대해서 피할수 잇는 곳까지의 최단 거리를 구하는 코드인데
# 사람이 많아지면 시간복잡도가 급격하게 상승해서 시간 초과가 발생함
# 따라서 비를 피할수 있는 모든 곳에서 이동 가능한 점까지의 최단 거리를 배열에 세겨 놓고
# 거기에 사람이 위치하면 그 값을 출력해준다.

# n 배열, h 사람, m 비 피할 공간
n, h, m = map(int, input().split())

# 0 이동가능 공간, 1 벽, 2 사람, 3 비 피할 수 있는 공간
grid = [list(map(int, input().split())) for _ in range(n)]


# Please write your code here.

def in_range(y, x):
    return 0 <= y < n and 0 <= x < n


def can_go(y, x):
    if not in_range(y, x) or grid[y][x] == 1:
        return False
    return True


# 사람들이 현재 있는 곳 저장
starts = []
for y in range(n):
    for x in range(n):
        if grid[y][x] == 2:
            starts.append((y, x))

result = [[0] * n for _ in range(n)]


def dfs(sy, sx):
    visited = [[-1] * n for _ in range(n)]
    q = deque()
    visited[sy][sx] = 0
    q.append((sy, sx))

    while q:
        y, x = q.popleft()
        if grid[y][x] == 3:
            result[sy][sx] = visited[y][x]
            break

        for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ny = y + dy
            nx = x + dx

            if can_go(ny, nx):
                visited[ny][nx] = visited[y][x] + 1
                q.append((ny, nx))


for y, x in starts:
    dfs(y, x)

for rows in result:
    print(*rows)
