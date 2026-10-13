n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.


dys, dxs = [-1, 0, 1, 0], [0, 1, 0, -1]


def in_range(y,x):
    return 0<=x and x<n and 0<=y and y<n

num = 0
for y in range(n):
    for x in range(n):
        cnt = 0
        for dy, dx in zip(dys, dxs):
            ny = y + dy
            nx = x + dx
            if in_range(ny,nx) and grid[ny][nx]==1:
                cnt+=1
        if cnt >=3:
            num +=1
print(num)
