n, m, r, c = map(int, input().split())
directions = list(input().split())


r, c = r - 1, c - 1

board = [[0] * n for _ in range(n)]

dice = {
    1: [2, 3, 5, 4],
    2: [6, 3, 1, 4],
    3: [1, 2, 6, 5],
    4: [1, 5, 6, 2],
    5: [6, 4, 1, 3],
    6: [2, 4, 5, 3],
}

dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]

front = 2
down = 6
board[r][c] = down
y, x = r, c
for dir in directions:
    if dir == 'R':
        ny, nx = y + dy[1], x + dx[1]
        if not (0 <= ny < n and 0 <= nx < n): continue
        for i, num in enumerate(dice[front]):
            if num == down:
                down = dice[front][(i+1) % 4]
                break
        y, x = ny, nx
        board[y][x] = down

    elif dir == 'L':
        ny, nx = y + dy[3], x + dx[3]
        if not (0 <= ny < n and 0 <= nx < n): continue
        for i, num in enumerate(dice[front]):
            if num == down:
                down = dice[front][(i+3) % 4]
                break
        y, x = ny, nx
        board[y][x] = down

    elif dir == 'U':
        ny, nx = y + dy[0], x + dx[0]
        if not (0 <= ny < n and 0 <= nx < n): continue
        front, down = down, 7 - front
        y, x = ny, nx
        board[y][x] = down

    else:  # 'D'
        ny, nx = y + dy[2], x + dx[2]
        if not (0 <= ny < n and 0 <= nx < n): continue
        front, down = 7 - down, front
        y, x = ny, nx
        board[y][x] = down


result = sum(map(sum, board))

print(result)