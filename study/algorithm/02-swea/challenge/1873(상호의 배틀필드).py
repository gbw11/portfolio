t = int(input())

for tc in range(1, t+1):
    h, w = map(int, input().split())
    grid = [list(input().strip()) for _ in range(h)]
    n = int(input())
    cmds = input().strip()

    # 방향 설정
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    dir_map = {'U':0, 'D':1, 'L':2, 'R':3}
    tank = ['^', 'v', '<', '>']

    # 탱크 위치 찾기
    for y in range(h):
        for x in range(w):
            if grid[y][x] in tank:
                d = tank.index(grid[y][x])
                ty, tx = y, x

    # 명령 수행
    for cmd in cmds:
        # 🔫 포탄
        if cmd == 'S':
            ny, nx = ty, tx
            while True:
                ny += dy[d]
                nx += dx[d]

                if not (0 <= ny < h and 0 <= nx < w):
                    break
                if grid[ny][nx] == '#':
                    break
                if grid[ny][nx] == '*':
                    grid[ny][nx] = '.'
                    break

        # 🚶 이동
        else:
            d = dir_map[cmd]
            grid[ty][tx] = tank[d]

            ny = ty + dy[d]
            nx = tx + dx[d]

            if 0 <= ny < h and 0 <= nx < w and grid[ny][nx] == '.':
                grid[ty][tx] = '.'
                grid[ny][nx] = tank[d]
                ty, tx = ny, nx

    # 출력
    print(f"#{tc}", end=" ")
    for row in grid:
        print("".join(row))