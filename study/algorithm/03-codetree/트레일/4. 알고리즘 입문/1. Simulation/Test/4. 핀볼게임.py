n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]


# Please write your code here.


def in_range(y, x):
    return 0 <= y < n and 0 <= x < n


def escape(y, x, i):  # 시작지점의 위치와 출발 방향
    # 가지치기 ! 출발 점의 진행방향에 거울이 아예없으면 굳이 탐색 x
    # 열체크
    if i == 0 or i == 2:
        col_cnt = 0
        for k in range(n):
            col_cnt += grid[k][x]
        if col_cnt == 0: return 0

    # 행체크
    if i == 1 or i == 3:
        row_cnt = 0
        for k in range(n):
            row_cnt += grid[y][k]
        if row_cnt == 0: return 0

    dys, dxs = [-1, 0, 1, 0], [0, 1, 0, -1]
    cnt = 0
    ty, tx = y, x
    idx = i
    while True:
        cnt += 1
        ny = ty + dys[idx]
        nx = tx + dxs[idx]
        if not in_range(ny, nx):
            break
        if grid[ny][nx] == 1:
            # 북 동 남 서 => 동 북 서 남
            if idx < 2:
                idx = 1 - idx
            else:
                idx = 5 - idx

        elif grid[ny][nx] == 2:
            # 북 동 남 서 => 서 남 동 북
            idx = 3 - idx
        ty, tx = ny, nx
    return cnt


points = []

# 테두리의 좌표와 들어와야할 방향을 넣었다.
points = []

for i in range(n):
    # 좌표들을 밖에서 출발 시킴!
    points.append((-1, i, 2))
    points.append((n, i, 0))
    points.append((i, -1, 1))
    points.append((i, n, 3))

result = n + 1
for point in points:
    result = max(result, escape(point[0], point[1], point[2]))

print(result)