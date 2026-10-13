n, m = map(int, input().split())

# Please write your code here.

board = [[0]*n for _ in range(n)]

dys, dxs = [-1, 0, 1, 0], [0, 1, 0, -1]

def in_range():
    return 0<=ny and ny<n and 0<=nx and nx<n 

for _ in range(m):
    point = list(map(int, input().split()))
    y = point[0]-1
    x = point[1]-1
    board[y][x] = 1
    cnt = 0
    for i in range(4):
        ny = y + dys[i]
        nx = x + dxs[i]

        if in_range() and board[ny][nx]==1:
            cnt +=1
    if cnt == 3:
        print(1)
    else:
        print(0)