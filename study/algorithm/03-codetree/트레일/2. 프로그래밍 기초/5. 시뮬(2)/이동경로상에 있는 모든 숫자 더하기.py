N, T = map(int, input().split())
str = input()
board = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.

dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]

idx = 0

y, x = N//2, N//2

result = [board[y][x]]

for ch in str:
    if ch == 'R':
        idx = (idx + 1) % 4

    elif ch == 'L':
        idx = (idx+3) % 4

    else:
        ny = y + dy[idx]
        nx = x + dx[idx]
        if not(0 <= ny < N and 0 <= nx < N):
            continue
        result.append(board[ny][nx])
        y, x = ny, nx

print(sum(result))