n, r, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

r, c = r - 1, c - 1  # 배열 인덱스 맞추기
# 우 좌 하 상  => 우선순위 낮은거 부터 돌리기
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


def in_range(y, x):
    return 0 <= y < n and 0 <= x < n


max_y, max_x = -1, -1
y, x = r, c
result = []
while True:
    result.append(arr[y][x])

    cnt = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if in_range(ny, nx) and arr[ny][nx] > arr[y][x]:
            max_y, max_x = ny, nx
            cnt += 1

    y, x = max_y, max_x
    if cnt == 0: break

print(*result)