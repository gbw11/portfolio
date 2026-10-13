n, m = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(n)])
w, v = list(w), list(v)

# Please write your code here.

dp = [-1]*(m+1)
dp[0] = 0

for i in range(n):
    for j in range(m,w[i]-1,-1):
        if dp[j-w[i]] != -1:
            dp[j] = max(dp[j], dp[j-w[i]]+v[i])

# 정확히 m이 될때가 아니라 m 이하에서 최대를 구하는 거기 때문에!
print(max(dp))