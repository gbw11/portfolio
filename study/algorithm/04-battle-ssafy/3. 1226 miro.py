# 1 : 벽, 0 : 길, 2: 출발점, 3: 도착점

def dfs(y, x):
    global ans
    if grid[y][x] == 3:
        ans =1
        return
    
    for dy, dx in [(0, 1),(0,-1), (1,0), (-1,0)]:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < 16 and 0 <= nx < 16:
            if not visited[ny][nx] and grid[ny][nx]!=1:                
                visited[ny][nx] = True
                dfs(ny, nx)
                visited[ny][nx] = False


for _ in range(10):
    tc = int(input())
    grid = [list(map(int, input().strip())) for _ in range(16)]

    visited = [[False]*16 for _ in range(16)]
    ans = 0
    valid = False
    for y in range(16):
        for x in range(16):
            if grid[y][x] == 2:
                visited[y][x] = True
                dfs(y, x)
                valid = True
                break
        if valid:
            break
    print(f'#{tc}', ans)
    # 도착가능하면 1 아니면 0



#================= ai code-==============
# 1 : 벽, 0 : 길, 2: 출발점, 3: 도착점

def dfs(y, x):
    global ans

    if ans:  # 이미 도착했으면 더 탐색 안함
        return

    if grid[y][x] == 3:
        ans = 1
        return

    for dy, dx in directions:
        ny, nx = y + dy, x + dx

        if 0 <= ny < 16 and 0 <= nx < 16:
            if not visited[ny][nx] and grid[ny][nx] != 1:
                visited[ny][nx] = True
                dfs(ny, nx)


for _ in range(10):
    tc = int(input())
    grid = [list(map(int, input().strip())) for _ in range(16)]

    visited = [[False]*16 for _ in range(16)]
    ans = 0

    # 방향 (상, 하, 좌, 우)
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    # 시작점 찾기
    for y in range(16):
        for x in range(16):
            if grid[y][x] == 2:
                sy, sx = y, x
                break
        else:
            continue
        break

    visited[sy][sx] = True
    dfs(sy, sx)

    print(f'#{tc}', ans)