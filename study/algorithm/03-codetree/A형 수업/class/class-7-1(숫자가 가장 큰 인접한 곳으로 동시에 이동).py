n, m, t = map(int, input().split())

# Create n x n grid
arr = [list(map(int, input().split())) for _ in range(n)]

# Get m marble positions
marbles = [tuple(map(int, input().split())) for _ in range(m)]
row = [pos[0] for pos in marbles]
col = [pos[1] for pos in marbles]

# Please write your code here.

def in_range(y, x):
    return 0 <= y < n and 0 <= x < n

# 구슬 위치를 저장하는 배열

pos = [[0]*n for _ in range(n)]
for r, c in zip(row, col):
    pos[r-1][c-1] = 1

# 우선순위 상 하 좌 우
dys, dxs = [-1, 1, 0, 0], [0, 0, -1, 1]

time = 0
while time < t:
    nxt_pos = [[0]*n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if pos[y][x] == 1:
                # 상하좌우 최댓값 저장하기위함
                curr_val = -1
                # 다음 이동 위치 저장
                nxt_y, nxt_x = -1, -1
                for dy, dx in zip(dys, dxs):
                    ny = y + dy
                    nx = x + dx
                    if not in_range(ny, nx): continue
                    if arr[ny][nx] > curr_val:
                        curr_val = arr[ny][nx]
                        nxt_y, nxt_x = ny, nx

                nxt_pos[nxt_y][nxt_x] += 1

    for y in range(n):
        for x in range(n):
            if nxt_pos[y][x] >= 2:
                nxt_pos[y][x] = 0

    pos = [rows[:] for rows in nxt_pos]

    time += 1

print(sum(sum(rows) for rows in pos))