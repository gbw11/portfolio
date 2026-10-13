# G : 이동가능, T: 나무, X :현재위치 , Y 도착위치

# A: 앞으로 이동, L : 왼쪽 90도 회전, R : 오른쪽 90도 회전

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    grid = [list(input().strip()) for _ in range(n)]
    # q : 커맨드 횟수
    q = int(input())
    for y in range(n):
        for x in range(n):
            if grid[y][x] == "X":
                sy, sx = y, x
            elif grid[y][x] == "Y":
                ey, ex = y, x

    ans = []

    for _ in range(q):
        m, cmds = input().split()
        m = int(m)
        dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]
        # idx : 보고있는 방향 상우좌하
        idx = 0
        y, x = sy, sx
        for cmd in cmds:
            if cmd == "A":
                y += dy[idx]
                x += dx[idx]
                if y<0 or x<0 or y>=n or x >= n or grid[y][x]=="T":
                    y -= dy[idx]
                    x -= dx[idx]

            elif cmd == "R":
                idx = (idx + 1)%4

            elif cmd == "L":
                idx = (idx + 3)%4
        
        if y == ey and x == ex:
            ans.append(1)
        else:
            ans.append(0)

    print(f"#{tc}", *ans)

#===========추천 코드========

# G : 이동가능, T: 나무, X :현재위치 , Y 도착위치
# A: 앞으로 이동, L : 왼쪽 90도 회전, R : 오른쪽 90도 회전

t = int(input())

# 방향: 상, 우, 하, 좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for tc in range(1, t + 1):
    n = int(input())
    grid = [list(input().strip()) for _ in range(n)]

    # 시작, 도착 위치 찾기
    for y in range(n):
        for x in range(n):
            if grid[y][x] == 'X':
                sy, sx = y, x
            elif grid[y][x] == 'Y':
                ey, ex = y, x

    q = int(input())
    ans = []

    for _ in range(q):
        _, cmds = input().split()

        y, x = sy, sx
        d = 0  # 방향 (0:상)

        for cmd in cmds:
            if cmd == 'A':
                ny, nx = y + dy[d], x + dx[d]

                if 0 <= ny < n and 0 <= nx < n and grid[ny][nx] != 'T':
                    y, x = ny, nx

            elif cmd == 'R':
                d = (d + 1) % 4

            else:  # 'L'
                d = (d - 1) % 4

        ans.append(1 if (y, x) == (ey, ex) else 0)

    print(f"#{tc}", *ans)