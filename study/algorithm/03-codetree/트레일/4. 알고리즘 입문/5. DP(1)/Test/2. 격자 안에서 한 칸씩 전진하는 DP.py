n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.


dp = [[0]*n for _ in range(n)]

def initialize():
    dp[0][n-1] = grid[0][n-1]

    for i in range(n-2, -1, -1):
        dp[0][i] = dp[0][i+1] + grid[0][i]

    for i in range(1, n):
        dp[i][n-1] = dp[i-1][n-1] + grid[i][n-1]

initialize()

for y in range(1, n):
    for x in range(n-2, -1, -1):
        dp[y][x] = min(dp[y-1][x] + grid[y][x], dp[y][x+1] + grid[y][x])

print(dp[n-1][0])