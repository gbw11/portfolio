n, m = map(int, input().split())
quests = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

k = max(tmp[0] for tmp in quests)
dp = [1000000]*(m+k+1)
dp[0] = 0

for j in range(n):
    w, c = quests[j]
    for i in range(m+k,w-1,-1):
        if dp[i-w] != 1000000:
            dp[i] = min(dp[i], dp[i-w]+c)

ans = min(dp[m:])
print(ans if ans != 1000000 else -1)