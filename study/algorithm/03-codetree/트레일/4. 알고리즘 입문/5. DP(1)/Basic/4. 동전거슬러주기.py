n, m = map(int, input().split())
coin = list(map(int, input().split()))

# Please write your code here.

dp = [float('inf')]*(m+1)

dp[0] = 0
for i in range(1, m+1):
    for j in range(n):
        if i >= coin[j]:
            if dp[i-coin[j]] == float('inf'):
                continue

            dp[i] = min(dp[i], dp[i-coin[j]]+1)

print(dp[m] if dp[m]!= float('inf') else -1)