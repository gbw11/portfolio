n = int(input())

# Please write your code here.

def fibbo(n):
    if n == 2 or n==3:
        return 1

    dp = [0] * (n + 1)

    dp[2] = 1
    dp[3] = 1
    dp[4] = 1


    for i in range(5, n+1):
        dp[i] = dp[i-3] + dp[i-2]

    return dp[n] % 10007

print(fibbo(n))