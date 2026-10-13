n, m = map(int, input().split())
# points = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
arr = [[0]*n for _ in range(n)]

dys, dxs = [-1, 0, 1, 0], [0, 1, 0, -1]

def in_range():
    return 0<=ny and ny<n and 0<=nx and nx<n 

for _ in range(m):
    r, c = map(int, input().split())
    y, x = r-1, c-1

    arr[y][x] = 1
    cnt = 0
    for i in range(4):
        ny = y + dys[i]
        nx = x + dxs[i]
        if not in_range():
            continue
        if arr[ny][nx]==1:
            cnt +=1
    if cnt ==3:
        print(1)
    else:
        print(0)