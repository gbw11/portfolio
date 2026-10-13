from collections import deque
from copy import deepcopy

k, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

answer = float('inf')

# 방향: 0=아래, 1=왼쪽, 2=위, 3=오른쪽
dys = [-1, 0, 1, 0]
dxs = [0, 1, 0, -1]

def in_range(y, x):
    return 0 <= y < n and 0 <= x < n

# ---------------------------
# 기울이기
# ---------------------------
def rotate(arr, direction):

    # 아래
    if direction == 0:
        for x in range(n):
            temp = []
            for y in range(n-1, -1, -1):
                if arr[y][x] != 0:
                    temp.append(arr[y][x])
            idx = 0
            for y in range(n-1, -1, -1):
                if idx < len(temp):
                    arr[y][x] = temp[idx]
                    idx += 1
                else:
                    arr[y][x] = 0

    # 왼쪽
    elif direction == 1:
        for y in range(n):
            temp = []
            for x in range(n):
                if arr[y][x] != 0:
                    temp.append(arr[y][x])
            idx = 0
            for x in range(n):
                if idx < len(temp):
                    arr[y][x] = temp[idx]
                    idx += 1
                else:
                    arr[y][x] = 0

    # 위
    elif direction == 2:
        for x in range(n):
            temp = []
            for y in range(n):
                if arr[y][x] != 0:
                    temp.append(arr[y][x])
            idx = 0
            for y in range(n):
                if idx < len(temp):
                    arr[y][x] = temp[idx]
                    idx += 1
                else:
                    arr[y][x] = 0

    # 오른쪽
    else:
        for y in range(n):
            temp = []
            for x in range(n-1, -1, -1):
                if arr[y][x] != 0:
                    temp.append(arr[y][x])
            idx = 0
            for x in range(n-1, -1, -1):
                if idx < len(temp):
                    arr[y][x] = temp[idx]
                    idx += 1
                else:
                    arr[y][x] = 0

# ---------------------------
# 대포 발사
# ---------------------------
def shoot(arr, direction, line):

    # 아래 (위에서 아래로 탐색)
    if direction == 0:
        for r in range(n):
            if arr[r][line] != 0:
                return r, line

    # 왼쪽 (오른쪽에서 왼쪽 탐색)
    elif direction == 1:
        for c in range(n-1, -1, -1):
            if arr[line][c] != 0:
                return line, c

    # 위 (아래에서 위 탐색)
    elif direction == 2:
        for r in range(n-1, -1, -1):
            if arr[r][line] != 0:
                return r, line

    # 오른쪽 (왼쪽에서 오른쪽 탐색)
    else:
        for c in range(n):
            if arr[line][c] != 0:
                return line, c

    return -1, -1


# ---------------------------
# 연쇄 폭발 BFS
# ---------------------------
def bfs(arr, sy, sx):

    q = deque()
    visited = [[False]*n for _ in range(n)]

    q.append((sy, sx, arr[sy][sx]))
    visited[sy][sx] = True

    while q:
        y, x, v = q.popleft()
        arr[y][x] = 0

        for dy, dx in zip(dys, dxs):
            for dist in range(1, v):
                ny = y + dy * dist
                nx = x + dx * dist

                if not in_range(ny, nx):
                    break

                if arr[ny][nx] != 0 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny, nx, arr[ny][nx]))


# ---------------------------
# 남은 개수 세기
# ---------------------------
def count_remain(arr):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                cnt += 1
    return cnt


# ---------------------------
# DFS 완전탐색
# ---------------------------
def dfs(turn, arr):
    global answer

    if turn == k:
        answer = min(answer, count_remain(arr))
        return

    direction = turn % 4

    for line in range(n):
        new_arr = deepcopy(arr)

        rotate(new_arr, direction)

        y, x = shoot(new_arr, direction, line)

        if y != -1:
            bfs(new_arr, y, x)
            rotate(new_arr, direction)

        dfs(turn + 1, new_arr)


dfs(0, grid)
print(answer)