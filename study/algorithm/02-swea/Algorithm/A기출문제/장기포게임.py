T = int(input())
 
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
 
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 2:
                sy, sx = y, x
 
    ans = set()
 
    def dfs(y, x, cnt):
        global ans
 
        if cnt == 3:
            return
 
        for d in range(4):
            wall = 0
            for k in range(1, N):
                ny = y + dy[d] * k
                nx = x + dx[d] * k
                if not (0 <= ny < N and 0 <= nx < N):
                    break
 
                if arr[ny][nx] == 2:
                    break
 
                if arr[ny][nx] == 1:
                    wall += 1
                    if wall == 2:
                        ans.add((ny, nx))
 
                        arr[ny][nx] = 2
                        arr[y][x] = 0
 
                        dfs(ny, nx, cnt + 1)
 
                        arr[ny][nx] = 1
                        arr[y][x] = 2
 
                elif wall == 1:
                    arr[ny][nx] = 2
                    arr[y][x] = 0
                    dfs(ny, nx, cnt + 1)
                    arr[ny][nx] = 0
                    arr[y][x] = 2
    dfs(sy, sx, 0)
    print(f'#{tc} {len(ans)}')