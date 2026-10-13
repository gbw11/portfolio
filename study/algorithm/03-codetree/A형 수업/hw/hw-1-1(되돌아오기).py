N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.

x, y = 0, 0
cnt = 0

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

for ch, dir_num in zip(dir, dist):
    if ch == "N":
        see = 0
    elif ch == 'E':
        see = 1
    elif ch == 'S':
        see = 2
    else:
        see = 3

    for i in range(dir_num):
        x, y = x + dx[see], y + dy[see]
        cnt +=1

        if x==0 and y == 0:
            print(cnt)
            exit()
print(-1)


## gpt 깔끔한 버전 ##
"""
N = int(input())
moves = [input().split() for _ in range(N)]

# 방향 매핑
dir_map = {"N": 0, "E": 1, "S": 2, "W": 3}
dx = [0, 1, 0, -1]  # N, E, S, W
dy = [1, 0, -1, 0]

x = y = cnt = 0

for d, s in moves:
    steps = int(s)
    direction = dir_map[d]
    
    for _ in range(steps):
        x += dx[direction]
        y += dy[direction]
        cnt += 1
        if x == 0 and y == 0:
            print(cnt)
            exit()  # 바로 종료

# 한 번도 (0,0)으로 돌아오지 않으면
print(-1)

"""