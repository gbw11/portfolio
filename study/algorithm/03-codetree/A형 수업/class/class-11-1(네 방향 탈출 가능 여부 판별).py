n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

visited = [[False]*m for _ in range(n)]

stack = [(0,0)]
visited[0][0] = True

while stack:
    y, x = stack.pop()
    
    for dy, dx in [(0,1),(0,-1),(1,0),(-1,0)]:
        ny = y + dy
        nx = x + dx
        
        if 0 <= ny < n and 0 <= nx < m:
            if not visited[ny][nx] and a[ny][nx] == 1:
                visited[ny][nx] = True
                stack.append((ny,nx))

if visited[n-1][m-1]:
    print(1)
else:
    print(0)