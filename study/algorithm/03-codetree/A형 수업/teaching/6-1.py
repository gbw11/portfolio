'''

회전이 쉽게, 한 방향부터 90도씩 돌려가면서 정의

우선순위가 있는 문제 => 우선순위에 따라 델타 배열 정의


    #   상 하 좌 우
dys = [-1, 1, 0, 0]
dxs = [0, 0, -1, 1]



curr_max = arr[y][x]
max_dir = -1

for i in range(4): # 상하좌우 값
    ny = y + dys[i]
    nx = x + dxs[i]

    # 가장 큰 값을 찾는다.
    if not in_range(ny, nx):
        continue

    if curr_max < arr[ny][nx]:
        curr_max = arr[ny][nx]
        max_dir = i

print(curr_max)
print(max_dir)  
'''

## 강사님 제출 코드

n, r, c = map(int, input().split())
a = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n+1):
    row = list(map(int, input().split()))
    for j in range(1, n + 1):
        a[i][j] = row[j - 1]

# Please write your code here.

def in_range(y, x):
    return 1<= y <= n and 1 <= x <= n

drs = [-1, 1, 0, 0]
dcs = [0, 0, -1, 1]


print(a[r][c], end=" ")
while True:
    nr, nc = r, c
    # 상 하 좌 우를 탐색

    for dr, dx in zip(drs, dcs):
        tr = r + dr
        tc = c + dcs

        # 격자 밖이면 패스
        if not in_range(nr, nc):
            continue

        # 현재 위치보다 더 작은 경우 패스
        if a[tr][tc] <= a[r][c]:
            continue
        
        # 아직 값이 바뀌지 않았다면
        if r == nr and c == nc:
            nr = tr
            nc = tc
        
    if r == nr and c == nc:
        break

    r, c = nr, nc
    print(a[r][c], end=" ")