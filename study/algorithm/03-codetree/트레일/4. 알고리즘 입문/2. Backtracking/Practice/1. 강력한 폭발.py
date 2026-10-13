# 지피티가 짜준 dfs 안에서 터트리고 기록하는거 다 하는 코드
# 내가 짜준 코드는 저 밑에 잇음/ 서로 비교해보기

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

bombs = []
for y in range(n):
    for x in range(n):
        if grid[y][x] == 1:
            bombs.append((y, x))

m = len(bombs)

def in_range(y, x):
    return 0 <= y < n and 0 <= x < n

result = 0

def explode(y, x, type):
    exploded = []

    # 자기 자신
    exploded.append((y, x))

    if type == 1:
        for dy in [-1, 1]:
            for k in range(1, 3):
                ny = y + dy * k
                nx = x + dx * k
                if in_range(ny, nx):
                    exploded.append((ny, nx))

    elif type == 2:
        for dy, dx in [(-1,0),(0,1),(1,0),(0,-1)]:
            ny = y + dy
            nx = x + dx
            if in_range(ny, nx):
                exploded.append((ny, nx))

    else:
        for dy, dx in [(-1,-1),(-1,1),(1,1),(1,-1)]:
            ny = y + dy
            nx = x + dx
            if in_range(ny, nx):
                exploded.append((ny, nx))

    # 실제 반영
    for ny, nx in exploded:
        grid[ny][nx] = 1

    return exploded


def dfs(lev):
    global result

    if lev == m:
        total = sum(sum(row) for row in grid)
        result = max(result, total)
        return

    y, x = bombs[lev]

    for type in range(1, 4):
        exploded = explode(y, x, type)

        dfs(lev + 1)

        # 🔥 복구
        for ny, nx in exploded:
            grid[ny][nx] = 0


dfs(0)

print(result)

# 백트래킹을 제대로 활용하지 못하고 답만 맞춤

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

# m 폭탄의 갯수
m = sum(sum(rows) for rows in grid)

# 범위 벗어나는지 확인하는 함수
def in_range(y, x):
    return 0 <= y < n and 0 <= x < n


def bomb1(y, x):
    # 상하 두칸씩 터지는 폭탄
    dys, dxs = [-1, 1], [0, 0]
    
    for dy, dx in zip(dys, dxs):
        for k in range(1, 3):
            ny = y + dy * k
            nx = x + dx * k
            if not in_range(ny, nx): continue
            temps[ny][nx] = 1

def bomb2(y, x):
    # 상하좌우가 터지는 폭탄
    dys, dxs = [-1, 0, 1, 0], [0, 1, 0, -1]
    
    for dy, dx in zip(dys, dxs):
        ny = y + dy
        nx = x + dx
        if not in_range(ny, nx): continue
        temps[ny][nx] = 1

def bomb3(y, x):
    # 네방향의 대각선이 터지는 폭탄
    dys, dxs = [-1, -1, 1, 1], [-1, 1, 1, -1]
   
    for dy, dx in zip(dys, dxs):
        ny = y + dy
        nx = x + dx
        if not in_range(ny, nx): continue
        temps[ny][nx] = 1


# 각 폭탄 별 터지는 방법을 정리한 배열
cases = []
path = []
def dfs(lev):
    if lev == m:
        cases.append(path[:])
        return

    for i in range(1, 4):
        path.append(i)
        dfs(lev + 1)
        path.pop()
    
    return

dfs(0)

result = m

for case in cases:
    temps = [rows[:] for rows in grid]
    cnt = 0
    for y in range(n):
        for x in range(n):
            if grid[y][x] == 1:
                if case[cnt] == 1:
                    bomb1(y, x)
                    cnt += 1
                
                elif case[cnt] == 2:
                    bomb2(y, x)
                    cnt += 1

                elif case[cnt] == 3:
                    bomb3(y, x)
                    cnt += 1
    result = max(result, sum(sum(rows) for rows in temps))

print(result)