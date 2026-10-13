n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

x, y = 0, 0


for ch, i in zip(dir, dist):
    if ch == "N":
       see = 0
    elif ch == 'E':
        see = 1
    elif ch == 'S':
        see = 2
    else:
        see = 3

    x, y = x + dx[see]*i, y + dy[see]*i

print(x, y)