t = int(input())

for tc in range(1, t+1):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]

    target = 1
    cnt = 0
    # 보고있는 방향 북(0) 동(1) 남(2) 서(3)
    dir = 1
    now_y, now_x = 0, 0
    endnumber = max(max(rows) for rows in grid)
    while target <= endnumber:
        for y in range(n):
            for x in range(n):
                if grid[y][x] == target:
                    t1 = y - now_y
                    t2 = x - now_x

                    cmd = []
                    if t1 < 0: cmd.append(0) # 북
                    if t2 > 0: cmd.append(1) # 동
                    if t1 > 0: cmd.append(2) # 남
                    if t2 < 0: cmd.append(3) # 서

                    dy, dx = cmd
                    c1 = (dy-dir) % 4 + (dx -dy) % 4
                    c2 = (dx-dir) % 4 + (dy -dx) % 4
                    if c1 >= c2:
                        cnt += c2
                        dir = dy
                    else:
                        cnt += c1
                        dir = dx
                    now_y, now_x = y, x
                    target += 1
    print(f'#{tc}', cnt)