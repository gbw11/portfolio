# . : 평지, *:벽돌,  #:강철, -:물
# import sys
# sys.stdin = open("input.txt", "r")

# sys.stdin = open(r"C:\Users\USER\OneDrive\바탕 화면\git data\first_repo\TEST\배틀싸피대비문제\input2.txt", "r")

def move(y, x, cnt):
    if cnt == len(activate):
        return grid
    act = activate[cnt]
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    d = {"U":0, "D":1, "L":2, "R":3, "S":4}

    see = ["^", "v", "<", ">"]
    act = d[act]
    if act == 4:
        # TODO : 포탄쏠때 함수 구현하고 break 걸기
        if grid[y][x] == '^':
            for i in range(y-1, -1, -1):
                if grid[i][x] == "*":
                    grid[i][x] = "."
                    break
                elif grid[i][x] == "#":
                    break
        
        elif grid[y][x] == 'v':
            for i in range(y+1, h):
                if grid[i][x] == "*":
                    grid[i][x] = "."
                    break 
                elif grid[i][x] == "#":
                    break
        
        elif grid[y][x] == '<':
            for j in range(x-1, -1, -1):
                if grid[y][j] == "*":
                    grid[y][j] = "."
                    break
                elif grid[y][j] == "#":
                    break

        elif grid[y][x] == '>':
            for j in range(x+1, w):
                if grid[y][j] == "*":
                    grid[y][j] = "."
                    break
                elif grid[y][j] == "#":
                    break

        return move(y, x, cnt+1)

    
    grid[y][x] = see[act]
    ny = y + dy[act]
    nx = x + dx[act]
    if ny<0 or nx<0 or ny >= h or nx>=w:
        return move(y, x, cnt+1)
    
    elif grid[ny][nx] == ".":
        grid[y][x] = "."
        grid[ny][nx] = see[act]
        return move(ny, nx, cnt+1)
    
    return move(y, x, cnt+1)

t = int(input())
for tc in range(1, t+1):
    # h: 높이, w:너비
    h, w = map(int, input().split())
    grid = [list(input().strip()) for _ in range(h)]
    n = int(input())
    activate = input().strip()
    
    
    found = False
    for y in range(h):
        for x in range(w):
            if grid[y][x] == "^" or grid[y][x] == "v" or grid[y][x] == ">" or grid[y][x] == "<":
                answer = move(y, x, 0)
                found = True
                break
        if found:
            break
    print(f"#{tc}", end=" ")
    for row in answer:
        print("".join(row))




#==========================gpt코드(단순 시뮬레이션)============================
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