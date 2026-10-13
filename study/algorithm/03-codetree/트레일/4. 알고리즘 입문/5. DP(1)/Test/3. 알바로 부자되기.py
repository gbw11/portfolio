n = int(input())
jobs = [tuple(map(int, input().split())) for _ in range(n)]
s = [job[0] for job in jobs]
e = [job[1] for job in jobs]
p = [job[2] for job in jobs]

# Please write your code here.

dp = [0]*n

for i in range(1, n):
    for j in range(i):
        if e[j] < s[i]:
            dp[i] += p[j]

print(max(dp))