# import sys
# sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline

from collections import deque

# 벽돌의 연쇄작용
def bfs(sy,sx):
    q = deque()
    visited = [[False]*w for _ in range(h)]
    visited[sy][sx] = True
    q.append((sy, sx, grid[sy][sx]))
    grid[sy][sx] = 0

    while q:
        y, x, dist = q.popleft()

        for dy, dx in [(-1,0),(1,0),(0,1),(0,-1)]:
            for d in range(1, dist):
                ny = y + dy*d
                nx = x + dx*d
                if 0 <= ny < h and 0 <= nx < w:
                    if not visited[ny][nx]:
                        visited[ny][nx] = True
                        if grid[ny][nx] != 0:
                            q.append((ny, nx, grid[ny][nx]))
                            grid[ny][nx] = 0
    return

# 중력 작용함수
def gravity(arr):
    nxt_arr = [[0] * w for _ in range(h)]
    for x in range(w):
        tmp = []
        for y in range(h):
            if arr[y][x] != 0:
                tmp.append(arr[y][x])

        tmp = [0] * (h - len(tmp)) + tmp[:]
        for i in range(h):
            nxt_arr[i][x] = tmp[i]

    return nxt_arr

# 몇번째 줄에 폭탄을 떨굴지 dfs로 하기
path = []
num_of_case = []
def dfs(lev):
    if lev == n:
        num_of_case.append(path[:])
        return
    for i in range(w):
        path.append(i)
        dfs(lev+1)
        path.pop()

t = int(input())

for tc in range(1, t+1):
    # n 슈팅 가능 횟수
    n, w, h = map(int, input().split())
    grids = [list(map(int, input().split())) for _ in range(h)]

    path = []
    num_of_case = []
    # 떨어트릴 모든 열을 고름!
    dfs(0)
    min_val = 10000
    for tmp in num_of_case:
        grid = [rows[:] for rows in grids]
        for i in tmp:
            for y in range(h):
                if grid[y][i] != 0:
                    bfs(y,i)
                    grid = gravity(grid)
                    break

        count = sum(1 for row in grid for x in row if x!=0)
        min_val = min(min_val, count)

    print(f'#{tc}', min_val)
