from collections import deque

n, k, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

start = []
for _ in range(k):
    ri, ci = map(int, input().split())
    start.append((ri, ci))

# Please write your code here.

def in_range(y, x):
    return 0 <= y < n and 0 <= x <n

visited = [[[False]*(k+1) for _ in range(n)] for _ in range(n)]
dys, dxs = [0,0,1,-1], [1,-1,0,0]

def bfs(sy, sx):
    global ans
    q = deque()
    # y, x, stone
    q.append((sy, sx, 0))
    visited[sy][sx][0] = True

    cnt = 0

    while q:
        y, x, used = q.popleft()

        for dy, dx in zip(dys, dxs):
            ny = y + dy
            nx = x + dx
            if not in_range(ny, nx): continue

            # 빈칸
            if grid[ny][nx] == 0 and not visited[ny][nx][used]:
                visited[ny][nx][used] = True
                q.append((ny, nx, used))
                cnt += 1

            # 돌
            elif grid[ny][nx] == 1 and used < k and not visited[ny][nx][used+1]:
                visited[ny][nx][used+1] = True
                q.append((ny, nx, used+1))
                cnt += 1
    ans = max(ans, cnt)
    return
                    
ans = 0

for s in start:
    bfs(s[0], s[1])
    
print(ans)