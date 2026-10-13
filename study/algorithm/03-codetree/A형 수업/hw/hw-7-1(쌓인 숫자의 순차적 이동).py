n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
move_nums = list(map(int, input().split()))

# 한 칸에 여러 개 들어갈 수 있게 변환
for y in range(n):
    for x in range(n):
        grid[y][x] = [grid[y][x]]

def in_range(y, x):
    return 0 <= y < n and 0 <= x < n

dys = [-1, -1, 0, 1, 1, 1, 0, -1]
dxs = [0, 1, 1, 1, 0, -1, -1, -1]

for num in move_nums:
    # 값을 찾으면 그 아래에서 다시 탐색하는 것을 방지하기 위한 수단
    found = False

    for y in range(n):
        for x in range(n):
            if num in grid[y][x]:
                max_value = -1
                nxt_y, nxt_x = -1, -1

                # 8방향 탐색
                for dy, dx in zip(dys, dxs):
                    ny, nx = y + dy, x + dx
                    if not in_range(ny, nx):
                        continue

                    for val in grid[ny][nx]:
                        if val > max_value:
                            max_value = val
                            nxt_y, nxt_x = ny, nx

                if nxt_y == -1:
                    continue

                # num 위치 찾기
                for idx, val in enumerate(grid[y][x]):
                    if val == num:
                        grid[nxt_y][nxt_x] += grid[y][x][idx:]
                        grid[y][x] = grid[y][x][:idx]
                        break

                found = True
                break
        if found:
            break

# 출력
for y in range(n):
    for x in range(n):
        if not grid[y][x]:
            print(None)
        else:
            print(*grid[y][x][::-1])