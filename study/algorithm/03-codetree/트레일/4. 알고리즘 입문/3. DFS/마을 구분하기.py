n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

visited = [[False]*n for _ in range(n)]


def dfs(y, x):
    global people
    visited[y][x] = True

    dys, dxs = [0,0,1,-1], [1,-1,0,0]

    for dy, dx in zip(dys, dxs):
        ny = y + dy
        nx = x + dx

        if 0 <= ny < n and 0 <= nx < n:
            if not visited[ny][nx] and grid[ny][nx]==1:
                visited[ny][nx] = True
                dfs(ny, nx)
                people += 1
                # visited[ny][nx] = False


cnt = 0
ans = []
for y in range(n):
    for x in range(n):
        if grid[y][x] == 1 and not visited[y][x]:
            cnt += 1
            people = 1
            dfs(y,x)
            ans.append(people)
print(cnt)
ans.sort()
for num in ans:
    print(num)