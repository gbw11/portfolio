n, m, t = map(int, input().split())  # n 행과 열, m 구슬의 개수, t 시간

# Create n x n grid
arr = [list(map(int, input().split())) for _ in range(n)]

# Get m marble positions
marbles = [tuple(map(int, input().split())) for _ in range(m)]
r = [pos[0] for pos in marbles]
c = [pos[1] for pos in marbles]

# Please write your code here.

# 현재 위치를 기록한 배열
temp = [[0] * n for _ in range(n)]
for i in range(m):
    temp[r[i] - 1][c[i] - 1] = 1  # 인덱싱 하기 위해서 -1씩


def in_range(y, x):
    return 0 <= y < n and 0 <= x < n


# 같을경우 우선순위 상 하 좌 우
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

time = 0
while time < t:
    next_temp = [[0] * n for _ in range(n)]  # 다음 기록할 배열 while 돌때마다 초기화
    for y in range(n):
        for x in range(n):
            if temp[y][x] == 1:  # 반복문 돌렸을 때 겹치는 부분 있을 수 있기 때문에 1 이상인 값에 대해서 탐색

                curr_y, curr_x = y, x  # 0 이 벗어나는 경우 체크
                number = 0
                for j in range(4):
                    ny = y + dy[j]
                    nx = x + dx[j]
                    if in_range(ny, nx):
                        if arr[ny][nx] > number:  # 같을 경우 우선순위 탐색임으로 같다 포함 X
                            number = arr[ny][nx]
                            curr_y, curr_x = ny, nx

                next_temp[curr_y][curr_x] += 1  # 다음 구슬의 위치 저장

    # 만난 구슬이 존재하면 삭제하는 부분
    for y in range(n):
        for x in range(n):
            if next_temp[y][x] >= 2:
                next_temp[y][x] = 0

    temp = next_temp  # 기록된 배열 저장
    time += 1

cnt = 0
for y in range(n):
    for x in range(n):
        if temp[y][x] == 1:
            cnt += 1

print(cnt)
