n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

dx = {'U': -1, 'D': 1, 'L': 0, 'R': 0}
dy = {'U': 0, 'D': 0, 'L': -1, 'R': 1}

def get_next(x, y, board):
    nx = x + dx[board[x][y]]
    ny = y + dy[board[x][y]]
    if 0 <= nx < n and 0 <= ny < m:
        return nx, ny
    return -1, -1


def solve(board):
    state = [[0]*m for _ in range(n)]  # 0=미방문, 1=방문중, 2=완료
    dp = [[0]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if state[i][j] != 0:
                continue

            stack = []
            x, y = i, j

            while True:
                if state[x][y] == 2:
                    val = dp[x][y]
                    break

                if state[x][y] == 1:
                    # 사이클 발견
                    idx = stack.index((x, y))
                    cycle_size = len(stack) - idx

                    # 사이클 부분 처리
                    for cx, cy in stack[idx:]:
                        dp[cx][cy] = cycle_size
                        state[cx][cy] = 2

                    val = cycle_size
                    stack = stack[:idx]
                    break

                state[x][y] = 1
                stack.append((x, y))

                nx, ny = get_next(x, y, board)
                if nx == -1:
                    val = 0
                    break

                x, y = nx, ny

            # 사이클 앞쪽 경로 처리
            while stack:
                px, py = stack.pop()
                val += 1
                dp[px][py] = val
                state[px][py] = 2

    ans = 0
    for i in range(n):
        for j in range(m):
            ans = max(ans, dp[i][j])

    return ans


answer = solve(grid)

# 행 변경
for r in range(n):
    original = grid[r][:]
    for d in ['U', 'D', 'L', 'R']:
        grid[r] = [d]*m
        answer = max(answer, solve(grid))
    grid[r] = original

# 열 변경
for c in range(m):
    original = [grid[i][c] for i in range(n)]
    for d in ['U', 'D', 'L', 'R']:
        for i in range(n):
            grid[i][c] = d
        answer = max(answer, solve(grid))
    for i in range(n):
        grid[i][c] = original[i]

print(answer)