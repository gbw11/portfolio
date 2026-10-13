n = int(input())
coin = [0] + list(map(int, input().split()))

# Please write your code here.


dp = [[float('-inf')]*4 for _ in range(n+1)]
dp[0][0] = 0
for i in range(1, n+1):
    for j in range(4):
        # 1칸 이동으로 도달 (j >= 1이어야 함)
        if j >= 1 and dp[i-1][j-1] != float('-inf'):
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + coin[i])
        # 2칸 이동으로 도달 (i >= 2이어야 함)
        if i >= 2 and dp[i-2][j] != float('-inf'):
            dp[i][j] = max(dp[i][j], dp[i-2][j] + coin[i])

print(max(dp[n]))