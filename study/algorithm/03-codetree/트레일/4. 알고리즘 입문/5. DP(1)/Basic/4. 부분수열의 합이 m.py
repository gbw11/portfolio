n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

dp = [float('inf')]*(m+1)

dp[0] = 0

for i in range(n):
    for j in range(m,arr[i]-1,-1):
        if dp[j-arr[i]] != float('inf'):
            dp[j] = min(dp[j], dp[j-arr[i]]+1)

print(dp[m] if dp[m] != float('inf') else -1)