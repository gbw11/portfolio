n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

visited = [[0]*n for _ in range(n)]

def in_range(y, x):
    return 0 <= y < n and 0 <= x < n

def can_go(y, x, target):
    if not in_range(y, x):
        return False
    if visited[y][x] or grid[y][x] != target:
        return False
    return True


def dfs(y, x):
    global cnt
    dys, dxs = [-1, 0, 1, 0], [0, 1, 0, -1]

    for dy, dx in zip(dys, dxs):
        ny = y + dy
        nx = x + dx
        if can_go(ny, nx, grid[y][x]):
            cnt += 1
            visited[ny][nx] = 1
            dfs(ny, nx)

    

result = 0
block_cnt = 0
for y in range(n):
    for x in range(n):
        if not visited[y][x]:
            visited[y][x] = 1
            cnt = 1
            dfs(y, x)
            result = max(result, cnt)
            
            if cnt >= 4: block_cnt +=1

print(block_cnt, result)