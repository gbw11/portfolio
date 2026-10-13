n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

dp = [float('inf')] * (n+1)

arr.insert(0, 0)
dp[0] = 0

for i in range(1, n+1):
    dp[i] = max(dp[i-1]+arr[i], arr[i])


print(max(dp[1:]))