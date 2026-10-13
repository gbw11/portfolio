N = int(input())
Q = int(input())
arr = [[0]*N for _ in range(N)]
for _ in range(Q):
    col, y1, x1, y2, x2 = map(int, input().split())

    if y1 > y2: y1, y2 = y2, y1
    if x1 > x2: x1, x2 = x2, x1

    for i in range(y1, y2+1):
        for j in range(x1, x2+1):
            if arr[i][j]<col:
                arr[i][j] = col

max_square = 0
dp = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 0:
            dp[i][j]

        elif i==0 or j==0:
            dp[i][j]=1

        elif arr[i][j] == arr[i-1][j] == arr[i][j-1] == arr[i-1][j-1]:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1

        else:
            dp[i][j]=1

        max_square = max(max_square, dp[i][j])

print(max_square**2)