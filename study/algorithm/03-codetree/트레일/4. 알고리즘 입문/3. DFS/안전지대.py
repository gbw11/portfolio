import sys
# 재귀 함수의 깊이를 늘려주는 방법!!
sys.setrecursionlimit(2500)

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

K = max(max(rows) for rows in grid)

def dfs(y, x):

    visited[y][x] = True

    dys, dxs = [0,0,1,-1], [1,-1,0,0]

    for dy, dx in zip(dys, dxs):
        ny = y + dy
        nx = x + dx
        if 0 <= ny < n and 0 <= nx < m:
            if grid[ny][nx] > k and not visited[ny][nx]:
                visited[ny][nx] = True
                dfs(ny, nx)

ans = []
for k in range(1, K):
    visited = [[False]*m for _ in range(n)]
    # 안정영역의 수 체크
    cnt = 0
    for y in range(n):
        for x in range(m):
            if grid[y][x]>k and not visited[y][x]:
                cnt += 1
                dfs(y,x)
    ans.append((k, cnt))

# 최대가 될때의 k개가 여러개일 경우 작은 k를 출력하기 위함
ans.sort(key = lambda x:(-x[1], x[0]))
if ans:
    print(*ans[0])

else:
    print(*(1, 0))